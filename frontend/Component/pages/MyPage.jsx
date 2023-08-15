import AsyncStorage from '@react-native-async-storage/async-storage';

import React, { useEffect, useState, memo, useContext, useRef } from "react";
import {
    Text, Button, View,
} from 'react-native';
import { NAME } from '../../App';

import { useNavigation } from '@react-navigation/native';
import { dataContext } from '../../App';
import { LOGOUT } from "../../App";

const MyPage = ()=>{

    const navigation = useNavigation();

    const { dispatch,user } = useContext(dataContext);
    const [name,setName]=useState('');

    useEffect(()=>{
        AsyncStorage.getItem(NAME).then(value => setName(value))
    },[])

    return(
        <View>
            <View><Text>{name}</Text></View>
            <Text>{user.keywords}</Text>
            <Text>{user.newsSites}</Text>
            <Text>{user.uniSites}</Text>
            <Text>{user.workSites}</Text>
            <Button title="로그아웃" 
            onPress={()=>{
                dispatch({
                    type : LOGOUT,
                    login : false,
                });
                navigation.navigate("Login")
                AsyncStorage.clear();
            }} />

        </View>
    )
}

export default MyPage;
