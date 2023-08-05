import AsyncStorage from '@react-native-async-storage/async-storage';

import React, { useEffect, useState, useContext } from "react";
import {
    Text, View, StyleSheet, Image, TextInput
    , ScrollView, Pressable, Button
} from 'react-native';

import { AddSITE, TOKEN } from "../../App";
import { dataContext } from '../../App';
import axios from "axios";

export default function ShowSite({ transData }) {
    const { dispatch, user } = useContext(dataContext);

    const [searchValue, setSearchValue] = useState(''); // 검색 값
    const [selectSite, setSelectSite] = useState([]);
    const [token, setToken] = useState("");

    // token 저장
    AsyncStorage.getItem(TOKEN).then(value => setToken(value))

    // 검색 기능
    onChangeSearch = (e) => {
        setSearchValue(e);
        // 입력 값에 따라 보여주는 컴포넌트 변화, 나중에 할 것
    }

    const postSite = async () => {

        dispatch({
            type: AddSITE,
            sites: selectSite
        });
        const data = {
            sites: selectSite,
        }
        try {
            await axios
                .post('http://172.30.1.40:8000/user/site/create/', data, {
                    headers: {
                        Authorization: token,
                    }
                }
                )
                .then(function (response) {
                    console.log(response.data);
                    // 키워드 선택으로
                })
                .catch(function (error) {
                    alert("에러발생")
                    console.log(error);
                    throw error;
                });
        } catch (error) {
            console.log(error);
            throw error;
        }
    }

    return (

        <View style={styles.showSite}>
            <Text style={{ ...styles.searchText, textAlign: 'center' }}>원하는 사이트를 선택하세요</Text>
            <TextInput placeholder="사이트를 검색하세요" autoCapitalize="none" autoCorrect={false}
                style={{ ...styles.searchInput, marginTop: 10 }} value={searchValue} onChangeText={onChangeSearch} />

            <ScrollView style={{ borderWidth: 2, flex: 1, marginTop: 10 }}>
                <View style={{
                    flexDirection: 'row', flexWrap: "wrap",
                    paddingHorizontal: 16,
                    paddingVertical: 10,
                    justifyContent: "space-between",
                }}>
                    {transData.map((post, index) => {
                        // console.log(post.src)
                        return (
                            <Pressable key={post.id} onPress={
                                () => {
                                    if (!selectSite.includes(post.site)) {
                                        setSelectSite([...selectSite, post.site]);
                                    }
                                }
                            }>
                                <Image style={{ width: 100, height: 80 }} source={post.src} />
                                <Text style={{ fontSize: 18, textAlign: 'center' }}>{post.site}</Text>
                            </Pressable>
                        );
                    })}
                </View>
            </ScrollView>
            <Button title="다음 페이지" onPress={() => {
                postSite();
            }} />
            <View>
                {selectSite?.length ? <Text style={{ fontSize: 20 }}>{`선택 : ${selectSite}`}</Text> : null}
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    showSite: {
        flex: 5,
        justifyContent: 'center',
        alignItems: 'center'
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