import firebase from "firebase/compat/app";
import "firebase/compat/firestore";
import "firebase/compat/database";

const firebaseConfig = {
  apiKey: "AIzaSyCCHLkcXGD-QSX5bBePv1S_KjiBwtSsYog",
  authDomain: "dummy-d18d5.firebaseapp.com",
  databaseURL: "https://dummy-d18d5-default-rtdb.firebaseio.com",
  projectId: "dummy-d18d5",
  storageBucket: "dummy-d18d5.appspot.com",
  messagingSenderId: "269803896644",
  appId: "1:269803896644:web:aca268cb21d466409ce111",
  measurementId: "G-WEKQDX0K18",
};

firebase.initializeApp(firebaseConfig);

export default firebase;
