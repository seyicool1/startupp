import streamlit as st
import numpy as py
# import matplotlib.pyplot as pyplot
import pandas as pd
!pip install joblib
import joblib
from sklearn.linear_model import LinearRegression

data = pd.read_csv('https://raw.githubusercontent.com/arib168/data/main/50_Startups.csv')
data.to_csv('startup.csv')

st.markdown("<br>", unsafe_allow_html= True)


st.markdown("<h1 style = 'color: #40A2E3; text-align: center; font-family: helvetica '>STARTUP PROJECT</h1>", unsafe_allow_html=True)
st.markdown("<h4 style = 'margin: -30px; color: #59B4C3; text-align: center; font-family: cursive '>Built By GomyCode MTW</h4>", unsafe_allow_html=True)

st.image('pngwing.com.png')

# st.write('By analyzing a diverse set of parameters, including Market Expense, Administrative Expense, and Research and Development Spending, our team seeks to develop a robust predictive model that can offer valuable insights into the future financial performance of startups. This initiative not only empowers investors and stakeholders to make data-driven decisions but also provides aspiring entrepreneurs with a comprehensive framework to evaluate the viability of their business models and refine their strategies for long-term success')


st.markdown("<p style = 'font-family: cursive' >By analyzing a diverse set of parameters, including Market Expense, Administrative Expense, and Research and Development Spending, our team seeks to develop a robust predictive model that can offer valuable insights into the future financial performance of startups. This initiative not only empowers investors and stakeholders to make data-driven decisions but also provides aspiring entrepreneurs with a comprehensive framework to evaluate the viability of their business models and refine their strategies for long-term success</p>", unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html= True)
st.markdown('<br>', unsafe_allow_html= True)

st.markdown('<br>', unsafe_allow_html= True)
st.dataframe(data, use_container_width= True)

st.sidebar.image('user.png', caption = 'welcome User')

st.sidebar.write('Feature Input')
rd_spend = st.sidebar.number_input('Research and Development Expense', data['R&D Spend'].min(), data['R&D Spend'].max()+ 10000)
admin = st.sidebar.number_input('Administrative Expense', data['Administration'].min(), data['Administration'].max()+ 10000)
mkt_spend = st.sidebar.number_input('Marketing Expense', data['Marketing Spend'].min(), data['Marketing Spend'].max()+10000)

st.markdown("<br>", unsafe_allow_html= True)
st.write('Input Variables')
input_var = pd.DataFrame({'R&D Spend': [rd_spend], 'Administration': [admin], 'Marketing Spend': [mkt_spend]})
st.dataframe(input_var)

model = joblib.load('startUpmode.pkl')

predictor = st.button('Predict Profit')
if predictor:
    prediction = model.predict(input_var)
    st.success(f'The Predicted value for nyour company is{prediction}')
    st.balloons()
