import streamlit as st
import pandas as pd
from predict import show_predict_page

page = st.sidebar.selectbox("Choose a page", ["Homepage", "Salary Prediction"])

if page == "Homepage":
    st.title("Salary Prediction App")
    st.write(
        """
        This app predicts the **Salary** of an employee!
        """
    )
else:
    show_predict_page()