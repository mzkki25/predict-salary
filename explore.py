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
    
    opsi = [
        'Country',
        'YearsCodePro',
        'EdLevel',
        'Employment',
    ]
    
    pilihan = st.selectbox("Pilih atribut", opsi)
    
    # Button untuk menampilkan data
    if st.button("Tampilkan data"):
        st.write(f"""Total penggajian berdasarkan {pilihan} dengan Salary""")
        data = df.groupby([pilihan])['Salary'].sum().sort_values(ascending=True)
        st.bar_chart(data)
    