import yfinance as yfinance
import pandas as pd
import streamlit as st

st.write("""
# Stock Price

* NYSE:EPAM from 2010-1-1 to 2024-1-12
    - closing price
    - volume
""")

tickerSymbol = "EPAM"
tickerData = yfinance.Ticker(tickerSymbol)
tickerDf = tickerData.history(period="1d", start="2010-1-1", end="2024-1-12")


st.line_chart(tickerDf.Close)

st.line_chart(tickerDf.Volume)