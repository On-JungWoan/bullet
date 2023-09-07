import {
    View,
    StyleSheet,
    Pressable,
    Text
} from 'react-native';

const BasicButton = ({text, bg, textColor, onPressEvent, marginBottom}) => {
    return (
        <View>
            <Pressable style={{ ...styles.button, backgroundColor:bg, marginBottom:marginBottom}} onPress={onPressEvent}>
                <Text style={{ color: textColor, fontSize: 20, fontWeight: 700 }}>{text}</Text>
            </Pressable>
        </View>
    );
};

const styles = StyleSheet.create({
    button: {
        borderWidth: 2,
        borderRadius: 15,
        borderStyle: 'solid',

        justifyContent: "center",
        alignItems: "center",

        paddingHorizontal: 20,
        paddingVertical: 10,
    }
});

export default BasicButton;