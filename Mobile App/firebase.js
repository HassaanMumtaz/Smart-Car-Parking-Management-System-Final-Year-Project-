// Import the functions you need from the SDKs you need
import * as firebase from "firebase";
import "firebase/firestore";
import "firebase/database";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
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

// Initialize Firebase
let app;
if (firebase.apps.length === 0) {
  app = firebase.initializeApp(firebaseConfig);
} else {
  app = firebase.app();
}

const auth = firebase.auth();
const firedb = firebase;

export { auth, firedb };
