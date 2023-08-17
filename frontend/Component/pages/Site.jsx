// basic
import React, { useEffect, useState, useContext, useCallback } from "react";
import {
    Text, View, StyleSheet, TextInput, KeyboardAvoidingView
} from 'react-native';

// install

// from App.js
import { dataContext } from '../../App';

// component
import SitesSelectPage from "../components/SiteContainer";

export default function Site({ transData, setSite, transSite }) {
    const { user } = useContext(dataContext);

    const [searchValue, setSearchValue] = useState(''); // 검색 값
    const [keywords, setKeywords] = useState(user.keywords?.length ? [...user.keywords] : []);


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
            <View style={{ ...styles.headContainer }}>
                <Text style={{ ...styles.searchText }}>원하는 사이트를 선택하세요</Text>

                <TextInput placeholder="사이트를 검색하세요" autoCapitalize="none" autoCorrect={false}
                    style={{ ...styles.searchInput }} value={searchValue} onChangeText={onChangeSearch}
                    onSubmitEditing={onSubmitText} />
            </View>
            <View style={{ ...styles.showSite }}>
                <SitesSelectPage transData={transData} setSite={setSite} transSite={transSite} />
            </View>
            <View style={{ flex: 1 }}>

            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    headContainer: {
        flex: 1.5,
        justifyContent: 'center',
        alignItems: 'center',

        marginTop: "15%",
    },
    showSite: {
        flex: 7,
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
    }
})
