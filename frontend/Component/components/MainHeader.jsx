import React, { useContext, useState, memo } from "react";
import {
    Text, View, Image, Pressable, StyleSheet
} from 'react-native';

import { FontAwesome } from '@expo/vector-icons';
import { dataContext } from "../../App";

import { useNavigation } from '@react-navigation/native';

const MainHeader = () => {
    const navigation = useNavigation();

    const { login } = useContext(dataContext);

    return (
        <View style={{ flex: 1, width: '100%' }}>
            <View style={{ ...styles.container }}>

                {login ?
                    <Pressable onPress={() => { navigation.navigate("Login"); }}>
                        <Image source={require("../../assets/LOGO.png")} />
                    </Pressable>
                    : <Image style={{...styles.image}} source={require("../../assets/LOGO.png")} />
                }

                {login === true ?
                    <Pressable style={{ ...styles.myPageImage }}
                        onPress={() => { navigation.navigate("MyPage"); }}>
                        <FontAwesome name="user-o" size={24} color="black" />
                    </Pressable>
                    : null
                }
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    container:{
        flex: 1,
        alignItems: 'center',
        flexDirection: 'row',
        marginTop: 20,
        borderBottomWidth: 1,
    },
    image: {
        width:'20%',
        height: '50%',
        resizeMode: "stretch",
    },
    myPageImage:{
        position: 'absolute',
        right: 20,
        marginTop: 5 
    }
});

export default MainHeader;