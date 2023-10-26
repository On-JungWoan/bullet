// basic
import React, {
  useEffect, memo, useCallback,
  useContext, useState
} from "react";
import {
  Text, View, Pressable, StyleSheet, Dimensions, ScrollView,
} from "react-native";

// install
import axios from "axios";
import { useNavigation } from "@react-navigation/native";
import { API_URL } from '@env';
const URL = API_URL

// from
import { dataContext } from "../../App";
import { TOKEN } from "./Main";

const Alarm = memo(() => {
  const navigation = useNavigation();

  const { user } = useContext(dataContext);
  const userKeywords = new Set([...user?.newsKeywords, ...user?.uniKeywords, ...user?.workKeywords]);

  const [allAlarm, setAllAlarm] = useState([]); // 전체 알림 보관
  const [showAlarm, setShowAlarm] = useState([]); // 키워드에 대응하는 알람
  const [selectedKeyword, setSelectedKeyword] = useState('');
  const [keywords, setKeywords] = useState([]);


  const makeKeyword = () =>{
    const arr=[];
    [...userKeywords].map((keyword, index) => {
      let obj = {}
      obj.id = index;
      obj.keyword = keyword;
      arr.push(obj)
    })
    setKeywords(arr)
  }
  
  const getAlarm = useCallback(async () => {
    try {
      await axios
        .get(`${URL}/post/user/`, {
          headers: {
            Authorization: TOKEN,
          },
        })
        .then((response) => {
          // console.log("alarm data", response.data);
          setAllAlarm([...response.data]);
        });
    } catch (error) {
      console.log(error);
      throw error;
    }
  }, []);
  

  // 키워드 클릭 -> 일치하는 기사 보여줌
  const onPressKeyword = (text)=>{ 
    let arr = [];
    for (x in allAlarm) {
      if (allAlarm[x].keyword === text) {
        arr.push(allAlarm[x]);
      }
    }
    setShowAlarm([...arr]);
  }

  useEffect(() => {
    makeKeyword();
    getAlarm();
  }, []);

  return (
    <View style={{ ...styles.container }}>
      <View style={{ ...styles.main }}>
        <View style={{ ...styles.keyContainer }}>
          <ScrollView
            horizontal showsHorizontalScrollIndicator={false}
          > 
            {keywords?.map((item, index) => {
              return (
                <Pressable style={ selectedKeyword === index ? styles.keyBoxSelected :styles.keyBox } key={item.keyword}>
                  <Text
                    style={ selectedKeyword === index ? styles.keySelected : styles.key }
                    onPress={() => {
                      setSelectedKeyword(item.id);
                      onPressKeyword(item.keyword);
                    }}
                  >
                    {item.keyword}
                  </Text>
                </Pressable>
                );
              })
            }
          </ScrollView>
        </View>

        <View style={{ ...styles.infoContainer, borderWidth:1 }}>
            <ScrollView>
            {showAlarm?.map((ann, index) => {
              return (
                <View style={{ borderBottomWidth: 1, paddingHorizontal: 10 }} key={ann.title}>
                  <Pressable
                    onPress={() => {
                      navigation.navigate('AlarmDetail', {data:showAlarm, index:index})
                    }}>
                    <Text style={{marginVertical:2}} numberOfLines={1} ellipsizeMode="tail">{ann.title}</Text>
                    <Text style={{marginVertical:2}} numberOfLines={1} ellipsizeMode="tail">{ann.content}</Text>
                    <Text style={{marginVertical:2}} numberOfLines={1} ellipsizeMode="tail">{ann.url}</Text>
                    <Text style={{marginVertical:2}} numberOfLines={1} ellipsizeMode="tail">{ann.keyword}</Text>
                  </Pressable>
                </View>
              );
            })}
            </ScrollView>

        </View>

        <View style={{ ...styles.buttonContainer }}>
          
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
  main: {
    flex: 10,
    width: "90%",
    marginLeft: "5%",
  },
  keyContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "row",
  },
  keyBox: {
    borderWidth: 1,
    marginHorizontal: 10,
    paddingVertical: 5,
    paddingHorizontal: 13,
    borderRadius: 30,
  },
  keyBoxSelected:{
    borderWidth: 1,
    marginHorizontal: 10,
    paddingVertical: 5,
    paddingHorizontal: 13,
    borderRadius: 30,
    backgroundColor : 'black'
  },
  key: {
    textAlign: "center",
    fontSize: 20,
  },
  keySelected :{
    textAlign: "center",
    fontSize: 20,
    color: 'white'
  },
  infoContainer: {
    flex: 6,
  },
  buttonContainer: {
    flex: 1,
    flexDirection: "row",
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
