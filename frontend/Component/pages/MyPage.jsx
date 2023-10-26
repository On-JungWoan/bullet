import AsyncStorage from "@react-native-async-storage/async-storage";

import React, { useEffect, useState, useContext } from "react";
import { Text, Button, View, StyleSheet, Image, ScrollView } from "react-native";
import { NAME } from "../../App";

import { useNavigation } from "@react-navigation/native";
import { dataContext } from "../../App";
import { LOGOUT } from "../../App";

const MyPage = () => {
  const navigation = useNavigation();

  const { dispatch, user } = useContext(dataContext);
  const [name, setName] = useState("");

  useEffect(() => {
    AsyncStorage.getItem(NAME).then((value) => setName(value));
  }, []);

  return (
    <View style={{ flex: 1, backgroundColor:'#fff' }}>
      <View style={{ flex: 1, width: "90%", marginLeft: "5%" }}>
        <View style={{ flex: 0.5 }}></View>

        <View style={{ flex: 1, justifyContent: "center" }}>
          <Text style={{ fontSize: 24, fontWeight: 400 }}>{name}님</Text>
        </View>

        <View style={{ flex: 0.5 }}></View>

        <View style={{ flex: 2 }}>
          <View style={{ ...styles.usingContainer }}>
            <View style={{ flex: 1 }}>
              <Text style={{ ...styles.usingText }}>이용권</Text>
            </View>
            <View style={{ flex: 1 }}>
              <Text style={{ ...styles.usingText }}>사이트</Text>
            </View>
            <View style={{ flex: 1 }}>
              <Text style={{ ...styles.usingText }}>키워드</Text>
            </View>
          </View>
          <View style={{ ...styles.countContainer }}>
            <View style={{...styles.rating }}>
            <Image style={{width:"70%", height:"60%", resizeMode : "stretch"}} source={require("../../assets/rating.png")}/>
            </View>
            <View style={{...styles.sitesCount}}>
              <Text>
                현재 사용 : {user.newsSites.length+user.uniSites.length+user.workSites.length}
              </Text>
            </View>
            <View style={{...styles.keywordsCount}}>
              <Text>
                현재 사용 : {user.newsKeywords.length +user.uniKeywords.length + user.workKeywords.length}
              </Text>
            </View>
          </View>
        </View>

        <View style={{ flex: 0.5 }}></View>

        <View style={{ flex: 1, justifyContent: "center" }}>
          <Text style={{ fontSize: 16, fontWeight: 400 }}>
            {name}님이 구독 중인 키워드/사이트
          </Text>
        </View>

        <View style={{ flex: 2, marginVertical: "3%" }}>
          <View style={{...styles.showBox}}>
            <Text style={{ color: "white" }}>뉴스</Text>
          </View>
          <View style={{ borderWidth: 1, flex: 3, flexDirection: "row" }}>
            <ScrollView>
              {
                [...user.newsSites]?.map((site, index) => {
                  return(
                    <View style={{alignItems:'center', marginVertical:5}} key={site}> 
                      <Text>{site} : {user.newsKeywords.join(', ')}</Text>
                    </View>
                  )
                })
              }
            </ScrollView>
          </View>
        </View>

        <View style={{ flex: 2, marginVertical: "3%" }}>
          <View style={{...styles.showBox}}>
            <Text style={{ color: "white" }}>대학</Text>
          </View>
          <View style={{ borderWidth: 1, flex: 3, flexDirection: "row" }}>
          <ScrollView>
              {
                [...user.uniSites]?.map((site, index) => {
                  return(
                    <View key={site} style={{alignItems:'center', marginVertical:5}}> 
                      <Text>{site} : {user.uniKeywords.join(', ')}</Text>
                    </View>
                  )
                })
              }
            </ScrollView>
          </View>
        </View>

        <View style={{ flex: 2, marginVertical: "3%" }}>
          <View style={{...styles.showBox}}>
            <Text style={{ color: "white" }}>취업</Text>
          </View>
          <View style={{ borderWidth: 1, flex: 3, flexDirection: "row" }}>
            <ScrollView>
              {
                [...user.workSites]?.map((site, index) => {
                  return(
                    <View style={{alignItems:'center', marginVertical:5}} key={site}> 
                      <Text>{site} : {user.workKeywords.join(', ')}</Text>
                    </View>
                  )
                })
              }
            </ScrollView>
          </View>
        </View>
        <View>
          <Button
            title="로그아웃"
            onPress={() => {
              navigation.replace("Login");
              dispatch({
                type: LOGOUT,
                login: false,
              });
              navigation.reset({index:0 ,routes: [{name: 'Login'}]})
              AsyncStorage.clear();
            }}
          />
        </View>
        <View style={{ flex: 1 }}></View>
      </View>
    </View>
  );
};

export default MyPage;

const styles = StyleSheet.create({
  usingContainer: {
    flex: 1,
    flexDirection: "row",
  },
  usingText: {
    fontSize: 12,
    textAlign: "center",
    fontWeight: "bold",
  },
  countContainer: {
    borderWidth: 1,
    flex: 4,
    flexDirection: "row",
  },
  rating : {
    flex: 1,
    borderRightWidth: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  sitesCount:{
    flex: 1,
    borderRightWidth: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  keywordsCount : {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  showBox : {
    flex: 1,
    backgroundColor: "black",
    justifyContent: "center",
    alignItems: "center",
  }
});