import React from "react";
import UnAvailableparkingspot from "./images/UnAvailableParking.png";
import car1 from "./images/car1.png";
import car2 from "./images/car2.png";
import car3 from "./images/car3.png";

export default function UnAvailable(props) {
  let index = 0;
  var cars = [car1, car2, car3];
  index = Math.floor(Math.random() * cars.length);

  return (
    <div className="card bg-dark text-white">
      <img
        src={cars[index]}
        className="card-img img-fluid"
        alt="..."
        style={{ maxheight: "350px" }}
      />
      <div className="card-img-overlay text-end row ms-0 p-0">
        <div className="col border border-3 me-3 align-self-end pt-1">
          <h5 className="card-title text-center">{props.spot}</h5>
        </div>
      </div>
    </div>
  );
}
