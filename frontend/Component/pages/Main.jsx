// basic
import React,{useEffect, useState} from "react";
import {
    Text, View, Pressable, StyleSheet, Image
} from 'react-native';

// install
import { useNavigation } from "@react-navigation/native";
import AsyncStorage from '@react-native-async-storage/async-storage';

// 상수
import { AccessTOKEN } from '../../App';


export let TOKEN = '';

export default function Main() {
    const navigation = useNavigation();

    const [token, setToken] = useState("");

    useEffect(()=>{
        AsyncStorage.getItem(AccessTOKEN).then(value => {
            setToken(value)
        });
    },[])

    useEffect(()=>{
        TOKEN = token;
        // console.log("mainToken",TOKEN);
    },[token])

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