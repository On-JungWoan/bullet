// basic
import React, { useEffect, useState, useContext, useCallback } from "react";
import {
    Text, View, StyleSheet, TextInput, Pressable
} from 'react-native';

// install
import { FontAwesome } from '@expo/vector-icons';
import AsyncStorage from '@react-native-async-storage/async-storage';

// from App.js
import { TOKEN, NAME } from '../../App';
import { dataContext } from '../../App';

// component
import SitesSelectPage from "../components/SiteContainer";

export default function Site({ transData, setSite }) {
    const [searchValue, setSearchValue] = useState(''); // 검색 값
    const [token, setToken] = useState("");

    const { user } = useContext(dataContext);
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
    onSubmitText = () => {
        if (searchValue === '') {
            return;
        }

        setKeywords([...keywords, searchValue]);
        setSearchValue('')
    }

    return (

        <View style={{ flex: 1 }}>
            <View style={{ flex: 1 }}>
                <Pressable style={styles.arrow} onPress={() => { setSite(false) }}>
                    <FontAwesome name="arrow-circle-left" size={40} color="black" />
                </Pressable>
            </View>
            <View style={{ ...styles.showSite, flex: 7 }}>
                <Text style={{ ...styles.searchText, textAlign: 'center' }}>원하는 사이트를 선택하세요</Text>
                <TextInput placeholder="사이트를 검색하세요" autoFocus autoCapitalize="none" autoCorrect={false}
                    style={{ ...styles.searchInput, marginTop: 10 }} value={searchValue} onChangeText={onChangeSearch}
                    onSubmitEditing={onSubmitText} />

                <View style={{ flex: 1 }}>
                    <SitesSelectPage transData={transData} token={token} />
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
