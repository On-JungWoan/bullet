// 로컬 저장 상수
export const AccessTOKEN = 'AccessTOKEN'
export const RefreshTOKEN = 'RefreshTOKEN'
export const NAME = 'NAME'

// import AsyncStorage from '@react-native-async-storage/async-storage';

// state
const initState = {
  login: false, // true면 로그인
  user: {
    "name": "",
    "keywords": [], // 키워드
    "newsSites": [], // 사이트
    "uniSites": [], // 사이트
    "workSites": [], // 사이트
  },
}

export const BaseURL = 'http://192.168.0.9:8000/'

// dispatch 상수
export const LOGIN = "LOGIN"
export const LOGOUT = "LOGOUT"
export const AddKEYWORD = "ADDKEYWORD"
export const AddSITE = "AddSITE"
export const TEST = "TEST";

// action
const reducer = (state, action) => {
  console.log("State", state);
  switch (action.type) {
    case LOGIN: // 로그인 시 모든 정보를 받아옴
      return {
        ...state,
        login: action.login,
        user: {
          "keywords": action.keywords,
          "name": action.name,
          "newsSites": action.newsSites,
          "uniSites": action.uniSites,
          "workSites": action.workSites,
        }
      }
    case LOGOUT: // 로그아웃
      return {
        ...state,
        login: action.login,
      }
    case AddSITE: // 뉴스 사이트 추가
      return{
        ...state,
        user: {
          "newsSites": action.newsSites,
          "uniSites": action.uniSites,
          "workSites": action.workSites,
          "name": state.user.name,
          "keywords": state.user.keywords,
        }
      }
    case AddKEYWORD: // 키워드 추가
      return {
        ...state,
        user: {
          "newsSites": state.user.newsSites,
          "uniSites": state.user.uniSites,
          "workSites": state.user.workSites,
          "name": state.user.name,
          "keywords": action.keywords,
        }
      }

    default:
      return state;
  }

}

// Context API
export const dataContext = createContext({
  login: false,
  dispatch: () => { },
});
/////////////////////////////////////////////////

// basic
// import { StatusBar } from "expo-status-bar";
import { StyleSheet, View, StatusBar} from 'react-native';
import React, {
  useMemo, createContext, useReducer
} from 'react';

// navigator
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

// pages
import Login from "./Component/pages/Login.jsx" // 로그인
import SignUp from './Component/pages/SignUp.jsx' // 회원가입

import Main from "./Component/pages/Main.jsx"; // 로그인 후 메인
import Register from "./Component/pages/Register.jsx"; // 키워드 및 사이트 등록 
import KeywordsSelectPage from './Component/pages/Keywords.jsx' // 키워드 등록 
import NewsSite from './Component/pages/NewsSite.jsx' // 뉴스 사이트 선택
import UniSite from './Component/pages/UniSite.jsx' // 대학교 사이트 선택
import WorkSite from './Component/pages/WorkSite.jsx' // 일 사이트 선택

import Alarm from "./Component/pages/Alarm.jsx"; // 알림

import MyPage from "./Component/pages/MyPage.jsx" // 마이페이지

// component
import MainHeader from "./Component/components/MainHeader.jsx"

const Stack = createNativeStackNavigator();

export default function App() {

  const [state, dispatch] = useReducer(reducer, initState)
  const { login, user } = state;

  const value = useMemo(() => (
    { login, dispatch, user }),
     [login, user]) //로그인, dispatch, user 정보를 전송

  return (
    <NavigationContainer>
      <dataContext.Provider value={value} style={{ flex: 1 }}>
        <StatusBar backgroundColor="black" color='white'/>
        <View style={{ flex:1 }}>
          <MainHeader />
        </View>
        <View style={{ flex:10 }}>

          <Stack.Navigator initialRouteName="Login" screenOptions={{ animation: 'none' }}>
            <Stack.Screen name="Login" component={Login} options={{ headerShown: false }} />
            <Stack.Screen name="SignUp" component={SignUp} options={{ headerShown: false }} />
            
            <Stack.Screen name="MyPage" component={MyPage} options={{ headerShown: false }} />
            <Stack.Screen name="Register" component={Register} options={{ headerShown: false }} />
            
            <Stack.Screen name="Main" component={Main} options={{ headerShown: false }} />
            
            <Stack.Screen name="Alarm" component={Alarm} options={{ headerShown: false }} />
            <Stack.Screen name="Keywords" component={KeywordsSelectPage} options={{ headerShown: false }} />
            
            <Stack.Screen name="NewsSite" component={NewsSite} options={{ headerShown: false }} />
            <Stack.Screen name="UniSite" component={UniSite} options={{ headerShown: false }} />
            <Stack.Screen name="WorkSite" component={WorkSite} options={{ headerShown: false }} />
          </Stack.Navigator>

        </View>
      </dataContext.Provider >
    </NavigationContainer>
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
