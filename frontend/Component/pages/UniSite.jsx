// basic
import React, { useState, useContext } from "react";
import { Text, View, StyleSheet, TextInput, Alert } from "react-native";

// install
import axios from "axios";
import { useNavigation } from "@react-navigation/native";
import { API_URL } from '@env';
const URL = API_URL

// from App.js
import { dataContext } from "../../App";
import { AddSITE, AddKEYWORD } from "../../App";
import { TOKEN } from "./Main";

// 데이터
import { universityData } from "../../university";

// component
import SitesSelectPage from "../components/SiteContainer";

export default function UniSite() {
  const navigation = useNavigation();

  const { user, dispatch } = useContext(dataContext);

  const [searchValue, setSearchValue] = useState(""); // 검색 값
  const [transSite, setTransSite] = useState([...user.uniSites]); // 선택한 사이트

  // site를 선택한지 학인
  const checkSiteLength = (sites) => {
    const count = sites.length;

    if (count === 0) {
      Alert.alert('사이트를 선택하지 않았습니다.', '사이트를 삭제하시는 건가요?', [
        {
          text: '아니요',
          onPress: () => postSite("Keywords"),
          style: 'cancel',
        },
        {text: '네', onPress: () => {
          dispatch({
            type: AddKEYWORD,
            newsKeywords:user.newsKeywords,
            uniKeywords:[],
            workKeywords:user.workKeywords,
          })
          postSite("Register")
        }},
      ]);
    } else {
      postSite("Keywords")
    }
  }

  // 사이트 전송
  const postSite = (where) => {
    const data = {
      sites: [...user.newsSites, ...user.workSites, ...transSite],
    };

    dispatch({
      type: AddSITE,
      newsSites: user.newsSites,
      uniSites: transSite,
      workSites: user.workSites,
    });

    axios
    .post(`${URL}/user/site/create/`, data, {
      headers: {
        Authorization: TOKEN,
      }
    })
    .then(function (response) {
      // console.log("SitesSelectPage", response.data);
      if(where === "Keywords"){
        navigation.navigate("Keywords", {category:"announce"});
      } else if(where === "Register"){
        navigation.navigate("Register");
      }
    })
    .catch(function (error) {
      throw alert(`ERROR ${error}`);
    });
  }

  // 검색 기능
  onChangeSearch = (e) => {
    setSearchValue(e);
  };

  // enter 이벤트 미완성, 검색 값을 포함하는 결과를 보여줌
  onSubmitText = () => {
    if (searchValue === "") {
      return;
    }

    setSearchValue("");
  };

  return (
    <View style={{ flex: 1, backgroundColor: "white" }}>
      <View style={{ flex: 1, width: "90%", marginLeft: "5%" }}>
        <View style={{ ...styles.headContainer }}>
          <Text style={{ ...styles.searchText }}>
            원하는 사이트를 선택하세요
          </Text>

          <TextInput
            placeholder="아직 구현 x"
            autoCapitalize="none"
            autoCorrect={false}
            style={{ ...styles.searchInput }}
            value={searchValue}
            onChangeText={onChangeSearch}
            onSubmitEditing={onSubmitText}
          />
        </View>
        <View style={{ ...styles.showSite }}>
          <SitesSelectPage
            numColumns={3}
            transData={universityData}
            transSite={transSite}
            setTransSite={setTransSite}
            checkSiteLength={checkSiteLength}
          />
        </View>
        <View style={{ flex: 1 }}></View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  headContainer: {
    flex: 1.5,
    justifyContent: "center",
    alignItems: "center",

    marginTop: "15%",
  },
  showSite: {
    flex: 7,
    justifyContent: "center",
    alignItems: "center",
  },
  arrow: {
    position: "absolute",
    top: 25,
    left: 25,
  },
  searchText: {
    color: "black",
    fontSize: 20,
    fontWeight: 700,
    textAlign: "center",
  },
  searchInput: {
    textAlign: "center",
    fontSize: 20,
    borderRadius: 10,
    borderWidth: 1,
    width: "80%",
    marginTop: 10,
  },
});
