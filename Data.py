import streamlit as st
import pandas as pd
import numpy as np


st.markdown("""
            
            <h1 style="text-align:center; background-color:black; border-radius:20px;">Analyze Data Here</h1>
            
            
            """,unsafe_allow_html=True)



st.write("---")

st.markdown("""
            
            <h3 style="" > Upload Data Below ⬇️ </h3>
            
            
            """,unsafe_allow_html=True)
data=st.file_uploader("",type=["csv","xlsx"])

st.write("---")

if data:
    data=pd.read_csv(data)
    
    r=st.slider("Choose the number of rows",max_value=data.shape[0]+1,min_value=1,value=5)
    st.write("---")
    c=st.multiselect("Choose Particular Cols",options=data.columns,default=data.columns)
    st.write("---")
    st.write(data.loc[:r,c])
    st.write("---")
    st.title("Grouped Data")
    st.write("---")
    st.write("Choose Columns of Statistics Grouped")
    
    stat_cols_group=st.multiselect("",options=data.select_dtypes(include="number").columns)
    
    for i in stat_cols_group:
        try:
            st.write(data.groupby([i]).mean())
        except:
            st.warning("Maybe there is problem in the so much feature in the columns")