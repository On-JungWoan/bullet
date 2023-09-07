// basic
import React, { useEffect, useState, useContext, useCallback } from "react";
import { Text, View, StyleSheet, TextInput, Dimensions } from "react-native";

// install
import axios from "axios";
import { useNavigation } from "@react-navigation/native";

// from App.js
import { dataContext } from "../../App";
import { AddSITE } from "../../App";
import { BaseURL } from "../../App";
import { TOKEN } from "./Main";

// 데이터
import { workData } from "../../Work";

// component
import SitesSelectPage from "../components/SiteContainer";

const windowWidth = Dimensions.get("window").width;

export default function WorkSite() {
  const navigation = useNavigation();

  const { user, dispatch } = useContext(dataContext);

  const [searchValue, setSearchValue] = useState(""); // 검색 값
  const [keywords, setKeywords] = useState(
    user.keywords?.length ? [...user.keywords] : []
  );

  const [transSite, setTransSite] = useState([...user.workSites]); // 선택한 사이트

  const postSite = async () => {
    if (transSite.length === 0) {
      alert("선택한 사이트가 없습니다.");
      return;
    }

    const data = {
      sites: [...user.newsSites, ...user.uniSites, ...transSite],
    };

    console.log(data);
    console.log("transSite", user.newsSites);
    console.log("user.uniSites", user.uniSites);
    console.log("user.workSites", transSite);

    dispatch({
      type: AddSITE,
      newsSites: user.newsSites,
      uniSites: user.uniSites,
      workSites: transSite,
    });

    try {
      await axios
        .post(`${BaseURL}/user/site/create/`, data, {
          headers: {
            Authorization: TOKEN,
          },
        })
        .then(function (response) {
          console.log("SitesSelectPage", response.data);
          navigation.navigate("Register");
        })
        .catch(function (error) {
          alert("에러발생");
          console.log("error", error);
          throw error;
        });
    } catch (error) {
      console.log("error", error);
      throw error;
    }
  };

  // 검색 기능
  onChangeSearch = (e) => {
    setSearchValue(e);
  };

  // enter 이벤트 미완성, 검색 값을 포함하는 결과를 보여줌
  onSubmitText = () => {
    if (searchValue === "") {
      return;
    }

    setKeywords([...keywords, searchValue]);
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
            placeholder="사이트를 검색하세요"
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
            width={windowWidth*0.9*0.45}
            transData={workData}
            transSite={transSite}
            setTransSite={setTransSite}
            postSite={postSite}
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
