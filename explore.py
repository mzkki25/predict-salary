import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    df = pd.read_csv("survey_results_public_preprocessing.csv")
    return df

df = load_data()

def show_explore_page():
    st.title("Eksplorasi penggajian")
    
    st.write("""###Total penggajian berdasarkan negara""")
    data = df.groupby(['Country'])['Salary'].sum().sort_values(ascending=True)
    st.bar_chart(data)
    
    st.write("""###Total penggajian berdasarkan pengalaman""")
    data = df.groupby(['YearsCodePro'])['Salary'].sum().sort_values(ascending=True)
    st.bar_chart(data)
    