// basic
import React, {useEffect, useState } from "react";
import {Text, View, Pressable, StyleSheet} from "react-native";
  
// install
import { useNavigation, useRoute } from "@react-navigation/native";
import { FontAwesome } from '@expo/vector-icons';


const AlarmDetail = ()=>{
    const navigation = useNavigation();
    const route = useRoute("AlarmDetail")

    const [data, setData] = useState();
    const [index, setIndex] = useState();
  
    useEffect(() => {
      setData([...route.params?.data]);
      setIndex(route.params?.index);
    }, []);
    
    return(
        <View style={{ flex: 1 }}>
            <View style={{ flex: 1,width: '90%', marginLeft: '5%', justifyContent:'center' }}>
                <Pressable style={{marginLeft:20}} onPress={()=>{navigation.pop();}}>
                    <FontAwesome name="arrow-left" size={40} color="black" />
                </Pressable>
            </View>
            <View style={{ flex: 6, borderWidth: 1, width: '90%', marginLeft: '5%' }}>
                <View style={{...styles.header}}>
                    <Text style={{...styles.textTitle }}>알림제목</Text>
                    {data?.length ? 
                        <Text style={{ ...styles.textSub}}>
                            {data[index].title}
                        </Text>
                    : null}
                </View>

                <View style={{ flex: 2, paddingHorizontal: '5%' }}>
                    <Text style={{...styles.textTitle }}>알림내용요약</Text>
                    {data?.length ? 
                        <Text style={{ ...styles.textSub }}>
                            {data[index].content}
                        </Text>
                    : null}
                </View>

                <View style={{flex: 1, paddingHorizontal: '5%', justifyContent: 'center'}}>
                    <Text style={{...styles.textTitle }}>알림내용링크</Text>
                    {data?.length ? 
                        <Text style={{ ...styles.textSub }}>
                            {data[index].url}
                        </Text>
                    : null}
                </View>
            </View>

            <View style={{...styles.buttonContainer}}>
                {index!==0 ?
                    <Pressable onPress={() => {
                        setIndex(current => current - 1);
                        }}>
                        <Text style={{...styles.buttonText }}>
                        이전 알림
                        </Text> 
                    </Pressable>
                :
                    <Pressable onPress={() => {
                        setIndex(current => current - 1);
                        }}>
                    </Pressable>
                }

                {index !== data?.length-1 ? 
                    <Pressable onPress={() => {
                        setIndex(current => current + 1);
                        }}>
                        <Text style={{...styles.buttonText }}>
                        다음 알림
                        </Text> 
                    </Pressable>
                :             
                    <Pressable onPress={() => {
                        setIndex(current => current + 1);
                        }}>
                    </Pressable>
                }
            </View>
            <View style={{flex:1}}></View>
        </View>
    )
}

export default AlarmDetail;

const styles = StyleSheet.create({
    header:{
        flex: 1,
        paddingHorizontal: '5%',
        justifyContent: 'center',
    },
    textTitle:{
        fontSize: 15, 
        fontWeight: 'bold', 
        borderBottomWidth: 1,
    },
    textSub:{
        marginTop: 2, 
        paddingLeft: 10
    },
    buttonContainer:{
        width: '90%', 
        marginLeft: '5%', 
        flexDirection: "row",
        marginTop: 10, 
        justifyContent:'space-between'
    },
    buttonText:{
        color: "black", 
        fontSize:20
    }
})