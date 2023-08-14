// basic
import React, { useEffect, useState, useCallback, useContext } from 'react';
import {
    StyleSheet, Text, View, ActivityIndicator,
    TextInput, Pressable, ScrollView, Image
} from 'react-native';

// install
import AsyncStorage from '@react-native-async-storage/async-storage';
import BouncyCheckbox from "react-native-bouncy-checkbox";
import axios from 'axios';
import { useNavigation } from '@react-navigation/native';

// from App.js
import { AccessTOKEN , RefreshTOKEN, NAME } from '../../App';
import { dataContext } from '../../App';
import { LOGIN } from '../../App';
import { BaseURL } from '../../App';

// component
import BasicButton from '../components/Button';

export default function Login() {
    const { dispatch } = useContext(dataContext);
    const navigation = useNavigation();

    const [login, setLogin] = useState(false);
    const [id, setId] = useState('');
    const [password, setPassword] = useState('');
    const [showPass, setShowPass] = useState(true);
    const [loading, setLoading] = useState(false); // true로 변경

    const [sites, setSites] = useState([]);
    const [keywords, setKeywords] = useState([]);


    // 로딩 창을 뛰우고 token이 있으면 자동 로그인 없으면 로그인 화면으로
    useEffect(() => {
        console.log(" 초기 로그인 확인")
        // setLogin(true);
        AsyncStorage.getItem(AccessTOKEN)
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

    // 자동 로그인시 등록 키워드 가져오기
    const getKeyword = useCallback(async () => {
        // console.log("getKeyword");
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
    }, []);

    // 자동 로그인시 등록 사이트 가져오기
    const getSite = useCallback(async () => {
        // console.log("getSite");
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
    }, []);

    // login===true면 메인화면으로
    useEffect(() => {
        console.log("user정보 dispatch");

        dispatch({
            type: LOGIN,
            login :login,
            sites: sites,
            name: AsyncStorage.getItem(NAME),
            keywords: keywords,
        });
        if(login === true){
            navigation.navigate('Main')
        }
    }, [login]);

    // 로그인
    const checkLogin = async () => {
        console.log("login");
        const data = {
            email: id,
            password: password
        }
        await axios
            .post(`${BaseURL}/user/login/`, data)
            .then(function (response) {
                console.log("checkLogin", response.data)
                AsyncStorage.setItem(AccessTOKEN, response.headers.authorization); // AccessTOKEN 저장
                AsyncStorage.setItem(RefreshTOKEN, response.headers["refresh-token"]); // RefreshTOKEN 저장
                AsyncStorage.setItem(NAME, response.data.username); // 이름은 로컬에 저장
                setSites(response.data.sites?.length !== 0 ? [...response.data.sites] : []) // 저장한 사이트
                setKeywords(response.data.keywords?.length !== 0 ? [...response.data.keywords] : []) // 저장한 키워드

                setLogin(true);
            })
            .catch(function (error) {
                alert("아이디 또는 비밀번호가 틀렸습니다.");
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
                <ScrollView style={{ ...styles.loginContainer }}>
                    <View style={{ ...styles.textContainer }}>
                        <Text style={{ ...styles.mainText, color: "black" }}>로그인</Text>
                    </View>

                    <View style={{
                        ...styles.inputTextContainer,
                        color:"black",
                        backgroundColor:"white",
                    }}>
                        <TextInput
                            style={{ ...styles.inputText }} placeholder="이메일" autoCapitalize="none" placeholderTextColor="#888"
                            value={id} onChangeText={(text) => setId(text)} autoCorrect={false}
                            keyboardType="email-address" />
                        <TextInput
                            style={{ ...styles.inputText }} placeholder="비밀번호" autoCapitalize="none" placeholderTextColor="#888"
                            autoCorrect={false} secureTextEntry={!showPass ? false : true}
                            value={password} onChangeText={(text) => setPassword(text)}
                            textContentType="password" />

                        <BouncyCheckbox style={{ paddingLeft: 10 }} textStyle={{ textDecorationLine: "none" }}
                            size={20} fillColor="black" unfillColor="#FFFFFF"
                            text="비밀번호 보기" iconStyle={{ borderColor: 'red', marginTop: 5, color: 'black' }}
                            onPress={() => setShowPass(!showPass)}
                        />
                    </View>

                    <View style={{ ...styles.buttonContainer }}>
                        <BasicButton text="로그인" bg="black" marginBottom={20}
                            textColor="white" onPressEvent={checkLogin} />
                        <BasicButton text="회원가입" bg="white"
                            textColor="black" onPressEvent={() => { navigation.navigate('SignUp') }} />
                    </View>

                    <View style={{ ...styles.findContainer }}>
                        <Pressable>
                            <Text style={{ fontSize: 10, color: '#888' }}>
                                비밀번호 찾기
                            </Text>
                        </Pressable>
                    </View>

                    <View style={{ ...styles.socialLoginContainer }}>
                        <Pressable style={{ ...styles.socialLogin}}>
                            <Image style={{...styles.img}} source={require('../../assets/social/kakao.png')} />
                            <Text>카카오</Text>
                        </Pressable>
                        <Pressable style={{ ...styles.socialLogin}}>
                            <Image style={{...styles.img}} source={require('../../assets/social/naver.png')} />
                            <Text>네이버</Text>
                        </Pressable>
                        <Pressable style={{ ...styles.socialLogin}}>
                            <Image style={{...styles.img}} source={require('../../assets/social/google.png')} />
                            <Text>구글</Text>
                        </Pressable>
                    </View>
                </ScrollView>
            }
        </View>

    );
}

const styles = StyleSheet.create({
    container: {
        height: '100%',
        justifyContent: "center",
        alignItems: 'center',

        backgroundColor: "white",
        flex: 1,
    },
    loginContainer: {
        width: '70%',
        height: '70%',

        marginTop: '30%',
    },
    textContainer: {
        flex: 0.5,
        width: '100%',

        justifyContent: "center",
        alignItems: 'center',
        marginBottom: 20,
    },
    mainText: {
        fontSize: 30,
    },
    inputTextContainer: {
        flex: 1,
        width: '100%',
        marginBottom: 20,
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
    findContainer: {
        flex: 0.2,
        alignItems: "center",
        justifyContent: 'center',
        marginBottom: 20,
    },
    buttonContainer: {
        flex: 1,
        width: '100%',
        marginBottom: 20,
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
    },
    img:{
    }
});