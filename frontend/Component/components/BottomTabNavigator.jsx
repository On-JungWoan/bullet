import { FontAwesome } from '@expo/vector-icons';

import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";

import MyPage from "../pages/MyPage";
import Home from "../pages/Home";
import Alarm from '../pages/Alarm';

const BottomTab = createBottomTabNavigator();
const BottomTabNavigator = () => {
    return (
        <BottomTab.Navigator initialRouteName="Home" screenOptions={{
            tabBarStyle: {	           
                height: 60,
            },
            tabBarItemStyle: {
                height: 55,
            },
        }} >
            <BottomTab.Screen name="Alarm" component={Alarm} options={{
                headerShown: false, tabBarIcon: () => (
                    <FontAwesome name="comments-o" size={28} color="black" />
                ),
            }} />
            <BottomTab.Screen name="Home" component={Home} options={{
                headerShown: false, tabBarIcon: () => (
                    <FontAwesome name="home" size={28} color={"black"} />
                ),
            }} />
            <BottomTab.Screen name="MyPage" component={MyPage} options={{
                headerShown: false, tabBarIcon: () => (
                    <FontAwesome name="user" size={28} color="black" />)
            }} />
        </BottomTab.Navigator >
    );
}
export default BottomTabNavigator;