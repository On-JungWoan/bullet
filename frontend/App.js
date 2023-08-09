export const TOKEN = 'TOKEN'
export const NAME = 'NAME'

// import AsyncStorage from '@react-native-async-storage/async-storage';

// state
const initState = {
  login: false, // true면 로그인
  dark: false, // true먄 다크모드
  user: {
    "name": "",
    "keywords": [], // 키워드
    "sites": [], // 사이트
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
  console.log("State", state);
  switch (action.type) {
    case LOGIN: // 로그인 시 모든 정보를 받아옴
      return {
        ...state,
        login: action.login,
        user: {
          "sites": action.sites,
          "name": action.name,
          "keywords": action.keywords,
        }
      }
    case LOGOUT:
      return {
        ...state,
        login: action.login,
      }
    case AddSITE:
      return {
        ...state,
        user: {
          "sites": action.sites,
          "name": state.user.name,
          "keywords": state.user.keywords,
        }
      }
    case AddKEYWORD:
      return {
        ...state,
        user: {
          "sites": state.user.sites,
          "name": state.user.name,
          "keywords": action.keywords,
        }
      }

    default:
      return state;
  }

}

export const dataContext = createContext({
  login: false,
  dispatch: () => { },
});
/////////////////////////////////////////////////

import React, {
  useMemo, createContext, useReducer
} from 'react';

import { StyleSheet, View } from 'react-native';

// pages
import Login from "./Component/pages/Login.jsx"
import MyPage from "./Component/pages/MyPage.jsx"
import SignUp from './Component/pages/SignUp.jsx'

// component
import MainHeader from "./Component/components/MainHeader.jsx"

// navigator
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

const Stack = createNativeStackNavigator();

export default function App() {

  const [state, dispatch] = useReducer(reducer, initState)
  const { login, user, dark } = state;

  const value = useMemo(() => ({ login, dispatch, user, dark }), [login, user]) //로그인, dispatch, user 정보를 전송

  return (
    <NavigationContainer>
      <dataContext.Provider value={value} style={{flex: 1}}>
        <View style={{ flex: 1 }}>
          <MainHeader />
        </View>
        <View style={{ flex: 9}}>
          <Stack.Navigator initialRouteName="Login">
            <Stack.Screen name="Login" component={Login} options={{ headerShown: false }} />
            <Stack.Screen name="MyPage" component={MyPage} options={{ headerShown: false }} />
            <Stack.Screen name="SignUp" component={SignUp} options={{ headerShown: false }} />
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
