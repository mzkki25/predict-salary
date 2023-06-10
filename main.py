import streamlit as st
import pandas as pd
from predict import show_predict_page
from explore import show_explore_page

page = st.sidebar.selectbox("Choose a page", ["Homepage", "Salary Prediction", "Data Exploration"])

if page == "Homepage":
    st.title("Salary Prediction App")
    st.write(
        """
        This app predicts the **Salary** of an employee!
        """
    )
elif page == "Data Exploration":
    show_explore_page()
else:
    show_predict_page()