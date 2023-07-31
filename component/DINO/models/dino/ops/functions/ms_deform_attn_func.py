# ------------------------------------------------------------------------------------------------
# Deformable DETR
# Copyright (c) 2020 SenseTime. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 [see LICENSE for details]
# ------------------------------------------------------------------------------------------------
# Modified from https://github.com/chengdazhi/Deformable-Convolution-V2-PyTorch/tree/pytorch_1.0.0
# ------------------------------------------------------------------------------------------------

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import torch
import torch.nn.functional as F
from torch.autograd import Function
from torch.autograd.function import once_differentiable

# import MultiScaleDeformableAttention as MSDA
from torch import Tensor, nn  

def multi_scale_deformable_attention(
    value: Tensor, value_spatial_shapes: Tensor, level_start_index, sampling_locations: Tensor, attention_weights: Tensor, im2col_step
) -> Tensor:
    batch_size, _, num_heads, hidden_dim = value.shape
    _, num_queries, num_heads, num_levels, num_points, _ = sampling_locations.shape
    value_list = value.split([height * width for height, width in value_spatial_shapes], dim=1)
    
    sampling_grids = 2 * sampling_locations - 1
    sampling_value_list = []
    for level_id, (height, width) in enumerate(value_spatial_shapes):
        # batch_size, height*width, num_heads, hidden_dim
        # -> batch_size, height*width, num_heads*hidden_dim
        # -> batch_size, num_heads*hidden_dim, height*width
        # -> batch_size*num_heads, hidden_dim, height, width
        value_l_ = (
            value_list[level_id].flatten(2).transpose(1, 2).reshape(batch_size * num_heads, hidden_dim, height, width)
        )
        # batch_size, num_queries, num_heads, num_points, 2
        # -> batch_size, num_heads, num_queries, num_points, 2
        # -> batch_size*num_heads, num_queries, num_points, 2
        sampling_grid_l_ = sampling_grids[:, :, :, level_id].transpose(1, 2).flatten(0, 1)
        # batch_size*num_heads, hidden_dim, num_queries, num_points
        sampling_value_l_ = nn.functional.grid_sample(
            value_l_, sampling_grid_l_, mode="bilinear", padding_mode="zeros", align_corners=False
        )
        sampling_value_list.append(sampling_value_l_)
    # (batch_size, num_queries, num_heads, num_levels, num_points)
    # -> (batch_size, num_heads, num_queries, num_levels, num_points)
    # -> (batch_size, num_heads, 1, num_queries, num_levels*num_points)
    attention_weights = attention_weights.transpose(1, 2).reshape(
        batch_size * num_heads, 1, num_queries, num_levels * num_points
    )
    output = (
        (torch.stack(sampling_value_list, dim=-2).flatten(-2) * attention_weights)
        .sum(-1)
        .view(batch_size, num_heads * hidden_dim, num_queries)
    )
    return output.transpose(1, 2).contiguous()

def ms_deform_attn_core_pytorch(value, value_spatial_shapes, sampling_locations, attention_weights):
    
    # for debug and test only,
    # need to use cuda version instead
    
    N_, S_, M_, D_ = value.shape
    _, Lq_, M_, L_, P_, _ = sampling_locations.shape
    
    start_idx = []
    for idx, (H_, W_) in enumerate(value_spatial_shapes):
        tmp = int(H_ * W_)
        if len(start_idx) > 0:
            tmp += start_idx[idx-1]
        start_idx.append(tmp)

    value_list = [
        value[:,0:start_idx[0],:,:],
        value[:,start_idx[0]:start_idx[1],:,:],
        value[:,start_idx[1]:start_idx[2],:,:],
        value[:,start_idx[2]:start_idx[3],:,:],
    ]
    
    sampling_grids = 2 * sampling_locations - 1    
    
    sampling_value_list = []
    for lid_, (H_, W_) in enumerate(value_spatial_shapes):
        # N_, H_*W_, M_, D_ -> N_, H_*W_, M_*D_ -> N_, M_*D_, H_*W_ -> N_*M_, D_, H_, W_
        value_l_ = value_list[lid_].flatten(2).transpose(1, 2).reshape(N_*M_, D_, int(H_), int(W_))
        # N_, Lq_, M_, P_, 2 -> N_, M_, Lq_, P_, 2 -> N_*M_, Lq_, P_, 2
        sampling_grid_l_ = sampling_grids[:, :, :, lid_].transpose(1, 2).flatten(0, 1)
        
        sampling_value_l_ = F.grid_sample(value_l_, sampling_grid_l_,mode='bilinear', padding_mode='zeros', align_corners=True)
        # sampling_value_l_ = custom_grid_sample(value_l_, sampling_grid_l_, align_corners=False)
        sampling_value_list.append(sampling_value_l_) 
        

        
        # # N_*M_, D_, Lq_, P_
        # sampling_value_l_ = F.grid_sample(value_l_, sampling_grid_l_,mode='bilinear', padding_mode='zeros', align_corners=True) # <- 이 부분 사용
        # # sampling_value_l_ = custom_grid_sample(value_l_.to('cpu'), sampling_grid_l_.to('cpu'), align_corners=True).to('cuda')
        # sampling_value_list.append(sampling_value_l_)
    
    # sampling_value_list, N_, M_, L_, P_, D_, Lq_ = roof(value, sampling_locations, value_spatial_shapes.type(torch.float32))

# import numpy as np
# np.isclose(
#     a.cpu().detach().numpy(),
#     b.cpu().detach().numpy()
# )

    # (N_, Lq_, M_, L_, P_) -> (N_, M_, Lq_, L_, P_) -> (N_, M_, 1, Lq_, L_*P_) -> 원래부터 없던 코드
    attention_weights = attention_weights.transpose(1, 2).reshape(N_*M_, 1, Lq_, L_*P_)
    output = (torch.stack(sampling_value_list, dim=-2).flatten(-2) * attention_weights).sum(-1).view(N_, M_*D_, Lq_)
    return output.transpose(1, 2).contiguous()

def ms_deform_attn_core_pytorch(value, value_spatial_shapes, sampling_locations, attention_weights):
    # for debug and test only,
    # need to use cuda version instead
    N_, S_, M_, D_ = value.shape
    _, Lq_, M_, L_, P_, _ = sampling_locations.shape
    value_list = value.split([H_ * W_ for H_, W_ in value_spatial_shapes], dim=1)
    sampling_grids = 2 * sampling_locations - 1
    sampling_value_list = []
    for lid_, (H_, W_) in enumerate(value_spatial_shapes):
        # N_, H_*W_, M_, D_ -> N_, H_*W_, M_*D_ -> N_, M_*D_, H_*W_ -> N_*M_, D_, H_, W_
        value_l_ = value_list[lid_].flatten(2).transpose(1, 2).reshape(N_*M_, D_, H_, W_)
        # N_, Lq_, M_, P_, 2 -> N_, M_, Lq_, P_, 2 -> N_*M_, Lq_, P_, 2
        sampling_grid_l_ = sampling_grids[:, :, :, lid_].transpose(1, 2).flatten(0, 1)
        # N_*M_, D_, Lq_, P_
        sampling_value_l_ = F.grid_sample(value_l_, sampling_grid_l_,
                                          mode='bilinear', padding_mode='zeros', align_corners=False)
        sampling_value_list.append(sampling_value_l_)
    # (N_, Lq_, M_, L_, P_) -> (N_, M_, Lq_, L_, P_) -> (N_, M_, 1, Lq_, L_*P_)
    attention_weights = attention_weights.transpose(1, 2).reshape(N_*M_, 1, Lq_, L_*P_)
    output = (torch.stack(sampling_value_list, dim=-2).flatten(-2) * attention_weights).sum(-1).view(N_, M_*D_, Lq_)
    return output.transpose(1, 2).contiguous()
