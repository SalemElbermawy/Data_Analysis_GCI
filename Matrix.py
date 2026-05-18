# mathmatical operation on arrays
# all possible operations
import streamlit as st 
import pandas as pd
import numpy as np

st.set_page_config(page_title="Matrix_Operation",page_icon="🧮")

st.markdown("""
            
            <h1 style="text-align:center; background-color:black; border-radius:20px;">Matrix Calculation 🧮</h1>
            
            """,unsafe_allow_html=True)
st.write("---")

st.markdown("""
            
          <h3 style="color:red; text-align:center;">Math Is Very Simple</h3>  
            
            """,unsafe_allow_html=True)
st.write("---")


st.markdown("""
         
         <ul style="color:cyan; background:black; border-radius:23px; padding:30px; text-align:center; margin:auto; width:250px; ">
         
         <li >Addition ➕</li>
         <li >Substraction ➖</li>
         <li >Multiblication ✖️</li>
         <li >Division ➗</li>
         <li >Dot Product 🧮</li>
         
         </ul>   
            
            """,unsafe_allow_html=True)

st.write("---")


shape_a=st.selectbox(label="Choose The Shape Of The Matrix (A)",options=["1×1","1×2","1×3","2×1","2×2","2×3","3×1","3×2","3×3"])
shape_b=st.selectbox(label="Choose The Shape Of The Matrix (B)",options=["1×1","1×2","1×3","2×1","2×2","2×3","3×1","3×2","3×3"])

rows,cols =map(int,shape_a.split("×"))

st.write("Enter Matrix A: ")

matrix_a=[]

for i in range(rows):
    
    cols_ui=st.columns(cols)
    
    row=[]
    
    for j in range(cols):
        val= cols_ui[j].number_input(label=f"{i}{j}",key=f"A_{i}_{j}",value=0)
        
        row.append(val)
    matrix_a.append(row)


matrix_a=np.array(matrix_a)
st.write("---")

st.write("Matrix A:")
st.write(matrix_a)




st.write("---")


rows_2,cols_2 =map(int,shape_b.split("×"))

st.write("Enter Matrix B: ")

matrix_b=[]

for i in range(rows_2):
    
    cols_ui=st.columns(cols_2)
    
    row=[]
    
    for j in range(cols_2):
        val= cols_ui[j].number_input(label=f"{i}{j}",key=f"B_{i}_{j}",value=0)
        
        row.append(val)
    matrix_b.append(row)


matrix_b=np.array(matrix_b)
st.write("---")
st.write("Matrix B:")
st.write(matrix_b)
st.write("---")


# box of operations 
# T , inv , det 

operation=st.selectbox("Choose Operation",options=["Addition","Substraction","Multiplying","Division","Dot","Transpose","Inverse","DET"])
st.write("---")

# presenting result
try:
    if operation == "Addition":
        st.write(matrix_a + matrix_b)
    
    elif operation == "Substraction":
        st.write(matrix_a - matrix_b)
    
    elif operation == "Multiplying":
        st.write(matrix_a * matrix_b)
        
    elif operation == "Division":
        st.write(matrix_a / matrix_b)
    
    elif operation == "Dot":
        st.write(np.dot(matrix_a , matrix_b))
    elif operation == "Inverse":
        a=np.linalg.inv(matrix_a)
        b=np.linalg.inv(matrix_b)
        st.write("Matrix A : ")
        st.write(a)
        st.write("---")
        st.write("Matrix B : ")
        st.write(b)
        st.write("---")
        
    elif operation == "DET":
        st.write("Matrix A : ")
        st.write(np.linalg.det(matrix_a))
        st.write("---")
        st.write("Matrix B : ")
        st.write(np.linalg.det(matrix_b))
        
    elif operation == "Transpose":
        st.write("Matrix A :")
        st.write(matrix_a.T)
        st.write("---")
        st.write("Matrix B : ")
        st.write(matrix_b.T)
        
    
    
except:
    st.warning("Please Check The Shape")
