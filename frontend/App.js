import { StatusBar } from 'expo-status-bar';
import React, { useEffect, useState, useMemo, useCallback } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Font
import { Fontisto } from '@expo/vector-icons';

import {
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity,
} from 'react-native';

import Main from './Component/pages/main';

const LOGIN = 'login';

export default function App() {
  const [login, setLogin] = useState(false);
  const [dark, setDark] = useState('dark');

  useEffect(() => {
    loadLogin();
  }, []);

  const isLogin = useCallback(async () => {
    if (!login) {
      setLogin(true);
    }
    await AsyncStorage.setItem(LOGIN, login);
  }, [login]);

  const loadLogin = async () => {
    const loginInfo = await AsyncStorage.getItem(LOGIN);
    loginInfo !== null ? setToDos(JSON.parse(loginInfo)) : null;
  };

  return (
    <View style={styles.container}>
      <StatusBar style="auto" />

      {login == false ? (
        <View style={{ ...styles.login }}>
          <Text style={{ ...styles.loginText }}>
            총 알
          </Text>

          <View style={{alignItems: 'center'}}>
            <TextInput
              style={{ ...styles.loginInput }}
              placeholder="아이디"></TextInput>
            <TextInput
              style={{ ...styles.loginInput, marginBottom: 20, }}
              placeholder="비밀번호"></TextInput>
          </View>

          <View style={{justifyContent:"center", alignItems:"center", marginBottom: 10,}}>
            <TouchableOpacity style={styles.loginBtn}
              onPress={() => {
                isLogin();
              }}>
              <Text style={{textAlign:"center", color : "white"}}>총알</Text>
            </TouchableOpacity>
          </View>
        </View>

      ) : (

        <Main/>

      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  login: {
    borderWidth: 2,
    borderRadius: 5,
    borderStyle: 'solid',
    backgroundColor: '#0081f1',

    width: '70%',
  },
  loginText: {
    color : "white",

    marginTop: 20,

    textAlign: 'center',
    fontSize: 30,
    fontWeight: 700,
  },
  loginInput: {
    color : "white",

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
    paddingHorizontal : 8,
    paddingVertical : 5,

    color : "white",
    width : "30%",

    borderWidth: 2,
    borderRadius: 5,
    borderStyle: 'solid',

  },
});
