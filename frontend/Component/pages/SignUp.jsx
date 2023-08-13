// basic
import React, { useEffect, useState, useCallback, useContext } from 'react';
import {
    StyleSheet, Text, View, TextInput, Pressable, ScrollView
} from 'react-native';

// install
import axios from 'axios';
import { useNavigation } from '@react-navigation/native';
import BouncyCheckbox from "react-native-bouncy-checkbox";
import { FontAwesome } from '@expo/vector-icons';

// from App.js
import { BaseURL } from '../../App';
import { dataContext } from '../../App';

// component
import BasicButton from '../components/Button';

export default function SignUp() {
    const [id, setId] = useState('');
    const [password, setPassword] = useState('');
    const [checkPassword, setCheckPassword] = useState('');
    const [showPass, setShowPass] = useState(true);
    const [name, setName] = useState('');

    const navigation = useNavigation();

    // 검사
    const [errorId, setErrorId] = useState('');
    const [errorPassword, setErrorPassword] = useState('');
    const [errorCheckPassword, setErrorCheckPassword] = useState('');

    useEffect(()=>{
        setId('')
        setPassword('')
        setCheckPassword('')
        setShowPass(false);
        setName('')
    },[])

    // ID 형식 확인
    const idForm = (e) => {
        setErrorId('이메일이 올바르지 않습니다.');
        if (e.includes('@')) {
            let be = e.split('@')[0];
            let af = e.split('@')[1];
            if (be === '' || af === '') {
                setErrorId('이메일이 올바르지 않습니다.');
            } else {
                setErrorId('');
            }
        }
        setId(e);
    }

    // 비밀번호 형식 확인
    const passwordForm = (e) => {
        if (e) {
            setErrorPassword('');
        } else {
            setErrorPassword('비밀번호를 입력해주세요');
        }
        setPassword(e)
    }

    // 비밀번호 같은지 확인
    const equalPassword = (e) => {
        if (e === password) {
            setErrorCheckPassword('')
        } else {
            setErrorCheckPassword('비밀번호가 다릅니다.')
        }
        setCheckPassword(e);
    }

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
                        alert("회원가입을 축하드립니다.");
                        navigation.navigate("Login")
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
        <View style={{ ...styles.container }}>
            <ScrollView style={{ ...styles.sighUpContainer }}>
                <View style={{ ...styles.textContainer }}>
                    <Pressable style={{ position: "absolute", left: 10 }} onPress={() => { navigation.navigate("Login") }}>
                        <FontAwesome name="arrow-circle-left" size={40} color="black" />
                    </Pressable>
                    <Text style={{ ...styles.mainText }}>회원가입</Text>
                </View>
                <View style={{ ...styles.inputTextContainer }}>
                    <Text style={{ ...styles.formText }}>이메일</Text>
                    <TextInput
                        style={{ ...styles.inputText }} placeholder="이메일을 입력하세요." autoCapitalize="none" placeholderTextColor="#888"
                        value={id} onChangeText={idForm} autoCorrect={false}
                        keyboardType="email-address" />
                    {errorId !== '' ? <Text style={{ ...styles.errorText }}>{errorId}</Text>
                        : null
                    }

                    <Text style={{ ...styles.formText }}>비밀번호</Text>
                    <TextInput
                        style={{ ...styles.inputText }} placeholder="비밀번호을 입력하세요." autoCapitalize="none" placeholderTextColor="#888"
                        keyboardType="number-pad" autoCorrect={false} secureTextEntry={!showPass ? false : true}
                        value={password} onChangeText={passwordForm}
                        textContentType="password" />
                    {errorPassword !== '' ? <Text style={{ ...styles.errorText }}>{errorPassword}</Text>
                        : null
                    }

                    <Text style={{ ...styles.formText }}>비밀번호 확인</Text>
                    <TextInput
                        style={{ ...styles.inputText }} placeholder="비밀번호을 입력하세요." autoCapitalize="none" placeholderTextColor="#888"
                        keyboardType="number-pad" autoCorrect={false} secureTextEntry={!showPass ? false : true}
                        value={checkPassword} onChangeText={equalPassword}
                        textContentType="password" />
                    {errorCheckPassword !== '' ? <Text style={{ ...styles.errorText }}>{errorCheckPassword}</Text>
                        : null
                    }

                    <BouncyCheckbox style={{ paddingLeft: 10, marginBottom: 20, }} textStyle={{ textDecorationLine: "none" }}
                        size={20} fillColor="black" unfillColor="#FFFFFF"
                        text="비밀번호 보기" iconStyle={{ borderColor: 'red', marginTop: 5, color: 'black' }}
                        onPress={() => setShowPass(!showPass)}
                    />

                    <Text style={{ ...styles.formText }}>이름</Text>
                    <TextInput
                        style={{ ...styles.inputText, marginBottom : 50 }} placeholder="이름을 입력하세요." autoCapitalize="none" placeholderTextColor="#888"
                        value={name} onChangeText={(text) => setName(text)} autoCorrect={false} />
                </View>
                <View style={{ ...styles.buttonContainer }}>
                    <BasicButton text="제출하기" bg="black" marginBottom={0}
                        textColor="white" onPressEvent={checkSignUp} />
                </View>
            </ScrollView>
        </View>

    );
}
const styles = StyleSheet.create({
    container: {
        justifyContent: "center",
        alignItems: 'center',

        backgroundColor: "white",
        flex: 1,
    },
    sighUpContainer: {
        width: '70%',
        height : '70%',

        marginTop:'20%',
    },
    textContainer: {
        flex: 1,
        flexDirection: "row",
        width: '100%',

        justifyContent: "center",
        alignItems: 'center',
        marginBottom : 20,
    },
    mainText: {
        fontSize: 30,
    },
    inputTextContainer: {
        flex: 4,
        width: '100%',
    },
    formText: {
        fontSize: 18,
        marginBottom: 5,
        paddingHorizontal: 10,
    },
    errorText: {
        marginBottom: 10,
        color: 'red',
        paddingHorizontal: 10,
    },
    inputText: {
        width: '100%',
        borderWidth: 1,
        borderRadius: 10,
        borderColor: '#888',

        paddingHorizontal: 10,
        paddingVertical: 10,

        fontSize: 20,
        color: '#888'
    },
    buttonContainer: {
        flex: 1,
        width:'100%',
    },
})