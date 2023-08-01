import AsyncStorage from '@react-native-async-storage/async-storage';

import React, { useEffect, useState, memo, useContext } from "react";
import {
    Text, Button,
    View,
} from 'react-native';

import { dataContext } from '../../App';
import { LOGOUT } from "../../App";

const MyPage = memo(()=>{

    const { dispatch } = useContext(dataContext);


    return(
        <View>
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
})

export default MyPage;
