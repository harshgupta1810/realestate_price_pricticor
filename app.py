import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import json
from sklearn.linear_model import LinearRegression
lr_clf = LinearRegression()



st.title('Real Estate Price Predition ')
data = pickle.load(open('banglore_home_prices_model.pkl','rb'))
def predict_price(locations,sqft,bath,bhk):
    loc_index = np.where(locations==location)[0][0]

    x = np.zeros(len(data))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return lr_clf.predict([x])[0]

location = st.text_input('your location', '1st Phase JP Nagar')
st.write('your location is', location)
sqrt = st.number_input('your carpet area is ')
st.write('total carpet area ', sqrt)
bath = st.number_input('total bathroom')
bath = int(bath)
st.write('total bathroom ', bath)
bhk = st.number_input('total bhk')
bhk = int(bhk)
st.write('total bhk ', bhk)

if st.button('predict'):
    predict_price(location, sqrt, bhk, bath)
else:
    st.write('Goodbye')