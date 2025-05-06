# streamlit_app.py
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load iris data + train model
iris = load_iris()
X, y = iris.data, iris.target
model = RandomForestClassifier().fit(X, y)

st.title("🌸 Iris Flower Classifier")

# Input sliders
sepal_length = st.slider('Sepal length (cm)', 4.0, 8.0, 5.1)
sepal_width = st.slider('Sepal width (cm)', 2.0, 4.5, 3.5)
petal_length = st.slider('Petal length (cm)', 1.0, 7.0, 1.4)
petal_width = st.slider('Petal width (cm)', 0.1, 2.5, 0.2)

# Predict button
if st.button("Predict"):
    sample = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(sample)
    pred_class = iris.target_names[prediction][0]
    st.success(f"🌟 Predicted class: {pred_class}")
