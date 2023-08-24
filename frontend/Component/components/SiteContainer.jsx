// basic
import React, { useEffect, useState, useContext, useCallback } from "react";
import {
    Text, View, StyleSheet, Image, ScrollView, Pressable, KeyboardAvoidingView
} from 'react-native';

// install
import { useNavigation } from "@react-navigation/native";

// from App.js

export default function SitesSelectPage({ transData,  transSite, setTransSite, postSite }) {

    const navigation = useNavigation();

    return (
        <View>
            <ScrollView style={{ ...styles.sitesContainer }} persistentScrollbar={true}>
                <KeyboardAvoidingView behavior={Platform.select({ ios: 'padding', android: undefined })} style={{ ...styles.site }}>
                    {transData.map((post, index) => {
                        return (
                            <Pressable style={{ marginBottom: 5 }} key={post.id} onPress={
                                () => {
                                    if (!transSite.includes(post.site)) {
                                        setTransSite([...transSite, post.site]);
                                    } else {
                                        let deleteSite = transSite;
                                        deleteSite.splice(deleteSite.indexOf(post.site), 1);
                                        setTransSite([...deleteSite]);
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

            <View style={{ ...styles.buttonContainer }}>
                <Pressable style={{ ...styles.button }} onPress={() => { navigation.pop() }}>
                    <Text style={{ color: "white", textAlign: 'center' }}>이전 화면</Text>
                </Pressable>

                <Pressable style={{ ...styles.button }} onPress={() => { postSite() }}>
                    <Text style={{ color: "white", textAlign: 'center' }}>등록하기</Text>
                </Pressable>
            </View>
            <View>
                {transSite?.length ? <Text style={{ fontSize: 20 }}>{`선택 : ${transSite}`}</Text> : null}
            </View>
        </View>
    )

}

const styles = StyleSheet.create({
    sitesContainer: {
        borderWidth: 2,
        marginTop: 10,
    },
    site: {
        flexDirection: 'row',
        flexWrap: "wrap",
        paddingHorizontal: 16,
        paddingVertical: 10,
        justifyContent: "space-between",
    },
    buttonContainer: {
        flex: 1,
        flexDirection: "row",
        backgroundColor: "Red",
        flexWrap: "wrap",
        marginTop: 10,

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
