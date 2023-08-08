import React, { useEffect, useState, useCallback, useContext } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';

import {
    StyleSheet, Text, View, ActivityIndicator,
    TextInput, Pressable, Button,
} from 'react-native';
import axios from 'axios';
import BouncyCheckbox from "react-native-bouncy-checkbox";
import { useNavigation } from '@react-navigation/native';

import { TOKEN } from '../../App';
import { NAME } from '../../App';
import { dataContext } from '../../App';
import { LOGIN } from '../../App';
import { BaseURL } from '../../App';

export default function SignUp() {
    const [signUp, setSignUp] = useState(false);

    const [id, setId] = useState('');
    const [password, setPassword] = useState('');
    const [name, setName] = useState('');

    const { dispatch } = useContext(dataContext);

    const navigation = useNavigation();

    // 회원가입
    const checkSignUp = async () => {
        console.log("회원가입")
        if (id === "" || password === "") {
            alert('아이디와 비밀번호를 입력해 주세요');
        } else {
            const data = {
                email: id,
                password: password,
                username: name
            }
            try {
                await axios
                    .post(`${BaseURL}/user/signup/`, data)
                    .then(function (response) {
                        console.log("checkSignUp", response.data);
                        setPassword("");
                        alert("회원가입을 축하드립니다.")
                        setSignUp(false);
                    })
                    .catch(function (error) {
                        alert("에러발생")
                        console.log(error);
                        throw error;
                    });
            } catch (error) {
                console.log(error);
                throw error;
            }
        }
    }


    return (
        <View>
            <Text>회원가입</Text>
            <Button title="로그인으로" onPress={()=>{navigation.navigate("Login")}}/>
        </View>

    );
}