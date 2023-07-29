import React, { useEffect, useState, useCallback, useContext } from 'react';
// import AsyncStorage from '@react-native-async-storage/async-storage';

import {
    StyleSheet, Text, View,
    TextInput, Pressable, Button,
} from 'react-native';
import axios from 'axios';
import BouncyCheckbox from "react-native-bouncy-checkbox";

import { dataContext } from '../../App';
import { LOGIN } from '../../App';

export default function LoginPage({ navigation }) {
    const [login, setLogin] = useState(false);
    const [signUp, setSignUp] = useState(false);
    const [id, setId] = useState('');
    const [password, setPassword] = useState('');
    const [name, setName] = useState('');
    const [showpass, setshowpass] = useState(true);

    const { dispatch } = useContext(dataContext);

    const swap = useCallback(() => {
        setId('');
        setPassword('');
        setName('');
        if (signUp === false) {
            setSignUp(true);
        } else if (signUp === true) {
            setSignUp(false);
        }
    }, [signUp]);

    useEffect(() => {
        dispatch({
            type: LOGIN,
            login: login,
        });
    }, [dispatch, login]);


    // 회원가입
    const checkSignUp = async () => {
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
                    .post('/user/signup', data)
                    .then(function async(response) {
                        console.log(response);
                        if (response.data["success"] === true) {
                            setLogin(false);
                        }
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

    // 로그인
    const checkLogin = () => {
        axios.post('http://192.168.0.9:8000/user/login', {
            email: id,
            password: password
        })
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    return (
        <View style={{ ...styles.login }}>
            <Text style={{ ...styles.loginText }}>총 알</Text>

            <View style={{ alignItems: 'center' }}>
                <TextInput
                    style={{ ...styles.loginInput }} placeholder="아이디" autoCapitalize="none"
                    value={id} onChangeText={(text) => setId(text)} autoCorrect={false}/>
                <TextInput
                    style={{ ...styles.loginInput }} placeholder="비밀번호" autoCapitalize="none"
                    autoCorrect={false} secureTextEntry={true} value={password}
                    onChangeText={(text) => setPassword(text)}
                    textContentType="password"/>

                <BouncyCheckbox
                    size={20} fillColor="black" unfillColor="#FFFFFF"
                    text="비밀번호 보기" iconStyle={{ borderColor: 'red', marginTop: 5, color: 'black' }}
                    textStyle={{ fontFamily: 'JosefinSans-Regular' }}
                    onPress={() => setshowpass(!showpass)}
                />

                {signUp ? (
                    <TextInput
                        style={{ ...styles.loginInput, marginBottom: 20 }}
                        autoCapitalize="none" autoCorrect={false}
                        value={name} onChangeText={(text) => setName(text)}
                        placeholder="이름">
                    </TextInput>
                ) : null}

            </View>

            {!signUp ? (
                <View>
                    <View style={{ marginTop: 10 }}>
                        <Button title="로그인" touchSoundDisabled
                            onPress={checkLogin}
                        />
                    </View>
                    <View style={{ marginTop: 10 }}>
                        <Button title="회원가입" touchSoundDisabled
                            onPress={swap}
                        />
                    </View>
                </View>
            ) :
                <View>
                    <View>
                        <Button title="제출하기" touchSoundDisabled
                            onPress={checkSignUp}
                        />
                    </View>
                    <View style={{ marginTop: 10 }}>
                        <Button
                            title="뒤로가기" touchSoundDisabled
                            onPress={swap}
                        />
                    </View>
                </View>}
        </View>
    );
}

const styles = StyleSheet.create({
    login: {
        borderWidth: 2,
        borderRadius: 5,
        borderStyle: 'solid',
        backgroundColor: '#0081f1',

        width: '70%',
    },
    loginText: {
        color: "white",

        marginTop: 20,

        textAlign: 'center',
        fontSize: 30,
        fontWeight: 700,
    },
    loginInput: {
        color: "white",

        width: '90%',
        paddingVertical: 5,
        paddingHorizontal: 15,

        borderWidth: 2,
        borderRadius: 5,
        borderStyle: 'solid',

        marginTop: 20,
        fontSize: 18,
    },
});