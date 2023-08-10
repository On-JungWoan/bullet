// basic
import React, { useEffect, useState, useContext, useCallback } from "react";
import {
    Text, View, TextInput, Button
} from 'react-native';

// install
import axios from "axios";

// from App.js
import { AddKEYWORD} from "../../App";
import { dataContext, BaseURL } from '../../App';

export default function KeywordsSelectPage({ keywords, token }) {
    const { dispatch, user } = useContext(dataContext);
    
    const postKeyword = async()=>{
        if(keywords?.length===0){
            alert('선택한 단어가 없습니다.');
            return;
        }

        dispatch({
            type:AddKEYWORD,
            keywords: keywords,
        })
        const data={
            keywords : keywords,
        }
        try{
            await axios
                .post(`${BaseURL}/user/keyword/create/`, data, {
                    headers: {
                        Authorization: token,
                    },
                }
                )
                .then(function (response) {
                    console.log("keyword",response.data);
                    
                })
                .catch(function (error) {
                    alert("에러발생")
                    console.log("error", error);
                    throw error;
                });
        } catch (error){
            console.log("error", error);
            throw error;
        }

    }

    return(
        <View>
            <View>
                {keywords?.length ? <Text style={{ fontSize: 20 }}>{`keywords : ${keywords} `}</Text> : null}
            </View>
            <Button title="완료" onPress={() => {
                postKeyword();
            }} />
        </View>
    )
}