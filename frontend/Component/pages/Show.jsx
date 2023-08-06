import AsyncStorage from '@react-native-async-storage/async-storage';

import React, { useEffect, useState, useContext, useCallback } from "react";
import {
    Text, View, StyleSheet, TextInput, Pressable
} from 'react-native';
import { FontAwesome } from '@expo/vector-icons';

import SitesSelectPage from './Sites';
import KeywordsSelectPage from './Keywords';

import { TOKEN, NAME } from '../../App';
import { dataContext } from '../../App';


export default function Show({ transData, setShow }) {
    const [searchValue, setSearchValue] = useState(''); // 검색 값
    const [siteOrKey, setSiteOrKey] = useState("site");
    const [token, setToken] = useState("");

    const { dispatch, user } = useContext(dataContext);
    const [keywords, setKeywords] = useState(user.keywords?.length ? [...user.keywords] : []);

    // token 저장
    useEffect(() => {
        AsyncStorage.getItem(TOKEN).then(value => setToken(value));
    }, [])


    // 검색 기능
    onChangeSearch = (e) => {
        setSearchValue(e);
    }

    // enter 이벤트
    onSubmitText = ()=>{
        console.log("sjow key", keywords);
        if(searchValue===''){
            return;
        }

        setKeywords([...keywords, searchValue]);
        console.log("show searchValue", searchValue);
        setSearchValue('')
    }

    return (

        <View style={{flex: 1 }}>
            <View style={{ flex: 1 }}>
                <Pressable style={styles.arrow} onPress={() => { siteOrKey === "site" ?setShow(false):setSiteOrKey("site") }}>
                    <FontAwesome name="arrow-circle-left" size={40} color="black" />
                </Pressable>
            </View>
            <View style={{ ...styles.showSite, flex: 7 }}>
                <Text style={{ ...styles.searchText, textAlign: 'center' }}>{siteOrKey === "site" ? "원하는 사이트를 선택하세요" : "원하는 키워드를 선택하세요"}</Text>
                <TextInput placeholder={siteOrKey === "site" ? "사이트를 검색하세요" : "키워드를 검색하세요"} autoFocus autoCapitalize="none" autoCorrect={false}
                    style={{ ...styles.searchInput, marginTop: 10 }} value={searchValue} onChangeText={onChangeSearch}
                    onSubmitEditing={onSubmitText} />

                <View style={{ flex: 1 }}>
                    {siteOrKey === "site" ?
                        <SitesSelectPage transData={transData} setSiteOrKey={setSiteOrKey} token={token} />
                        :
                        <KeywordsSelectPage keywords={keywords} token={token} />
                    }
                </View>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    showSite: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center'
    },
    arrow: {
        position: 'absolute',
        top: 25,
        left: 25,
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
})
