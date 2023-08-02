import AsyncStorage from '@react-native-async-storage/async-storage'

export const TOKEN = 'TOKEN'

// state
const initState = {
  login: false, // true면 로그인
  dark : false, // true먄 다크모드
  user: {
    "name": "", // 이름
    "keyword" : [], // 키워드
    "site" : [], // 사이트
  },
}

export const LOGIN = "LOGIN"
export const LOGOUT = "LOGOUT"

// action
const reducer = (state, action) => {
  switch (action.type) {
    case LOGIN:
      return {
        ...state,
        login: action.login,
      }
    case LOGOUT:
      return {
        ...state,
        login: action.login,
      }
    default:
      return state;
  }

}

/////////////////////////////////////////////////

import { StatusBar } from 'expo-status-bar';
import React, {
  useEffect, useMemo, useCallback, createContext, useReducer
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
  const { login } = state;

  const value = useMemo(() => ({ login, dispatch }), [login])

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
