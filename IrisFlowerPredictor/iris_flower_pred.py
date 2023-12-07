import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Iris Flower Prediction App

This app lets you predict the Iris flower type!

""")

st.sidebar.header('User Input Features')


def user_input():
    sepal_length = st.sidebar.slider('Sepal Length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal Length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 0.2)
    data = {'Sepal Length': sepal_length,
            'Sepal Width': sepal_width,
            'Petal Length': petal_length,
            'Petal Width': petal_width}
    features = pd.DataFrame(data, index = [0])
    return features


df = user_input()

st.subheader('User Input Parameter')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_prob = clf.predict_proba(df)

st.subheader('Class Label and their corresponding index number')
# st.write(iris.target_names)
st.image('dataset_classification.png', caption= 'Target Names')

st.subheader('Prediction')
st.write(iris.target_names[prediction])

# st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_prob)

