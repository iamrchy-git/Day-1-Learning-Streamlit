import yfinance as yf
import streamlit as st
import pandas as pd

st.write(""" 
# Simple Stock Price App
 Shown are the stock **closing price** and ***volume***of Google!
 
""")
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1f17e75

# define the ticket symbol
tickerSymbol = 'GOOGL'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
tickerDf = tickerData.history(start='2010-5-31',end='2020-5-31')

# Open high low close volume Dividends Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)