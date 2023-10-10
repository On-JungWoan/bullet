// basic
import React,{useCallback, useEffect, useState} from "react";
import {
    Text, View, Pressable, StyleSheet, Image
} from 'react-native';

import * as Notifications from 'expo-notifications';

// install
import { useNavigation } from "@react-navigation/native";
import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from "axios";
import { API_URL } from '@env';
const URL = API_URL

// 상수
import { AccessTOKEN } from '../../App';

export let TOKEN = '';

// 알림
Notifications.setNotificationHandler({
	handleNotification: async () => ({
		shouldShowAlert: true,
		shouldPlaySound: true,
		shouldSetBadge: true,
	}),
});

export default function Main() {
    const navigation = useNavigation();

    const [token, setToken] = useState("");
    const [notiToken, setNotiToken] = useState("")

    useEffect( ()=>{
        AsyncStorage.getItem(AccessTOKEN).then(value => {
            setToken(value)
        });
        getNotiToken();
    },[])

    const getNotiToken = () =>{
        Notifications.getDevicePushTokenAsync().then(value=>{
            setNotiToken(value["data"].slice(value["data"].indexOf('[')+1,value["data"].indexOf(']')));
            // setNotiToken(value["data"]);
        })
    }

    const postAlarmToken = useCallback(async (notiToken) =>{
        console.log("notiToken2",notiToken)
        try {
            await axios
                .post(`${URL}/user/fcm/`,
                {
                    "token":notiToken
                }, {
                    headers: {
                        Authorization: TOKEN,
                    },
                }
                )
                .then(function (response) {
                    // console.log("notiToken response", response.data);
                })
                .catch(function (error) {
                    alert(error)
                    throw error;
                });
        } catch (error) {
            alert(error);
            throw error;
        }
    })

    useEffect(()=>{
        TOKEN = token;
        if(notiToken !==''){
            // postAlarmToken(notiToken);
        }
    },[token,notiToken])

    return (
        <View style={{ ...styles.container }}>
            <View style={{ ...styles.mainContainer }}>
                <Pressable style={{ ...styles.pressContainer, backgroundColor: "black" }} onPress={() => { navigation.navigate("Register");}}>
                    <Image style={{width:"40%", height:"50%", resizeMode : "stretch"}} source={require("../../assets/main/register.png")}/>
                    <Text style={{ ...styles.text, color:"white"}}>
                        등록하기
                    </Text>
                </Pressable>
                <Pressable style={{ ...styles.pressContainer, backgroundColor:"black" }} onPress={() => { navigation.navigate("Alarm");}}>
                <Image style={{width:"30%", height:"40%", resizeMode : "stretch"}} source={require("../../assets/main/alarm.png")}/>
                    <Text  style={{ ...styles.text, color:"white" }}>
                        알림 확인하기
                    </Text>
                </Pressable>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        height: '100%',
        justifyContent: "center",
        alignItems: 'center',

        backgroundColor: "white",
        flex: 1,
    },
    mainContainer: {
        width: '70%',
        height: '60%',
    },
    pressContainer: {
        flex: 1,
        marginVertical: 10,

        justifyContent: 'center',
        alignItems: 'center',
        textAlign: 'center',

        borderRadius: 20,
    },
    text: {
        fontSize: 20,
        marginTop: 20,
    }
})