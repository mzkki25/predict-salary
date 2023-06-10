import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    df = pd.read_csv("survey_results_public_clean.csv")
    return df

df = load_data()

def show_explore_page():
    st.title("Salary Explorer")
    
    st.write("""### Sum of salary based on country""")
    data = df.groupby(['Country'])['Salary'].sum().sort_values(ascending=False)
    st.bar_chart(data)
    
    st.write("""### Mean salary based on experience""")
    data = df.groupby(['YearsCodePro'])['Salary'].mean().sort_values(ascending=False)
    st.bar_chart(data)
    