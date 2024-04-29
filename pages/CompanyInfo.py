import streamlit as st 
import vnstock as vs
import pandas as pd

st.header("Company Infomations")

# get data
cp_df = vs.listing_companies(live=True)
cp_list_name = cp_df['organName'].tolist()
cp_ticker = cp_df['ticker'].tolist()


col1, col2= st.columns(2)

with col1:
    option_ticket = st.selectbox('Ticker: ',cp_ticker)

st.write(vs.company_profile(option_ticket))
