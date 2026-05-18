import pandas as pd
import numpy as np
import streamlit as st

st.markdown("""
            
            <h1 style="text-align:center;"> Describe & Visualize Data </h1>
            
            """,unsafe_allow_html=True)

st.markdown("""
            
            <h3 style="" > Upload Data Below ⬇️ </h3>
            
            
            """,unsafe_allow_html=True)

data=st.file_uploader("",type=["csv","xlsx"])
if data :
    data=pd.read_csv(data)

    st.write("---")

    correct_cols=list(data.select_dtypes(include=["str","number"]).columns)
    data=data.fillna(data.mean())

    data=data[correct_cols]

    st.write(data.describe())
    st.write("---")
    
    st.markdown("""
            
            <h3>Groupby Specific Feature</h3>    
                
                """,unsafe_allow_html=True)
    
    
    group_cols=[]
    for c in correct_cols:
        
        if len(data[c].unique()) <=6 :
            
            group_cols.append(c)
    
    if len(group_cols) == 0:
        st.info("Columns have too much values to group by it")
        
    else:
        st.markdown("""
                    
              <h5>Choose the column which will be grouped according to it </h5>      
                    """,unsafe_allow_html=True)
        choosen_group=st.selectbox("",options=group_cols)
        st.markdown("""
                    
              <h5>Choose the operation on the data </h5>      
                    """,unsafe_allow_html=True)
        choosen_operation=st.multiselect("",options=["Mean","Median"])
        st.markdown("""
                    
              <h5>Choose the columns which you want to implement the operation on them </h5>      
                    """,unsafe_allow_html=True)
        correct_cols.remove(choosen_group)
        operation_cols=st.multiselect("",options=correct_cols)
        
        if choosen_operation=="Main":
            group_data=data.groupby(choosen_group)
            st.write(group_data[operation_cols].mean())
            
        if choosen_operation=="Median":
            group_data=data.groupby(choosen_group)
            st.write(group_data[operation_cols].median())
        
    st.write("---")
    
    st.markdown("""
              
              <h2>Graphs</h2>  
                
                """,unsafe_allow_html=True)
    
    st.write("---")
    
    st.markdown("""
              
              <h5>Choose the type of the graph</h5>  
                
                """,unsafe_allow_html=True)
    
    tab1,tab2=st.tabs(["Numerical Graphs","Categorical Graphs"])
    
    with tab1:
        st.subheader("Welcome to present your numerical graphs")
        graph_type=st.selectbox("",options=["Scatter","Line","Box Plot","Hist"])
        
        numerical_cols=list(data.select_dtypes(include="number").columns)
        
        if graph_type == "Scatter":
            
            x_axis=st.selectbox("Choose The Column On X-axis",options=numerical_cols)
            y_axis=st.selectbox("Choose The Column On Y-axis",options=numerical_cols)
            
            
    with tab2:
        st.header("")
        st.selectbox("",options=[])
        
    
    
    