import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import yfinance as yf
import streamlit as st


tickers=["SOL-USD"]
start="2021-01-01"
end="2023-04-12"
df = yf.download(tickers,group_by=tickers)
df.head()

st.title('Stock Trend Prediction')
user_input = st.text_input('Enter Stock Ticker', 'AAPL')
df = data.DataReader(user_input,'yahoo',start,end)
st.subheader('Data from 2021 - 2023')
st.write(df.describe())
