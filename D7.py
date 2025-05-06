pip install streamlit scikit-learn pandas numpy matplotlib seaborn

# app.py

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# App Title
st.title('🌸 Iris Flower Classifier Dashboard')

# Sidebar Inputs
st.sidebar.header('User Input Features')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length (cm)', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width (cm)', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length (cm)', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width (cm)', 0.1, 2.5, 0.2)
    data = {
        'sepal length (cm)': sepal_length,
        'sepal width (cm)': sepal_width,
        'petal length (cm)': petal_length,
        'petal width (cm)': petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Load Iris dataset
iris = load_iris()
X = iris.data
Y = iris.target

# Train Model
model = RandomForestClassifier()
model.fit(X, Y)

# Predict
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

# Output
st.subheader('User Input Features')
st.write(input_df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
st.write('Prediction Probability:', prediction_proba)

# Display dataset
st.subheader('Iris Dataset Preview')
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
st.write(df)
