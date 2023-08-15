// basic
import React, { useEffect, useState, useContext, useCallback } from "react";
import {
    Text, View, StyleSheet, Image, ScrollView, Pressable, KeyboardAvoidingView
} from 'react-native';

// install
import axios from "axios";

// from App.js
import { dataContext } from '../../App';
import { BaseURL } from '../../App';
import { TOKEN } from "../pages/Main";

export default function SitesSelectPage({ transData, setSite }) {
    const { dispatch, user } = useContext(dataContext);
    const [selectSite, setSelectSite] = useState(user.sites?.length ? [...user.sites] : []); // 처음 등록이면 []

    const postSite = async () => {

        if (selectSite.length === 0) {
            alert('선택한 사이트가 없습니다.');
            return;
        }

        dispatch({
            type: AddSITE,
            sites: selectSite
        });
        const data = {
            sites: selectSite,
        }
        try {
            await axios
                .post(`${BaseURL}/user/site/create/`, data, {
                    headers: {
                        Authorization: TOKEN,
                    },
                }
                )
                .then(function (response) {
                    console.log("SitesSelectPage", response.data);
                })
                .catch(function (error) {
                    alert("에러발생")
                    console.log("error", error);
                    throw error;
                });
        } catch (error) {
            console.log("error", error);
            throw error;
        }
    }

    return (
        <View>
            <ScrollView style={{ ...styles.sitesContainer}} persistentScrollbar={true}>
                <KeyboardAvoidingView behavior={Platform.select({ios: 'padding', android: undefined})}  style={{...styles.site }}>
                    {transData.map((post, index) => {
                        return (
                            <Pressable style={{ marginBottom: 5 }} key={post.id} onPress={
                                () => {
                                    if (!selectSite.includes(post.site)) {
                                        setSelectSite([...selectSite, post.site]);
                                    } else {
                                        let deleteSite = selectSite;
                                        deleteSite.splice(deleteSite.indexOf(post.site), 1);
                                        setSelectSite([...deleteSite]);
                                    }
                                }
                            }>
                                <Image style={{ width: 100, height: 80, resizeMode: "stretch", marginBottom: 3 }} source={post.src} />
                                <Text style={{ fontSize: 15, textAlign: 'center' }}>{post.site}</Text>
                            </Pressable>
                        );
                    })}
                </KeyboardAvoidingView>
            </ScrollView>

            <View style={{...styles.buttonContainer}}>
                <Pressable style={{...styles.button}} onPress={() => { setSite(false) }}>
                    <Text style={{color : "white",textAlign: 'center'}}>이전 화면</Text>
                </Pressable>

                <Pressable style={{...styles.button}} onPress={() => {}}>
                    <Text style={{color : "white",textAlign: 'center'}}>등록하기</Text>
                </Pressable>
            </View>
            <View>
                {selectSite?.length ? <Text style={{ fontSize: 20 }}>{`선택 : ${selectSite}`}</Text> : null}
            </View>
        </View>
    )

}

const styles = StyleSheet.create({
    sitesContainer :{
        borderWidth: 2,
        marginTop: 10,
    },
    site:{
        flexDirection: 'row', 
        flexWrap: "wrap",
        paddingHorizontal: 16, 
        paddingVertical: 10,
        justifyContent: "space-between",
    },
    buttonContainer :{
        flex :1,
        flexDirection : "row",
        backgroundColor : "Red",
        flexWrap : "wrap",
        marginTop : 10,
        
    },
    button :{
        flex :1,
        backgroundColor : "black",
        borderWidth:1,
        borderRadius : 20,

        paddingHorizontal : 15,
        paddingVertical :8,
        marginHorizontal : 10,
    }
})
