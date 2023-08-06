import React, { useEffect, useState, useContext, useCallback } from "react";
import {
    Text, View, StyleSheet, Image
    , ScrollView, Pressable, Button
} from 'react-native';

import { AddSITE } from "../../App";
import { dataContext } from '../../App';
import axios from "axios";
import { BaseURL } from '../../App';


export default function SitesSelectPage({ transData, setSiteOrKey, token }) {
    const { dispatch, user } = useContext(dataContext);
    const [selectSite, setSelectSite] = useState(user.sites?.length ? [...user.sites] : []); // 처음 등록이면 []

    const postSite = async () => {

        if(selectSite.length===0){
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
                        Authorization: token,
                    },
                }
                )
                .then(function (response) {
                    console.log("SitesSelectPage",response.data);
                    setSiteOrKey("keyword"); // 키워드 선택으로
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
            <ScrollView style={{ borderWidth: 2, flex: 1, marginTop: 10 }}>
                <View style={{
                    flexDirection: 'row', flexWrap: "wrap",
                    paddingHorizontal: 16, paddingVertical: 10,
                    justifyContent: "space-between",
                }}>
                    {transData.map((post, index) => {
                        // console.log(post.src)
                        return (
                            <Pressable key={post.id} onPress={
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