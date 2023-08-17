// basic
import React, { useState, memo, useCallback, useContext } from "react";
import {
    Text, Image, View, Pressable, StyleSheet
} from 'react-native';

// install
import { useNavigation } from "@react-navigation/native";
import axios from "axios";

// from App.js
import { dataContext } from "../../App";

// data
import Site from "./Site";
import { newsData } from "../../news";
import { universityData } from "../../university";

const Register = memo(() => {
    const navigation = useNavigation();
    const { user, dispatch } = useContext(dataContext);

    const [site, setSite] = useState(false); // 사이트 등록 page로
    const [transData, setData] = useState([]); // 다음 페이지에 보여줄 데이터 (공지, 직업 등)

    const [newsSites, setNewsSites] = useState(user.newsSites?.length ? [...user.newsSites] : []);
    const [uniSites, setUniSites] = useState(user.uniSites?.length ? [...user.uniSites] : []);
    const [workSites, setWorkSites] = useState(user.workSites?.length ? [...user.workSites] : []);

    const [transSite, setTransSite] = useState([]);

    // 뉴스 선택
    onPressNews = useCallback(() => {
        console.log("뉴스")
        setData(newsData);
        setTransSite(newsSites);
        setSite(true);
    }, [])

    // 공지사항 선택
    onPressNotice = useCallback(() => {
        console.log("대학교")
        setData(universityData);
        setTransSite(uniSites);
        setSite(true);
    }, [])

    // 직업 선택
    onPressJob = useCallback(() => {
        console.log("일")

        setTransSite(workSites);
        setSite(true);
    }, [])

    // 키워드 등록
    onPressKeyword = useCallback(() => {
        console.log("키워드")
        navigation.navigate('Keywords');
    }, [])


    return (
        <View style={{ ...styles.container }}>
            {site ? // show가 true면 검색창을 보여줌
                <View style={{ flex: 1, width: '90%' }}>
                    <Site transData={transData} setSite={setSite} transSite={transSite} />
                </View>
                : <View style={styles.moveCompo}>
                    <Pressable style={{ ...styles.press }} onPress={onPressNews}>
                        <Image style={{ ...styles.image }} source={require('../../assets/icon.png')} />
                        <Text style={{ fontSize: 20, fontWeight: "bold", color: "white" }}>뉴스 사이트 선택</Text>
                    </Pressable>

                    <Pressable style={{ ...styles.press }} onPress={onPressNotice}>
                        <Image style={{ ...styles.image }} source={require('../../assets/icon.png')} />
                        <Text style={{ fontSize: 20, fontWeight: "bold", color: "white" }}>대학교 사이트 선택</Text>
                    </Pressable>

                    <Pressable style={{ ...styles.press }} onPress={onPressJob}>
                        <Image style={{ ...styles.image }} source={require('../../assets/icon.png')} />
                        <Text style={{ fontSize: 20, fontWeight: "bold", color: "white" }}>취업 사이트 선택</Text>
                    </Pressable>

                    <Pressable style={{ ...styles.press }} onPress={onPressKeyword}>
                        <Image style={{ ...styles.image }} source={require('../../assets/icon.png')} />
                        <Text style={{ fontSize: 20, fontWeight: "bold", color: "white" }}>키워드 등록</Text>
                    </Pressable>
                </View>
            }
        </View>
    )
})

export default Register;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        width: '100%',
        height: '100%',

        textAlign: 'center',
        justifyContent: 'center',
        alignItems: 'center',

        backgroundColor: "white",
    },
    moveCompo: {
        width: '75%',
        height: '60%',
    },
    press: {
        flex: 1,
        flexDirection: "row",
        justifyContent: 'center',
        alignItems: 'center',

        backgroundColor: 'black',

        marginBottom: 20,

        borderRadius: 20,
    },
    image: {
        width: 60,
        height: 60,
        marginRight: 15,
    }
});