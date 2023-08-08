import AsyncStorage from '@react-native-async-storage/async-storage';

import React, { useEffect, useState, memo, useContext, useRef } from "react";
import {
    Text, Button,
    View,
} from 'react-native';
import { TOKEN, NAME } from '../../App';

import { dataContext } from '../../App';
import { LOGOUT } from "../../App";

const MyPage = ()=>{

    const { dispatch,user } = useContext(dataContext);
    const [name,setName]=useState('');

    useEffect(()=>{
        AsyncStorage.getItem(NAME).then(value => setName(value))
    },[])

    return(
        <View>
            <View><Text>{name}</Text></View>
            <Button title="로그아웃" 
            onPress={()=>{
                dispatch({
                    type : LOGOUT,
                    login : false,
                });
                AsyncStorage.clear();
            }} />

        </View>
    )
}

export default MyPage;
