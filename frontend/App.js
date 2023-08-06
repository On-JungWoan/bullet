export const TOKEN = 'TOKEN'
export const NAME = 'NAME'

// import AsyncStorage from '@react-native-async-storage/async-storage';

// state
const initState = {
  login: false, // true면 로그인
  dark : false, // true먄 다크모드
  user: {
    "name": "",
    "keywords" : [], // 키워드
    "sites" : [], // 사이트
  },
}

export const BaseURL = 'http://192.168.0.9:8000'

export const LOGIN = "LOGIN"
export const LOGOUT = "LOGOUT"
export const AddKEYWORD = "ADDKEYWORD"
export const AddSITE = "ADDSITE"
export const TEST = "TEST";

// action
const reducer = (state, action) => {
  console.log("State",state);
  switch (action.type) {
    case LOGIN: // 로그인 시 모든 정보를 받아옴
      return {
        ...state,
        login: action.login,
        user : {
          "sites" : action.sites,
          "name" : action.name,
          "keywords" : action.keywords,
        }
      }
    case LOGOUT:
      return {
        ...state,
        login: action.login,
      }
    case AddSITE :
      return {
        ...state,
        user : {
          "sites" : action.sites,
          "name" : state.user.name,
          "keywords" : state.user.keywords,
        }
      } 
    case AddKEYWORD:
      return {
        ...state,
        user : {
          "sites" : state.user.sites,
          "name" : state.user.name,
          "keywords" : action.keywords,
        }
      }
    case TEST :
      return state
    
    default:
      return state;
  }

}

/////////////////////////////////////////////////

import { StatusBar } from 'expo-status-bar';
import React, {
  useMemo, createContext, useReducer
} from 'react';

import { StyleSheet, View } from 'react-native';


export const dataContext = createContext({
  login: false,
  dispatch: () => { },
});

import MainPage from './Component/pages/Main';
import LoginPage from './Component/pages/Login';

export default function App() {

  const [state, dispatch] = useReducer(reducer, initState)
  const { login, user } = state;

  const value = useMemo(() => ({ login, dispatch, user }), [login, user]) //로그인, dispatch, user 정보를 전송

  return (
    <dataContext.Provider value={value}>
      <View style={{ ...styles.container }}>
        <StatusBar style="auto" />
        {!login ? <LoginPage />
          : <MainPage />
        }
      </View>
    </dataContext.Provider >
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
