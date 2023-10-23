// basic
import React, { useEffect, useState, useContext, useCallback } from "react";
import {
    Text, View, TextInput, Pressable, StyleSheet
} from 'react-native';

// install
import axios from "axios";
import { useNavigation, useRoute } from "@react-navigation/native";
import { API_URL } from '@env';
const URL = API_URL

// from App.js
import { AddKEYWORD } from "../../App";
import { dataContext } from '../../App';
import { TOKEN } from "./Main";

export default function KeywordsSelectPage() {
    const navigation = useNavigation();
    const route = useRoute("Keywords");

    const { dispatch, user } = useContext(dataContext);

    const [searchValue, setSearchValue] = useState(''); // 검색 값
    const [keywords, setKeywords] = useState([]);
    const [category, setCategory] = useState("")

    useEffect(()=>{
        setCategory(route.params?.category)
        checkCategory(route.params?.category);
    },[])

    useEffect(()=>{
        dispatchKeyword(category);
    },[keywords])

    const checkCategory = useCallback((text)=>{
        console.log("checkCategory",text);
        if(text === "news"){
            setKeywords(user.newsKeywords?.length ? [...user.newsKeywords] : [])
        }else if(text==="announce"){
            setKeywords(user.uniKeywords?.length ? [...user.uniKeywords] : [])
        }else if(text==="job"){
            setKeywords(user.workKeywords?.length ? [...user.workKeywords] : [])
        }
    },[])


    // 검색 기능
    onChangeSearch = (e) => {
        setSearchValue(e);
    }

    // enter 이벤트
    onSubmitText = () => {
        if (searchValue === '') {
            return;
        }

        setKeywords([...keywords, searchValue]);
        setSearchValue('');
    }

    const dispatchKeyword = (text)=>{
        if(text === "news"){
            dispatch({
                type: AddKEYWORD,
                newsKeywords:keywords,
                uniKeywords:user.uniKeywords,
                workKeywords:user.workKeywords,
            })
        }else if(text==="job"){
            dispatch({
                type: AddKEYWORD,
                newsKeywords:user.newsKeywords,
                uniKeywords:user.uniKeywords,
                workKeywords:keywords,
            })
        }else if(text==="announce"){
            dispatch({
                type: AddKEYWORD,
                newsKeywords:user.newsKeywords,
                uniKeywords:keywords,
                workKeywords:user.workKeywords,
            })
        }

    }

    const postKeyword = async () => {
        if (keywords?.length === 0) {
            alert('선택한 단어가 없습니다.');
            return;
        }
        
        const data = {
            category : category,
            keywords: keywords,
        }

        console.log(data);

        try {
            await axios
                .post(`${URL}/user/keyword/create/`, data, {
                    headers: {
                        Authorization: TOKEN,
                    },
                }
                )
                .then(function (response) {
                    // console.log("keyword", response.data);
                    navigation.navigate('Register');
                })
                .catch(function (error) {
                    alert("에러발생")
                    console.log("error", error);
                    throw error;
                });
        } catch (error) {
            alert(error);
            throw error;
        }
    }

    return (

        <View style={{ ...styles.container }}>
            <View style={{ flex: 1, width: '75%' }}>
                <View style={{ ...styles.headContainer }}>
                    <Text style={{ ...styles.searchText }}>원하는 키워드를 입력하세요</Text>

                    <TextInput placeholder="키워드를 입력하세요" autoCapitalize="none" autoCorrect={false}
                        style={{ ...styles.searchInput }} value={searchValue} onChangeText={onChangeSearch}
                        onSubmitEditing={onSubmitText}/>
                </View>

                <View>
                    <Text style={{textAlign:"center", fontSize: 20}}>키워드</Text>
                </View>

                <View style={{ ...styles.showKeywords, backgroundColor : "Red" }}>
                    <View style={{ flexDirection: "row" , flexWrap:"wrap", justifyContent: 'center', alignItems: 'center',}}>
                        {keywords?.map((keyword, index) => {
                            return (
                                <View style={{ ...styles.keyword }} key={keyword}>
                                    <Text style={{ fontSize: 20, marginRight: 10 }}>{keyword}</Text>
                                    <Pressable key={keyword} onPress={() => {
                                        let deleteKeywords = keywords;
                                        deleteKeywords.splice(deleteKeywords.indexOf(keyword), 1);
                                        setKeywords([...deleteKeywords]);
                                    }} >
                                        <Text style={{ fontSize: 20 }}>x</Text>

                                    </Pressable>
                                </View>
                            )
                        })}
                    </View>
                </View>

                <View style={{ ...styles.buttonContainer }}>
                    <Pressable style={{ ...styles.button }} onPress={() => { navigation.pop(); }}>
                        <Text style={{ color: "white", textAlign: 'center' }}>이전 화면</Text>
                    </Pressable>

                    <Pressable style={{ ...styles.button }} onPress={() => { postKeyword() }}>
                        <Text style={{ color: "white", textAlign: 'center' }}>등록하기</Text>
                    </Pressable>
                </View>
                <View style={{ flex: 1 }}>

                </View>
            </View>
        </View >
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    headContainer: {
        flex: 1,
        justifyContent: "center",
        alignItems: 'center',

        marginTop: "20%",
        marginBottom: 20,

        borderBottomWidth: 1,
        borderStyle: 'dashed'
    },
    showKeywords: {
        flex: 2,
        justifyContent: 'center',
        alignItems: 'center',

        borderBottomWidth: 1,
        borderStyle: 'dashed'

    },
    arrow: {
        position: 'absolute',
        top: 25,
        left: 25,
    },
    searchText: {
        color: 'black',
        fontSize: 20,
        fontWeight: 700,
        textAlign: 'center',
    },
    searchInput: {
        textAlign: 'center',
        fontSize: 20,

        borderRadius: 10,
        borderWidth: 1,

        width: '80%',
        marginTop: 10
    },
    keyword: {
        borderWidth: 1, 
        borderRadius: 10, 

        flexDirection: "row", 

        marginHorizontal: 5,
        marginBottom : 5,

        paddingHorizontal: 8, 
        paddingVertical: 3,
    },
    buttonContainer: {
        flex: 1,
        flexDirection: "row",
        flexWrap: "wrap",

        marginTop: 20,

    },
    button: {
        flex: 1,

        backgroundColor: "black",
        borderWidth: 1,
        borderRadius: 20,

        paddingHorizontal: 15,
        paddingVertical: 8,
        marginHorizontal: 10,
    }
})
