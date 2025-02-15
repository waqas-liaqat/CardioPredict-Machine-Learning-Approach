# 🏥 Heart Disease Prediction

![Project Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-lightgrey)

## 📌 Project Overview
This project is a **machine learning-based web application** that predicts the likelihood of heart disease based on patient health metrics. The model is trained on a structured dataset using various supervised learning techniques. The backend is built using **Flask**, and the application will be deployed soon.

## 🔍 Features
- **Exploratory Data Analysis (EDA)**: Detailed insights into dataset trends and distributions.
- **Machine Learning Model Training**: Implemented multiple models with hyperparameter tuning.
- **Flask Web App** (Coming Soon): A user-friendly interface to input patient data and receive predictions.
- **Logging & Exception Handling**: Robust logging to track errors and execution.
- **Modular Pipeline**: Clean and structured code for easy modifications.

## 📁 Project Structure
```
Heart Disease Prediction/
│── artifacts/            # Stores model & data artifacts
│   │── data.csv         # Raw dataset
│   │── model.pkl        # Trained machine learning model
│   │── preprocessor.pkl # Data preprocessing pipeline
│   │── train.csv, test.csv # Training & testing datasets
│
│── notebook/            # Jupyter notebooks for EDA & Model Training
│   │── 1. EDA.ipynb
│   │── 2. Model Training.ipynb
│
│── src/                 # Source code
│   │── components/      # Custom components for training
│   │── pipeline/        # Machine learning pipeline
│   │── exception.py     # Custom exception handling
│   │── logger.py        # Logging configuration
│   │── utils.py         # Utility functions
│
│── templates/           # HTML templates for Flask app
│   │── index.html       # Home page (UI for predictions)
│   │── home.html        # Additional UI template
│
│── app.py               # Flask API (To Be Deployed)
│── requirements.txt     # Python dependencies
│── setup.py             # Package setup file
│── README.md            # Project documentation (this file)
│── .gitignore           # Git ignore file
```

## ⚙️ Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction
```
### **2️⃣ Create a Virtual Environment** (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On MacOS/Linux
venv\Scripts\activate     # On Windows
```
### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```
### **4️⃣ Run the Flask App** (Coming Soon)
```sh
python app.py
```

## 🏆 Model Performance
- **Best Model:** AdaBoostClassifier
- **Accuracy:** 66.85%
- **ROC-AUC Score:** 0.83

## 🛠 Future Updates
- ✅ Improve class imbalance handling using SMOTE
- ✅ Optimize hyperparameters using Bayesian Optimization
- 🔜 Deploy Flask Web App (Coming Soon)
- 🔜 Add API documentation using Swagger

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## 📜 License
This project is open-source and available under the **MIT License**.

## ✉️ Contact
**Muhammad Waqas**  
📧 waqasliaqat630@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/muhammad-waqas)

