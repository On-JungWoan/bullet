import torch
from transformers import PreTrainedTokenizerFast
from transformers import BartForConditionalGeneration

def summarize(
        text:str,
        demo:bool=False
    ) -> str:
    tokenizer = PreTrainedTokenizerFast.from_pretrained('digit82/kobart-summarization')
    model = BartForConditionalGeneration.from_pretrained('digit82/kobart-summarization')

    if demo:
        with open('component/KoBART-summarization/target.txt', 'r', encoding="UTF-8") as f:
            text = f.readlines()
            text = ''.join(text)

    text = text.replace('\n', ' ')

    raw_input_ids = tokenizer.encode(text[:500])
    input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]

    summary_ids = model.generate(torch.tensor([input_ids]),  num_beams=4,  max_length=512,  eos_token_id=1)
    result = tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)
    print(f"\n\n{'='*50} 요약결과 {'='*50}")
    print(result)

    return result