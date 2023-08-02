import React, { useCallback, useEffect, useState } from "react";
import {
    Text, View, StyleSheet, Image, TextInput
    , ScrollView, Pressable, Button
} from 'react-native';


export default function ShowSite({ data, getSitesFromChildren, site }) {
    const [searchValue, setSearchValue] = useState(''); // 검색 값
    const [selectSite, setSelectSite] = useState([]);


    useEffect(() => {
        getSitesFromChildren(selectSite);
    } ,[selectSite])
    
    // 검색 기능
    onChangeSearch =(e) => {
        setSearchValue(e);
        // 입력 값에 따라 보여주는 컴포넌트 변화, 나중에 할 것
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
                        {/* 이미지는 링크, site는 text, post는 선택된 json 데이터 */}
                        {data.map((post, index) => {
                            return (
                                <Pressable key={post.id} onPress={
                                    () => {
                                        setSelectSite([...selectSite, post.site])
                                    }
                                }>
                                    <Image style={{ width: 100, height: 80 }} source={require("../../assets/icon.png")} />
                                    <Text style={{ fontSize: 18, textAlign: 'center' }}>{post.site}</Text>
                                </Pressable>
                            );
                        })}
                    </View>
                </ScrollView>
                <Button title="다음 페이지" onPress={()=>{console.log("키워드 선택으로")}}/>
            </View>
    )
}

const styles = StyleSheet.create({
    showSite: {
        flex:5,
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
