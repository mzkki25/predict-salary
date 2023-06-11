import streamlit as st
import pandas as pd
from predict import show_predict_page
from explore import show_explore_page
from homepage import show_homepage

page = st.sidebar.selectbox("Pilih laman", ["Homepage", "Salary Prediction", "Data Exploration"])

if page == "Homepage":
    show_homepage()
elif page == "Data Exploration":
    show_explore_page()
else:
    show_predict_page()