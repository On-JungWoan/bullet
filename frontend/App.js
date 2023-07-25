// state
const initState = {
  login: false,
  user: {
    "name": "",
    "dark": "dark",
  },
}

export const LOGIN = "LOGIN"
export const DARK = "DARK"

// action
const reducer = (state, action) => {
  switch (action.type) {
    case LOGIN:
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
import { NavigationContainer, createNativeStackNavigator } from "@react-navigation/native";

import { registerRootComponent } from 'expo';
registerRootComponent(App);

export const dataContext = createContext({
  login: false,
  dispatch: () => { },
});

import MainPage from './Component/pages/Main';
import LoginPage from './Component/pages/Login';
import SignUp from './Component/pages/SignUp'

const Stack = createNativeStackNavigator();

export default function App() {

  const [state, dispatch] = useReducer(reducer, initState)
  const { login } = state;

  const value = useMemo(() => ({ login, dispatch }), [login])

  return (
    <dataContext.Provider value={value}>
      <View style={{...styles.container}}>
        <StatusBar style="auto" />
        { !login ? <LoginPage /> :
          <NavigationContainer>
            <Stack.Navigator initialRouteName="Main">
              <Stack.Screen name="Main" component={MainPage} />
              <Stack.Screen name="SignUp" component={SignUp} />
            </Stack.Navigator>
          </NavigationContainer>
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
