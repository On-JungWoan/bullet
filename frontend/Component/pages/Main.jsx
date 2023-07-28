import React, { useEffect, useState } from "react";

import {
    StyleSheet,
    Text,
    View,
} from 'react-native';

import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";

const Stack = createNativeStackNavigator();

import MainHeader from "../components/MainHeader";
import BottomTabNavigator from "../components/BottomTabNavigator";

export default function MainPage() {
    return (
        <View style={{ flex: 1, width: '100%' }}>
            <MainHeader />
            <View style={{ flex: 9, width: '100%' }}>
                <NavigationContainer>
                    <Stack.Navigator>
                        <Stack.Screen name="Root" component={BottomTabNavigator} options={{ headerShown: false }} />
                    </Stack.Navigator>
                </NavigationContainer>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({

})