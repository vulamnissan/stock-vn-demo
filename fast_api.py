from vnstock import * 
import streamlit as st

df =  stock_intraday_data(symbol='TCB', 
                            page_size=500, investor_segment=True)
# print(df)
st.write(df)
