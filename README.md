# 🌱 FertiMind - Smart Fertilizer Advisor Using AI

---

## 🎯 Project Goal

**FertiMind** is a machine learning–based web application that predicts the most suitable fertilizer based on soil and environmental conditions. It simplifies fertilizer decision-making for farmers and agricultural planners, helping improve yield, reduce wastage, and support smart farming practices.

---

## 📌 Project Overview

Agriculture plays a crucial role in global food security. Often, farmers apply fertilizers without scientific analysis, which leads to environmental damage and poor crop yield. **FertiMind** solves this by predicting the right fertilizer based on:

- **Soil Type**
- **Crop Type**
- **Nutrient Content (N, P, K)**
- **Temperature, Humidity, Moisture**

The prediction is done using a **Decision Tree Classifier**, and the app is deployed with **Streamlit** for a user-friendly interface.

---

## 🔄 Project Workflow

### 1. 📊 Data Preprocessing
- Dataset used: `Crop_recommendation.csv`
- Loaded and cleaned using **Pandas**
- Converted categorical features like soil and crop types into numerical form using manual mapping
- Feature Scaling was performed using **StandardScaler** to normalize the data
- Used **Seaborn** and **Matplotlib** to explore correlations and distributions

### 2. 🤖 Model Building
- Machine Learning Algorithm: **Decision Tree Classifier**
- Split the dataset into training and testing sets using an 80/20 ratio:
  - **80%** for training the model
  - **20%** for testing the model
- Trained using **Scikit-learn’s** `DecisionTreeClassifier`
- Saved the trained model and scaler using **Pickle** for deployment

### 3. 📈 Evaluation Metrics
- **Accuracy Score**: Achieved approximately `100%` on the test set
- Model was evaluated using:
  - Train-test split validation
  - Accuracy as the primary metric

### 4. 🌐 Deployment
- Web app created using **Streamlit**
- Users input:
  - Environmental conditions
  - Soil and crop types
  - Nutrient levels
- Model processes the input and outputs a fertilizer recommendation in real time

---

## 🧰 Tech Stack

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn**
- **Seaborn**, **Matplotlib**
- **Streamlit**
- **Pickle**

---

## 📁 Project Structure

```bash
FertiMind/
│
├── app.py                           # Streamlit app for frontend and prediction
├── model.pkl                        # Trained Decision Tree model
├── scaler.pkl                       # StandardScaler object used for preprocessing
├── Crop_recommendation.csv          # Dataset used for training and testing
├── Fertilizer_Recommendation_System.ipynb  # Jupyter notebook for EDA & model building
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```
---

## 🔍 Features

- Intuitive web interface for quick fertilizer prediction
- Selectable soil and crop types
- Real-time ML-based recommendation
- Simple UI suitable for educational or prototype use

---

## 🌱 Future Enhancements

- Add confusion matrix and precision/recall evaluation
- Use location-based environmental data (e.g., rainfall, region)
- Add multilingual support for farmers in different regions
- Enhance model with deep learning or ensemble methods
- Mobile-responsive or offline Android version

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use, share, and modify with attribution.

---

