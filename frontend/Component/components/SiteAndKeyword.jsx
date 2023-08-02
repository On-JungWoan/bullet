import React from "react";
import { Text, View, StyleSheet,Image } from 'react-native';


export default function SiteAndKeyword({img, site}){
    return(
        <View style={styles.imageBox}>
            <Image source={require(img)}/>
            <Text>{site}</Text>
        </View>
    )
}

const styles = StyleSheet.create({
    imageBox : {
        flex:1,
    }
})
