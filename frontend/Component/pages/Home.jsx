import React, { useEffect, useState, memo, useCallback } from "react";
import {
    Text, Image, View, Pressable, ScrollView,
    StyleSheet, TextInput, ActivityIndicator
} from 'react-native';

// import ShowSite from "../components/showSite";
import news from "../../news.json"

import { FontAwesome } from '@expo/vector-icons';

const Home = memo(() => {
    const [searchValue, setSearchValue] = useState(''); // 검색 값
    const [show, setShow] = useState(false); // 다음 페이지로 이동할 것인가?
    const [data, setData] = useState([]); // 다음 페이지에 보여줄 데이터 (공지, 직업 등)
    const [site, setSite] = useState([]); // 선택한 사이트

    // 검색 기능
    onChangeSearch = (e) => {
        setSearchValue(e.target.value);
        // 입력 값에 따라 보여주는 컴포넌트 변화, 나중에 할 것
    }

    // 뉴스 선택
    onPressNews = useCallback(() => {
        console.log("뉴스")
        setData(news);
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

    // onPressSite = useCallback((post) => {
    //     setSite([...site, post.site]);
    // }, [site])


    return (
        <View style={{ ...styles.container }}>

            <Pressable style={styles.arrow} onPress={() => { setShow(false), setSite=([]) }}>
                <FontAwesome name="arrow-circle-left" size={40} color="black" />
            </Pressable>

            {show ? // show가 true면 검색창을 보여줌
                <View style={styles.showSite}>
                    <Text style={{ ...styles.searchText, textAlign: 'center' }}>원하는 사이트를 선택하세요</Text>
                    <TextInput placeholder="사이트를 검색하세요" autoCapitalize="none" autoCorrect={false}
                        style={{...styles.searchInput, marginTop : 10 }} value={searchValue} onChangeText={onChangeSearch} />

                    <ScrollView style={{ borderWidth: 2, flex: 1, marginTop : 10 }}>
                        <View style={{
                            flexDirection: 'row', flexWrap: "wrap",
                            paddingHorizontal: 16,
                            paddingVertical: 10,
                            justifyContent: "space-between",
                        }}>
                            {/* 이미지는 링크, site는 text, post는 선택된 json 데이터 */}
                            {data.map((post, index) => {
                                return (
                                    <Pressable key={post.id} onPress={
                                        ()=>{
                                            setSite([...site, post.site]);
                                            console.log(site);
                                        }
                                    }>
                                        <Image style={{ width: 100, height: 80 }} source={require("../../assets/icon.png")} />
                                        <Text style={{ fontSize: 18,textAlign : 'center'}}>{post.site}</Text>
                                    </Pressable>
                                );
                            })}
                        </View>
                    </ScrollView>
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
                </View>}

                {site?.length? <Text>{`선택 : ${site}`}</Text>:null}
        </View>
    )
})

export default Home;

const styles = StyleSheet.create({
    container: {
        width: '100%',
        height: '100%',
        textAlign: 'center',
        justifyContent: 'center',
        alignItems: 'center',
    },
    arrow: {
        position: "absolute",
        top: 25,
        left: 25,
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
    // 사이트 설정 하는 곳
    showSite: {
        backgroundColor: "red",
        width: '90%',
        height: "60%",
        justifyContent:'center',
        alignItems : 'center'
    },
    searchText: {
        color: 'black',
        fontSize: 30,
        fontWeight: 700,
    },
    searchInput: { 
        textAlign: 'center', 
        fontSize: 20, 
        borderRadius: 10, 
        borderWidth: 1, 
        width: '90%',
    }
});