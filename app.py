import streamlit as st

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="💖",
    layout="wide"
)

import pickle as pkl
import pandas as pd

# Load the saved model and preprocessor
@st.cache_data
def load_model():
    with open("artifacts/preprocessor.pkl", "rb") as file:
        preprocessor = pkl.load(file)

    model = pkl.load(open("artifacts/model.pkl", "rb"))
    return preprocessor, model

preprocessor, model = load_model()

# ===================== 🎨 PAGE STYLING 🎨 =====================


# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stButton>button {
            background-color: #d63384;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            width: 100%;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #c2185b;
            color: white;
        }
        .stSidebar {
            background-color: #e3f2fd;
        }
        [data-testid="stSidebar"] h2, [data-testid="stSidebar"] label, [data-testid="stSidebar"] div {
            color: #a10e48 !important;
            font-weight: bold;
        }
        .stMarkdown h1 {
            color: #c2185b;
        }
    </style>
""", unsafe_allow_html=True)

# ===================== 🌟 APP TITLE & HEADER 🌟 =====================
st.markdown("<h1 style='text-align: center; color: #d63384;'>💖 Heart Disease Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Predict heart disease severity with AI!</h3>", unsafe_allow_html=True)

st.write("🔎 Enter the patient details in the sidebar to get a prediction.")

# ===================== 📝 USER INPUT SIDEBAR =====================
with st.sidebar:
    st.markdown("<h2 style='color:#c2185b;'>📋 Patient Information</h2>", unsafe_allow_html=True)
    
    age = st.slider("Age", 18, 100, 50)
    sex = st.radio("Sex", ["Male", "Female"])
    dataset = st.selectbox("Dataset", ["Cleveland", "Hungary", "Switzerland", "VA Long Beach"])
    cp = st.selectbox("Chest Pain Type", ["typical angina", "atypical angina", "non-anginal", "asymptomatic"])
    trestbps = st.slider("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    chol = st.slider("Serum Cholesterol (mg/dL)", 100, 600, 200)
    fbs = st.radio("Fasting Blood Sugar > 120 mg/dL", [True, False])
    restecg = st.selectbox("Resting ECG", ["normal", "stt abnormality", "lv hypertrophy"])
    thalch = st.slider("Max Heart Rate Achieved", 60, 202, 140)
    exang = st.radio("Exercise-Induced Angina", [True, False])
    oldpeak = st.slider("ST Depression Induced by Exercise", -2.6, 6.2, 1.0)
    slope = st.selectbox("Slope of Peak Exercise ST Segment", ["downsloping", "flat", "upsloping"])
    ca = st.slider("Number of Major Vessels", 0, 3, 1)
    thal = st.selectbox("Thalassemia", ["normal", "fixed defect", "reversible defect"])
    stress_level = st.selectbox("Stress Level", ["typical angina_hi", "asymptomatic_hi", "asymptomatic_lo", "no anginal_medium", "atypical angina_medium"])

# Convert boolean values to strings
fbs = "Yes" if fbs else "No"
exang = "Yes" if exang else "No"

# ===================== 📊 PREDICTION SECTION =====================
col1, col2, col3 = st.columns([1, 2, 1])  # Center align the button

with col2:
    if st.button("🔮 Predict Heart Disease Severity"):
        # Create DataFrame with the same column order used during training
        user_input = pd.DataFrame({
            "age": [age], "sex": [sex], "dataset": [dataset], "cp": [cp], "trestbps": [trestbps], 
            "chol": [chol], "fbs": [fbs], "restecg": [restecg], "thalch": [thalch], "exang": [exang], 
            "oldpeak": [oldpeak], "slope": [slope], "ca": [ca], "thal": [thal], "stress_level": [stress_level]
        })

        # Apply the saved preprocessor (ColumnTransformer)
        transformed_input = preprocessor.transform(user_input)

        # Convert the transformed NumPy array back to DataFrame
        transformed_input_df = pd.DataFrame(transformed_input)

        # Make Prediction
        prediction = model.predict(transformed_input_df)

        # ===================== 🎯 DISPLAY RESULTS =====================
        st.markdown("<h2 style='text-align: center; color: #d63384;'>🔍 Prediction Result</h2>", unsafe_allow_html=True)

        severity_dict = {
            0: "No Heart Disease (Safe)",
            1: "Mild Heart Disease",
            2: "Moderate Heart Disease",
            3: "Severe Heart Disease",
            4: "Critical Condition - Immediate Attention Needed!"
        }

        result = severity_dict[prediction[0]]

        if prediction[0] == 0:
            st.success(f"✅ {result}")
        else:
            st.error(f"⚠️ {result}")
