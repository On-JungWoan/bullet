// basic
import React, { useContext} from "react";
import {
    Text, View, Image, Pressable, StyleSheet
} from 'react-native';

// install
import { useNavigation } from '@react-navigation/native';
import { FontAwesome } from '@expo/vector-icons';

// from App.js
import { dataContext } from "../../App";

const MainHeader = () => {
    const navigation = useNavigation();
    const { login } = useContext(dataContext);

    return (
        <View style={{flex:1}}>
            <View style={{ ...styles.headContainer }}>

                {login ?
                    <Pressable style={{...styles.image}} onPress={() => { navigation.navigate("Main"); }}>
                        <Image style={{width:'100%', height: '100%', resizeMode : "stretch"}} source={require("../../assets/LOGO.png")} />
                    </Pressable>
                    : <Image style={{...styles.image}} source={require("../../assets/LOGO.png")} />
                }
                {login === true ?
                    <Pressable style={{ ...styles.myPageImage }}
                        onPress={() => { navigation.navigate("MyPage"); }}>
                        <FontAwesome name="user-o" size={27} color="white" />
                    </Pressable>
                    : null
                }
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    headContainer:{
        flex: 1,
        alignItems: 'center',
        flexDirection: 'row',
        borderBottomWidth: 1,

        backgroundColor : "black"
    },
    image: {
        width:'18%',
        height: '40%',
        marginLeft : '5%',
        resizeMode : "stretch"
    },
    myPageImage:{
        position: 'absolute',
        right: '5%',
        marginTop: 5 
    }
});

export default MainHeader;