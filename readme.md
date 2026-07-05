# 🔥 Algerian Forest Fire Prediction

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4-orange?logo=scikitlearn)
![Render](https://img.shields.io/badge/Deployment-Render-46E3B7?logo=render)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-red)
![Status](https://img.shields.io/badge/Project-Live-success)

A Machine Learning-powered web application that predicts the **Fire Weather Index (FWI)** using meteorological data from the Algerian Forest Fires dataset. The application is built with **Flask** and deployed online for real-time predictions.

🌐 **Live Demo:** https://algerian-forest-fire-prediction-3gqw.onrender.com/

## 📌Project Overview

Forest fires are one of the most destructive natural disasters. Predicting fire weather conditions can help authorities take preventive measures and reduce damage.

This application uses a **Ridge Regression** model trained on the **Algerian Forest Fires Dataset** to estimate the **Fire Weather Index (FWI)** based on weather conditions.

##  What is Fire Weather Index (FWI)?

The Fire Weather Index (FWI) is a numerical indicator used to estimate the potential intensity and spread of forest fires based on weather conditions. Higher FWI values indicate more favorable conditions for wildfire ignition and rapid spread.

| FWI Range    | Risk Level       |
| ------------ | ---------------- |
| **0 – 5**    | 🟢 Very Low Risk |
| **5 – 15**   | 🟡 Low Risk      |
| **15 – 30**  | 🟠 Moderate Risk |
| **Above 30** | 🔴 High Risk     |

## 🚀 **Features**

- Predicts Fire Weather Index (FWI)
- Interactive Flask Web Interface
- Real-time predictions
- Risk classification
- Error handling
- Responsive UI
- Cloud deployment using Render

## 📊 **Machine Learning Model**

### Algorithm Used
- Ridge Regression

### Why Ridge Regression?

- Reduces overfitting using L2 Regularization
- Performs well with correlated features
- Produces stable predictions
- Suitable for continuous value prediction (FWI)

## 📂 Input Features

| Feature                    | Description                                                                       |
| -------------------------- | --------------------------------------------------------------------------------- |
| **Region**                 | Indicates the geographical region of Algeria where the weather data was recorded. |
| **Temperature**            | Measures the ambient air temperature in degrees Celsius (°C).                     |
| **RH (Relative Humidity)** | Represents the percentage of moisture present in the air.                         |
| **Ws (Wind Speed)**        | Indicates the speed of the wind in kilometers per hour (km/h).                    |
| **Rain**                   | Measures the amount of rainfall received in millimeters (mm).                     |
| **FFMC**                   | Represents the moisture content of fine fuels like dry leaves and grass.          |
| **DMC**                    | Indicates the moisture level of decomposed organic matter on the forest floor.    |
| **ISI**                    | Estimates how quickly a fire is likely to spread after ignition.                  |
| **Classes**                | Represents whether fire conditions were observed (`1 = Fire`, `0 = No Fire`).     |
Note: These features are preprocessed using StandardScaler before being passed to the trained Ridge Regression model, which predicts the Fire Weather Index (FWI).
## 📈 Output

The application predicts the **Fire Weather Index (FWI)** and categorizes the wildfire risk.

Example:

FWI Prediction = 24.87

Risk Level = Moderate Risk

Recommendation = Stay Alert. Avoid Campfires.

## 🛠 Tech Stack

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Ridge Regression
- StandardScaler
- NumPy
- Pandas

### Backend

- Flask

### Frontend

- HTML5
- CSS3
- JavaScript

### Deployment

- Render
- GitHub

## 📁 Project Structure

```
Algerian-Forest-Fire-Prediction
│
├── Models
│   ├── ridge_model.pkl
│   └── scaler.pkl
│
├── static
│
├── templates
│   ├── index.html
│   └── home.html
│
├── app.py
├── requirements.txt
├── runtime.txt
├── Procfile
└── README.md
```

## 📸 Screenshots

### Home Page
<img width="1082" height="716" alt="image" src="https://github.com/user-attachments/assets/bc2ca1a6-7fca-4aa6-8bdb-682f7926e9ae" />

### Prediction Result
<img width="742" height="563" alt="image" src="https://github.com/user-attachments/assets/2eb54fe8-9078-4bdd-a703-d81204a7ae6d" />

## 📚 Dataset

The project uses the **Algerian Forest Fires Dataset**, containing meteorological observations and fire occurrence records from two regions of Algeria.

## 🎯 Future Improvements

- Weather API Integration
- Interactive Charts
- Dark Mode
- Prediction History
- PDF Report Generation
- User Authentication
- Deep Learning Models
- XGBoost Comparison

## 👨‍💻 Developed By

**Krish Mahto**

B.Tech Artificial Intelligence & Data Science

Thakur College of Engineering & Technology

## ⭐ If you found this project helpful,

Please consider giving this repository a ⭐ on GitHub!
