import React, { useContext, useState, memo } from "react";
import {
    Text,
    View,
    Pressable
} from 'react-native';

import { FontAwesome } from '@expo/vector-icons';

import { dataContext } from "../../App";
import { TEST } from "../../App";

const MainHeader = memo(() => {

    const { dispatch } = useContext(dataContext);

    return (
        <View style={{ flex: 1, width: '100%' }}>
            <View style={{ flex: 1, borderBottomWidth: 1, alignItems: 'center', marginTop:20, flexDirection:'row' }}>
                <Text style={{
                    textAlign: 'left', fontSize: 30, fontWeight: 700,
                    marginHorizontal: 20
                }}>총알
                </Text>
                <Pressable style={{position:'absolute', right:20, marginTop:5}} onPress={()=>{
                    dispatch({type:TEST});
                }}>
                    <FontAwesome name="bars" size={35} color="black" />
                </Pressable>
            </View>
        </View>
    )
})

export default MainHeader;