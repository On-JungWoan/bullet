// basic
import React, { useState, useContext } from "react";
import { Text, View, StyleSheet, TextInput } from "react-native";

// install
import axios from "axios";
import { useNavigation } from "@react-navigation/native";
import { API_URL } from '@env';
const URL = API_URL

// from App.js
import { dataContext } from "../../App";
import { AddSITE } from "../../App";
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

  const postSite = async () => {
    if (transSite.length === 0) {
      alert("선택한 사이트가 없습니다.");
      return;
    }

    const data = {
      sites: [...user.newsSites, ...user.workSites, ...transSite],
    };

    dispatch({
      type: AddSITE,
      newsSites: user.newsSites,
      uniSites: transSite,
      workSites: user.workSites,
    });

    try {
      await axios
        .post(`${URL}/user/site/create/`, data, {
          headers: {
            Authorization: TOKEN,
          },
        })
        .then(function (response) {
          // console.log("SitesSelectPage", response.data);
          navigation.navigate("Keywords",{category:"announce"});
        })
        .catch(function (error) {
          throw error;
        });
    } catch (error) {
      alert(`ERROR ${error}`);
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
