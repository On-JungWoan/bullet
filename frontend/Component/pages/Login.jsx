import React, { useEffect, useState, useCallback, useContext } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';

import {
    StyleSheet, Text, View, ActivityIndicator,
    TextInput, Pressable, Button,
} from 'react-native';
import axios from 'axios';
import BouncyCheckbox from "react-native-bouncy-checkbox";

import { TOKEN } from '../../App';
import { NAME } from '../../App';
import { dataContext } from '../../App';
import { LOGIN } from '../../App';
import { BaseURL } from '../../App';

export default function LoginPage({ navigation }) {
    const [login, setLogin] = useState(false);
    const [signUp, setSignUp] = useState(false);

    const [id, setId] = useState('');
    const [password, setPassword] = useState('');
    const [name, setName] = useState('');
    const [sites, setSites] = useState([]);
    const [keywords, setKeywords] = useState([]);

    const [showpass, setshowpass] = useState(true);
    const [loading, setLoading] = useState(true);

    const { dispatch } = useContext(dataContext);

    let token;

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

    // 자동 로그인시 등록 키워드 가져오기
    const getKeyword = useCallback(async () => {
        console.log("getKeyword");
        try {
            await axios.get(`${BaseURL}/user/keyword/`, {
                headers: {
                    Authorization: token,
                }
            })
                .then((response) => {
                    console.log("getKeyword", response.data);
                    setKeywords(response.data)
                })
        } catch (error) {
            console.log(error);
            throw error;
        }
    }, [keywords]);

    // 자동 로그인시 등록 사이트 가져오기
    const getSite = useCallback(async () => {
        console.log("getSite");
        try {
            await axios.get(`${BaseURL}/user/site/`, {
                headers: {
                    Authorization: token,
                }
            })
                .then((response) => {
                    console.log("getSites", response.data);
                    setSites(response.data);
                })
        } catch (error) {
            console.log(error);
            throw error;
        }
    }, [sites]);

    useEffect(() => {
        console.log("user정보 dispatch");

        dispatch({
            type: LOGIN,
            login: login,
            sites: sites,
            name: AsyncStorage.getItem(NAME),
            keywords: keywords,
        });
    }, [login,sites,keywords]);

    // 초기 로그인 확인
    useEffect(() => {
        console.log(" 초기 로그인 확인")
        AsyncStorage.getItem(TOKEN)
            .then(value => {
                if (value) { // 자동 로그인
                    token = value;
                    console.log("token", token)

                    getSite();
                    getKeyword();

                    setLogin(true);
                } else {
                    setLoading(false);
                }
            })
    }, [])

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

    // 로그인
    const checkLogin = async () => {
        console.log("로그인")
        const data = {
            email: id,
            password: password
        }
        await axios
            .post(`${BaseURL}/user/login/`, data)
            .then(function (response) {
                console.log("checkLogin", response.data)
                AsyncStorage.setItem(TOKEN, response.headers.authorization); // 자동 로그인 token 저장
                AsyncStorage.setItem(NAME, response.data.username); // 이름은 로컬에도 저장
                setSites(response.data.sites?.length !== 0 ? [...response.data.sites] : []) // 저장한 사이트
                setKeywords(response.data.keywords?.length !== 0 ? [...response.data.keywords] : []) // 저장한 키워드
                setLogin(true);
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    return (
        <View>
            {loading === true ?
                <View style={{ ...styles.day, alignItems: 'center' }}>
                    <ActivityIndicator color="black" size="large" style={{ marginTop: 10 }} />
                </View> :
                <View style={{ ...styles.login }}>
                    <Text style={{ ...styles.loginText }}>총 알</Text>

                    <View style={{ alignItems: 'center' }}>
                        <TextInput
                            style={{ ...styles.loginInput }} placeholder="아이디" autoCapitalize="none"
                            value={id} onChangeText={(text) => setId(text)} autoCorrect={false} />
                        <TextInput
                            style={{ ...styles.loginInput }} placeholder="비밀번호" autoCapitalize="none" keyboardType="number-pad"
                            autoCorrect={false} secureTextEntry={!showpass ? false : true} value={password}
                            onChangeText={(text) => setPassword(text)}
                            textContentType="password" />

                        <BouncyCheckbox
                            size={20} fillColor="black" unfillColor="#FFFFFF"
                            text="비밀번호 보기" iconStyle={{ borderColor: 'red', marginTop: 5, color: 'black' }}
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
                        </View>
                    }
                </View>
            }
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