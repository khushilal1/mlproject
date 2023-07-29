import React, { useState } from "react";
import "./predict.css";

// Predict component
const Predict = () => {
  // State values
  const [data, setData] = useState("");
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState({
    Year: "",
    Present_Price: "",
    Kms_Driven: "",
    Owner: "",
    Fuel_Type_Petrol: "",
    Seller_Type_Individual: "",
    Transmission_Mannual: "",
  });

  // Input field change handler -> input field herne
  const setFormHandler = (e) => {
    const { name, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: +value,
    }));
    console.log(formData);
  };

  // Form submitting handler -> form submit garepaxi
  const formSubmitHandler = (e) => {
    e.preventDefault();
    console.log(formData);
    setLoading(true);
    fetch("http://localhost:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      // Body baata hamro form ko data pathaako
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        // Status success vayepachi prediction ko response paayeko ra store gareko
        setData(data);
        setLoading(false);
      })
      .catch((error) => {
        // error vaye error
        console.error(error);
      });
  };

  // Clear field button handler

  const clearHandler = () => {
    setFormData({
      Year: "",
      Present_Price: "",
      Kms_Driven: "",
      Owner: "",
      Fuel_Type_Petrol: "",
      Seller_Type_Individual: "",
      Transmission_Mannual: "",
    });
    setData(null);
  };

  // Returning JSX
  return (
    <div className="container">
      <p className="title">
        <h1>Welcome to the Car Price Prediction Web Reat App</h1>
      </p>
      <p className="desc">Testing flask react with ML (Linear Regression)</p>

      <form onSubmit={formSubmitHandler}>
        <input
          type="number"
          name="Year"
          placeholder="Enter the year in which you buy this car."
          required="required"
          onChange={setFormHandler}
          value={formData.Year}
        />
        <input
          type="number"
          name="Present_Price"
          placeholder="Enter the cost price of car (in lpa)  in which you buy."
          required="required"
          onChange={setFormHandler}
          value={formData.Present_Price}
        />
        <input
          type="number"
          name="Kms_Driven"
          placeholder="Enter the meter reading of your car."
          required="required"
          onChange={setFormHandler}
          value={formData.Kms_Driven}
        />
        <input
          type="number"
          name="Owner"
          placeholder="0 for (first hand),1 for (second hand) and 3 for (third hand)"
          required="required"
          onChange={setFormHandler}
          value={formData.Owner}
        />

        <input
          type="text"
          name="Fuel_Type_Petrol"
          placeholder="Enter petrol or diesel or CNG as type of car"
          onChange={setFormHandler}
          value={formData.Fuel_Type_Petrol}
        />

        <input
          type="text"
          name=" Seller_type_individula"
          placeholder="Are you want sell car  to dealer or  individual?"
          onChange={setFormHandler}
          value={formData.Seller_Type_Individual}
        />

        <input
          type="text"
          name="Transmission_Mannual "
          placeholder="Is your car mechanical or automatic"
          onChange={setFormHandler}
          value={formData.Transmission_Mannual}
        />

        <div className="btn-container">
          <button type="submit">Predict Current Selling price</button>
          <button className="clear" onClick={clearHandler}>
            Clear field
          </button>
        </div>
      </form>
      <div className="data">
        {loading && <h4>Predicting...</h4>}

        {/* Data after making post request in the backend */}
        {data && (
          <>
            <p className="predicted-data">
              The selling price will be <strong>{data?.prediction}</strong>
              <br></br>
              The accuracy is <strong>{data?.accuracy}</strong>
            </p>
          </>
        )}
      </div>
    </div>
  );
};

export default Predict;
