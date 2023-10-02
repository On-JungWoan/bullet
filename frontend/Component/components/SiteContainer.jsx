// basic
import React from "react";
import { Text, View, StyleSheet, Image, FlatList, Pressable} from "react-native";

// install
import { useNavigation } from "@react-navigation/native";

// from App.js

export default function SitesSelectPage({numColumns, transData, transSite, setTransSite, postSite,}) {
  const navigation = useNavigation();
  
  const renderItem = ({item, index}) =>{
    return(
      <Pressable style={{ marginVertical: 10, flex:1 }} onPress={() => {
        if (!transSite.includes(item.site)) {
          setTransSite([...transSite, item.site]);
        } else {
          let deleteSite = transSite;
          deleteSite.splice(deleteSite.indexOf(item.site), 1);
          setTransSite([...deleteSite]);
        }
      }}>
        <Image style={{ width: '100%', height: 80,
                    resizeMode: "contain", marginBottom: 3}}
          source={item.src}
        />
        <Text style={{ fontSize: 15, textAlign: "center" }}>{item.id}</Text>
      </Pressable>
    )
  }

  return (
    <View style={{flex:1, width:'100%'}}>
      <View style={{...styles.sitesContainer, flex:5}}>
        <FlatList
          data={transData}
          renderItem={renderItem}
          numColumns={numColumns}
        />
      </View>

      <View style={{ ...styles.buttonContainer }}>
        <Pressable
          style={{ ...styles.button }}
          onPress={() => {
            navigation.pop();
          }}
        >
          <Text style={{ color: "white", textAlign: "center" }}>이전 화면</Text>
        </Pressable>

        <Pressable
          style={{ ...styles.button }}
          onPress={() => {
            postSite();
          }}
        >
          <Text style={{ color: "white", textAlign: "center" }}>등록하기</Text>
        </Pressable>
      </View>
      <View>
        {transSite?.length ? (
          <Text style={{ fontSize: 20 }}>{`선택 : ${transSite}`}</Text>
        ) : null}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  sitesContainer: {
    borderWidth: 2,
    marginTop: 10,
  },
  buttonContainer: {
    flex: 1,
    flexDirection: "row",
    backgroundColor: "Red",
    flexWrap: "wrap",
    marginTop: 10,
  },
  button: {
    flex: 1,
    backgroundColor: "black",
    borderWidth: 1,
    borderRadius: 20,

    paddingHorizontal: 15,
    paddingVertical: 8,
    marginHorizontal: 10,
  },
});
