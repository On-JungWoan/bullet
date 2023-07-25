import React, { useEffect, useState, useCallback, useContext } from 'react';
// import AsyncStorage from '@react-native-async-storage/async-storage';

import {
    StyleSheet, Text, View,
    TextInput, Pressable, Button,
} from 'react-native';

import { dataContext } from '../../App';
import { LOGIN } from '../../App';

export default function LoginPage({navigation}) {
    const [login, setLogin] = useState(false);

    const { dispatch } = useContext(dataContext);

    const doLogin = () => {
        if (!login) {
            setLogin(true);
        } else {
            setLogin(false);
        }
    };

    useEffect(() => {
        console.log('Login.js', login);
        dispatch({
            type: LOGIN,
            login: login,
        })
    }, [dispatch, login]);

    return (
        <View style={{ ...styles.login }}>
            <Text style={{ ...styles.loginText }}>
                총 알
            </Text>

            <View style={{ alignItems: 'center' }}>
                <TextInput
                    style={{ ...styles.loginInput }}
                    placeholder="아이디"></TextInput>
                <TextInput
                    style={{ ...styles.loginInput, marginBottom: 20, }}
                    placeholder="비밀번호"></TextInput>
            </View>


            <View style={{ justifyContent: "center", alignItems: "center", marginBottom: 10, }}>
                <Pressable style={styles.loginBtn} onPress={doLogin}>
                    <Text style={{ textAlign: "center", color: "white" }}>로그인</Text>
                </Pressable>
            </View>
            <View>
                <Button title="SignUp"
                    onPress={() => navigation.navigate('SignUp')}
                >회원가입</Button>
            </View>
        </View>
    )
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
    loginBtn: {
        paddingHorizontal: 8,
        paddingVertical: 5,

        color: "white",
        width: "30%",

        borderWidth: 2,
        borderRadius: 5,
        borderStyle: 'solid',

    },
});