import { useNavigation } from "@react-navigation/core";
import React from "react";
import { auth, firedb } from "../firebase";
import {
  ImageBackground,
  StyleSheet,
  TouchableOpacity,
  View,
  Text,
  Image,
  Alert,
} from "react-native";
import { useState, useEffect } from "react";
import firebase from "../firebase";
import "firebase/database";

const HomeScreen = () => {
  const navigation = useNavigation();

  const showAlert = () =>
    Alert.alert("Fee not Paid", "Please pay your parking fee to continue", [
      {
        text: "Exit",
        onPress: () => handleSignOut(),
        style: "cancel",
      },
    ]);

  const handleSignOut = () => {
    auth
      .signOut()
      .then(() => {
        navigation.replace("Login");
      })
      .catch((error) => alert(error.message));
  };

  const [parking_spots, setparking_spots] = useState([]);
  const [loading, setloading] = useState(false);
  const ref = firedb.database().ref("Parking_Spots");
  const ref2 = firedb.firestore().collection("people");
  const [people, setpeople] = useState([]);

  function getParking_Spots() {
    ref.on("value", (snapshot) => {
      let docs = snapshot.val();
      const parking = [];
      for (let doc in docs) {
        parking.push({
          index: docs[doc].index,
          availability: docs[doc].availability,
        });
      }
      console.log(parking);
      setparking_spots(parking);
      setloading(false);
    });
  }

  function getpeople() {
    ref2.onSnapshot((querySnapshot) => {
      const ppl = [];
      querySnapshot.forEach((doc) => {
        ppl.push(doc.data());
      });
      setpeople(ppl);
      console.log(people);
    });
  }

  useEffect(() => {
    getParking_Spots();
    getpeople();
  }, []);

  if (loading) {
    return <Text>Loading...</Text>;
  }

  return (
    <ImageBackground
      style={styles.background}
      source={require("./background.png")}
    >
      <TouchableOpacity onPress={handleSignOut} style={styles.button}>
        <Text style={styles.buttonText}>Sign out</Text>
      </TouchableOpacity>

      <View style={styles.textstyle}>
        <Text style={{ fontSize: 40, fontWeight: "bold" }}>Welcome!</Text>
        <Text style={{ fontSize: 20, fontWeight: "bold" }}>
          {" "}
          Please Park your car in your designated area.
        </Text>
      </View>

      {parking_spots.some((p) => p.availability === true && p.index === 1) ? (
        <Image
          resizeMode="contain"
          style={styles.parking1}
          source={require("./handicappedspot1.png")}
        ></Image>
      ) : (
        <Image
          resizeMode="contain"
          style={styles.parking1}
          source={require("./occupiedspot1.png")}
        ></Image>
      )}

      {parking_spots.some((p) => p.availability === true && p.index === 2) ? (
        <Image
          resizeMode="contain"
          style={styles.parking2}
          source={require("./emptyspot2.png")}
        ></Image>
      ) : (
        <Image
          resizeMode="contain"
          style={styles.parking2}
          source={require("./occupiedspot2.png")}
        ></Image>
      )}

      {parking_spots.some((p) => p.availability === true && p.index === 3) ? (
        <Image
          resizeMode="contain"
          style={styles.parking3}
          source={require("./emptyspot3.png")}
        ></Image>
      ) : (
        <Image
          resizeMode="contain"
          style={styles.parking3}
          source={require("./occupiedspot3.png")}
        ></Image>
      )}
    </ImageBackground>

    // <View style={styles.container}>

    //   {/* <TouchableOpacity onPress={handleSignOut} style={styles.button}>
    //     <Text style={styles.buttonText}>Sign out</Text>
    //   </TouchableOpacity> */}
    // </View>
  );
};

export default HomeScreen;

const styles = StyleSheet.create({
  background: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "flex-end",
  },
  parking1: {
    position: "absolute",
    width: 120,
    height: 215,
    backgroundColor: "black",
    bottom: 200,
    left: "5%",
  },

  parking2: {
    position: "absolute",
    width: 120,
    height: 215,
    backgroundColor: "white",
    bottom: 200,
  },

  parking3: {
    position: "absolute",
    width: 120,
    height: 215,
    backgroundColor: "black",
    bottom: 200,
    right: "5%",
  },

  textstyle: {
    position: "absolute",
    top: 100,
    alignItems: "center",
  },
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  button: {
    backgroundColor: "#0782F9",
    width: "60%",
    padding: 15,
    borderRadius: 10,
    alignItems: "center",
    marginTop: 40,
    bottom: 10,
  },
  buttonText: {
    color: "white",
    fontWeight: "700",
    fontSize: 16,
  },
});
