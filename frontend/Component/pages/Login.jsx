import React, { useEffect, useState, useCallback, useContext } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';

import {
    StyleSheet, Text, View, ActivityIndicator,
    TextInput, Pressable,
} from 'react-native';
import axios from 'axios';
import BouncyCheckbox from "react-native-bouncy-checkbox";
import { useNavigation } from '@react-navigation/native';

import { TOKEN } from '../../App';
import { NAME } from '../../App';
import { dataContext } from '../../App';
import { LOGIN } from '../../App';
import { BaseURL } from '../../App';

import BasicButton from '../components/Button';

export default function Login() {
    const { dispatch, dark } = useContext(dataContext);
    const navigation = useNavigation();

    const [login, setLogin] = useState(false);
    const [id, setId] = useState('');
    const [password, setPassword] = useState('');
    const [name, setName] = useState('');
    const [showPass, setShowPass] = useState(true);
    const [loading, setLoading] = useState(false); // true로 변경

    const [sites, setSites] = useState([]);
    const [keywords, setKeywords] = useState([]);


    // // 초기 로그인 확인
    // useEffect(() => {
    //     console.log(" 초기 로그인 확인")
    //     AsyncStorage.getItem(TOKEN)
    //         .then(value => {
    //             if (value) { // 자동 로그인
    //                 token = value;
    //                 console.log("token", token)

    //                 getSite();
    //                 getKeyword();

    //                 // setLogin(true);
    //             } else {
    //                 setLoading(false);
    //             }
    //         })
    // }, [])

    // // 자동 로그인시 등록 키워드 가져오기
    // const getKeyword = useCallback(async () => {
    //     console.log("getKeyword");
    //     try {
    //         await axios.get(`${BaseURL}/user/keyword/`, {
    //             headers: {
    //                 Authorization: token,
    //             }
    //         })
    //             .then((response) => {
    //                 console.log("getKeyword", response.data);
    //                 setKeywords(response.data)
    //             })
    //     } catch (error) {
    //         console.log(error);
    //         throw error;
    //     }
    // }, [keywords]);

    // // 자동 로그인시 등록 사이트 가져오기
    // const getSite = useCallback(async () => {
    //     console.log("getSite");
    //     try {
    //         await axios.get(`${BaseURL}/user/site/`, {
    //             headers: {
    //                 Authorization: token,
    //             }
    //         })
    //             .then((response) => {
    //                 console.log("getSites", response.data);
    //                 setSites(response.data);
    //             })
    //     } catch (error) {
    //         console.log(error);
    //         throw error;
    //     }
    // }, [sites]);

    // useEffect(() => {
    //     console.log("user정보 dispatch");

    //     dispatch({
    //         type: LOGIN,
    //         login: login,
    //         sites: sites,
    //         name: AsyncStorage.getItem(NAME),
    //         keywords: keywords,
    //     });
    // }, [login, sites, keywords]);

    // 로그인
    const checkLogin = async () => {
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
        <View style={{ ...styles.container }}>
            {loading ?
                <View style={{ ...styles.day, alignItems: 'center' }}>
                    <ActivityIndicator color="black" size="large" style={{ marginTop: 10 }} />
                </View>
                :
                <View style={{ ...styles.loginContainer }}>
                    <Text style={{ ...styles.mainText, color: dark === true ? "white" : "black" }}>로그인</Text>

                    <View style={{
                        ...styles.inputTextContainer,
                        color: dark === true ? "white" : "black",
                        // backgroundColor:dark===true ? "black" : "white",
                    }}>
                        <TextInput
                            style={{ ...styles.inputText }} placeholder="이메일" autoCapitalize="none" placeholderTextColor="#888"
                            value={id} onChangeText={(text) => setId(text)} autoCorrect={false} />
                        <TextInput
                            style={{ ...styles.inputText }} placeholder="비밀번호" autoCapitalize="none" placeholderTextColor="#888"
                            keyboardType="number-pad" autoCorrect={false} secureTextEntry={!showPass ? false : true}
                            value={password} onChangeText={(text) => setPassword(text)}
                            textContentType="password" />

                        <BouncyCheckbox style={{ paddingLeft: 10 }}
                            size={20} fillColor="black" unfillColor="#FFFFFF"
                            text="비밀번호 보기" iconStyle={{ borderColor: 'red', marginTop: 5, color: 'black' }}
                            onPress={() => setPassword(!showPass)}
                        />
                    </View>

                    <View style={{ ...styles.buttonContainer }}>
                        <BasicButton text="로그인" bg={dark === true ? "white" : "black"} marginBottom={20}
                            textColor={dark === true ? "black" : "white"} onPressEvent={checkLogin} />
                        <BasicButton text="회원가입하기" bg={dark === true ? "black" : "white"}
                            textColor={dark === true ? "white" : "black"} onPressEvent={() => { navigation.navigate('SignUp') }} />
                    </View>

                    <View style={{ flex: 0.2, marginBottom: 10 }}>
                        <Pressable>
                            <Text style={{ fontSize: 20, color: '#888' }}>
                                비밀번호 찾기
                            </Text>
                        </Pressable>
                    </View>

                    <View style={{ ...styles.socialLoginContainer }}>
                        <Pressable style={{ ...styles.socialLogin, backgroundColor: "yellow" }}>
                            <Text>카카오</Text>
                        </Pressable>
                        <Pressable style={{ ...styles.socialLogin, backgroundColor: "green" }}>
                            <Text>네이버</Text>
                        </Pressable>
                        <Pressable style={{ ...styles.socialLogin, backgroundColor: "blue" }}>
                            <Text>구글</Text>
                        </Pressable>
                    </View>
                </View>
            }
        </View>

    );
}

const styles = StyleSheet.create({
    container: {
        height: '100%',
        justifyContent: "center",
        alignItems: 'center',

    },
    loginContainer: {
        width: '70%',
        height: '70%',

        justifyContent: "center",
        alignItems: 'center',
    },
    mainText: {
        flex: 0.5,
        fontSize: 30,
    },
    inputTextContainer: {
        flex: 1,
        width: '100%',
    },
    inputText: {
        width: '100%',
        borderBottomWidth: 1,
        borderColor: '#888',

        marginBottom: 20,
        fontSize: 20,
        paddingHorizontal: 10,

        color: '#888'
    },
    buttonContainer: {
        flex: 1,
        width: '100%',
    },
    socialLoginContainer: {
        flex: 0.8,
        width: '100%',
        flexDirection: "row"
    },
    socialLogin: {
        flex: 1,
        alignItems: "center",
        justifyContent: 'center'
    }
});