// basic
import React, { useEffect, useState, memo, useCallback } from "react";
import {
  Text,
  View,
  Pressable,
  StyleSheet,
  Dimensions,
  ScrollView,
} from "react-native";

// install
import axios from "axios";

// from App.js
import { dataContext } from "../../App";
import { BaseURL } from "../../App";
import { TOKEN } from "./Main";

let screenWidth = Dimensions.get("window").width;
let screenHeight = Dimensions.get("window").height;

const Alarm = memo(() => {
  const getAlarm = useCallback(async () => {
    try {
      console.log("TOKEN", TOKEN);
      await axios
        .get(`${BaseURL}/post/user/`, {
          headers: {
            Authorization: TOKEN,
          },
        })
        .then((response) => {
          console.log("alarm data", response.data);
        });
    } catch (error) {
      console.log(error);
      throw error;
    }
  }, []);

  console.log("X");

  useEffect(() => {
    getAlarm();
  }, []);

  return (
    <View style={{ ...styles.container }}>
      <View style={{ ...styles.main }}>
        <View style={{ flex: 0.5 }}></View>
        <View style={{...styles.keyContainer}}
        >
          <ScrollView horizontal pagingEnabled contentContainerStyle={{...styles.scrollBox}}>
            <Pressable style={{...styles.keyBox}}>
              <Text style={{ ...styles.key }}>
                1
              </Text>
            </Pressable>
            <Pressable style={{...styles.keyBox}}>
              <Text style={{ ...styles.key }}>
                2
              </Text>
            </Pressable>
            <Pressable style={{...styles.keyBox}}>
              <Text style={{ ...styles.key }}>
                3
              </Text>
            </Pressable>
            <Pressable style={{...styles.keyBox}}>
              <Text style={{ ...styles.key }}>
                4
              </Text>
            </Pressable>
            <Pressable style={{...styles.keyBox}}>
              <Text style={{ ...styles.key }}>
                5
              </Text>
            </Pressable>
          </ScrollView>
        </View>

        <View style={{...styles.infoContainer, backgroundColor: "blue" }}>

        </View>

        <View style={{flex:1}}>

        </View>
      </View>
    </View>
  );
});

export default Alarm;

const styles = StyleSheet.create({
  container: {
    backgroundColor: "white",
    flex: 1,
  },
  main:{
    flex: 10, width: "90%", marginLeft: "5%"
  },
  keyContainer:{
    flex: 1, 
    justifyContent: "center", 
    alignItems: "center", 
    flexDirection: "row"
  },
  scrollBox:{
    width: screenWidth * 0.9,
    backgroundColor: "red",
    alignItems: "center",
  },
  keyBox:{
    width: "20%",
    marginHorizontal: "5%",
  },
  key:{
    height: "50%", borderWidth: 1, textAlign: "center"
  },
  infoContainer:{
    flex: 6,
  }
});
