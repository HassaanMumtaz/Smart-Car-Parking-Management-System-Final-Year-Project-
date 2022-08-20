import "bootstrap/dist/css/bootstrap.min.css";
import React, { useState, useEffect } from "react";
import firebase from "./firebase";
import "firebase/database";
import Available from "./Available";
import UnAvailable from "./UnAvailable";
import parkingspot from "./images/parkingspot.png";

function App() {
  const [parking_spots, setparking_spots] = useState([]);
  const [loading, setloading] = useState(false);
  const ref = firebase.database().ref("Parking_Spots");

  function getParking_Spots() {
    // ref.onSnapshot((querySnapshot) => {
    //   const parking = [];
    //   querySnapshot.forEach((doc) => {
    //     parking.push(doc.data());
    //   });
    //   setParking_Spots(parking);
    //   setloading(false);
    // });

    console.log("hello");
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

  useEffect(() => {
    getParking_Spots();
  }, []);

  if (loading) {
    return <h1>Loading...</h1>;
  }

  return (
    <div className="fluid-container bg-dark bg-gradient vh-100">
      <div className="hero-image">
        <div className="hero-text">
          <h1>Welcome!</h1>
          <h3>Please Park your car in your designated area.</h3>
        </div>
      </div>
      <div className="container">
        <div className="row ms-1 mt-3">
          <div className="col text-end "></div>
          <div className="col  text-center text-light mt-1">
            <h6>
              Parking Spots{" "}
              <span className="badge bg-info text-dark ms-2 me-1">
                {parking_spots.length}
              </span>
              Available
              <span className="badge bg-info text-dark ms-2 me-1">
                {parking_spots.filter((p) => p.availability === true).length}
              </span>{" "}
              Occupied
              <span className="badge bg-info text-dark ms-2">
                {parking_spots.filter((p) => p.availability !== true).length}
              </span>
            </h6>
          </div>
          <div className="col  text-start"></div>
        </div>
        <div className="row  mt-3 " style={{ height: "350px" }}>
          <div className=" col-3  p-0"></div>
          <div className=" col-2  p-0">
            {parking_spots.some(
              (p) => p.availability === true && p.index === 1
            ) ? (
              <Available spot={"01"}></Available>
            ) : (
              <UnAvailable spot={"01"}></UnAvailable>
            )}
          </div>
          <div className="  col-2  p-0 ">
            {parking_spots.some(
              (p) => p.availability === true && p.index === 2
            ) ? (
              <Available spot={"02"}></Available>
            ) : (
              <UnAvailable spot={"02"}></UnAvailable>
            )}
          </div>
          <div className=" col-2   p-0">
            {parking_spots.some(
              (p) => p.availability === true && p.index === 3
            ) ? (
              <Available spot={"03"}></Available>
            ) : (
              <UnAvailable spot={"03"}></UnAvailable>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
