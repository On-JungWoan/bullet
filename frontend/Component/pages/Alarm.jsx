// basic
import React, { useEffect, useState, memo, useCallback } from "react";
import {
    Text, View, Pressable, StyleSheet
} from 'react-native';

// install
import axios from 'axios';

// from App.js
import { dataContext } from '../../App';
import { BaseURL } from '../../App';
import { TOKEN } from "./Main";

const Alarm = memo(() => {

    const getAlarm = useCallback(async () => {
        try {
            console.log("TOKEN", TOKEN)
            await axios.get(`${BaseURL}/post/user/`, {
                headers: {
                    Authorization: TOKEN,
                }
            })
                .then((response) => {
                    console.log("Al", response.data);
                })
        } catch (error) {
            console.log(error);
            throw error;
        }
    }, [])

    useEffect(() => {
        getAlarm();
    }, [])


    return (
        <View style={{ ...styles.container }}>
            <Text>알람</Text>

        </View>
    )
})

export default Alarm;

const styles = StyleSheet.create({
    container: {
        backgroundColor: "white",
        flex: 1,
    }
})