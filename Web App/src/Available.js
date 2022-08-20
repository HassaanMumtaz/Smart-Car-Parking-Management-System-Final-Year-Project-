import React from "react";
import parkingspot from "./images/parkingspot.png";

export default function Available(props) {
  return (
    <div className="card bg-dark text-white">
      <img
        src={parkingspot}
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
