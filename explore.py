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
    
    opsi1 = [
        'Country',
        'YearsCodePro',
        'EdLevel',
        'Employment',
    ]
    
    pilihan1 = st.selectbox("Pilih atribut untuk menghitung opsi yang dipilih berdasarkan salary", opsi1)

    col1, col2 = st.columns(2)

    if col1.button("Tampilkan data", key=1):
        col2.empty()
        st.divider()
        st.write(f"""Total penggajian berdasarkan {pilihan1} dengan Salary""")
        data = df.groupby([pilihan1])['Salary'].sum().sort_values(ascending=True)
        st.bar_chart(data)

    if col2.button("Bersihkan output", key=1.5):
        col1.empty()
        col2.empty()

    
    st.divider()
    
    opsi2 = [
        'Australia', 
        'Brazil', 
        'Canada',
        'France',
        'Germany',
        'India',
        'Italy',
        'Netherlands',
        'Other',
        'Poland',
        'Spain',
        'Sweden',
        'United Kingdom of Great Britain and Northern Ireland',
        'United States of America'
    ]
    
    pilihan2 = st.selectbox("Pilih negara untuk menghitung opsi yang dipilih berdasarkan salary", opsi2)
    
    if st.button("Tampilkan data", key=2):
        st.divider()
        st.write(f"""Menampilkan negara {pilihan2} dengan 5 Salary tertinggi""")
        data = df[df['Country'] == pilihan2].sort_values(by='Salary', ascending=False).head(5)
        # Buatlah ke dalam dataframe
        table_data = pd.DataFrame({'Salary': data['Salary']})
        st.table(table_data)
    if st.button("Bersihkan output", key=2.5):
        st.empty()
        