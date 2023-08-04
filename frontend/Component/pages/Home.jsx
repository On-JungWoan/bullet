import React, { useEffect, useState, memo, useCallback } from "react";
import {
    Text, Image, View, Pressable, StyleSheet
} from 'react-native';

import ShowSite from "./ShowSite";
import { newsData } from "../../news";

import { FontAwesome } from '@expo/vector-icons';


const Home = memo(() => {
    const [show, setShow] = useState(false); // 다음 페이지로 이동할 것인가?
    const [transData, setData] = useState([]); // 다음 페이지에 보여줄 데이터 (공지, 직업 등)

    // 뉴스 선택
    onPressNews = useCallback(() => {
        console.log("뉴스")
        setData(newsData);
        setShow(true);
    }, [])
    // 공지사항 선택
    onPressNotice = useCallback(() => {
        console.log("공지사항")
        setShow(true);
    }, [])
    // 직업 선택
    onPressJob = useCallback(() => {
        console.log("일")
        setShow(true);
    }, [])


    return (
        <View style={{ ...styles.container }}>
            {show ? // show가 true면 검색창을 보여줌
                <View style={{ flex: 1, width:'90%' }}>
                    <View style={{ flex: 1 }}>
                        <Pressable style={styles.arrow} onPress={() => { setShow(false) }}>
                            <FontAwesome name="arrow-circle-left" size={40} color="black" />
                        </Pressable>
                    </View>
                    <View style={{flex:7}}>
                        <ShowSite transData={transData} />
                    </View>
                </View>
                : <View style={styles.moveCompo}>
                    <Pressable style={{ ...styles.press, marginRight: 5 }} onPress={onPressNews}>
                        <Image style={{ width: 60, height: 60 }} source={require('../../assets/icon.png')} />
                        <Text style={{ fontSize: 18 }}>뉴스</Text>
                    </Pressable>
                    <Pressable style={{ ...styles.press, marginRight: 5 }} onPress={onPressNotice}>
                        <Image style={{ width: 60, height: 60 }} source={require('../../assets/icon.png')} />
                        <Text style={{ fontSize: 18 }}>공지사항</Text>
                    </Pressable>
                    <Pressable style={styles.press} onPress={onPressJob}>
                        <Image style={{ width: 60, height: 60 }} source={require('../../assets/icon.png')} />
                        <Text style={{ fontSize: 18 }}>취업</Text>
                    </Pressable>
                </View>
            }


        </View>
    )
})

export default Home;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        width: '100%',
        height: '100%',
        textAlign: 'center',
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor : "white"
    },
    arrow: {
        position : 'absolute',
        top :25,
        left : 25,
    },
    moveCompo: {
        alignItems: 'center',
        flexDirection: 'row',
        flex: 1,
        width: '75%',
    },
    press: {
        height: '20%',
        display: 'flex',
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
});