import React, {useState, useEffect} from "react";
import { Text, View, StyleSheet,Image } from 'react-native';


export default function ShowSite({img, site}){
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

ShowSite;