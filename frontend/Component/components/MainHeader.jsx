import React, { useEffect, useState, memo } from "react";
import {
    Text,
    View,
    Pressable
} from 'react-native';

import { FontAwesome } from '@expo/vector-icons';

const MainHeader = memo(() => {
    return (
        <View style={{ flex: 1, width: '100%' }}>
            <View style={{ flex: 1, borderBottomWidth: 1, alignItems: 'center', marginTop:20, flexDirection:'row' }}>
                <Text style={{
                    textAlign: 'left', fontSize: 30, fontWeight: 700,
                    marginHorizontal: 20
                }}>총알
                </Text>
                <Pressable style={{position:'absolute', right:20, marginTop:5}} onPress={()=>{console.log("X")}}>
                    <FontAwesome name="bars" size={35} color="black" />
                </Pressable>
            </View>
        </View>
    )
})

export default MainHeader;