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
    
    st.write("""### Pratinjau Data""")
    # Menampilkan data
    st.table(df.head(10))
    
    st.divider()
    st.divider()
    
    
    # Bagian 1
    opsi1 = [
        'Country',
        'EdLevel',
        'Employment',
        'Job Title',
        'Gender',
    ]
    
    pilihan1 = st.selectbox("Pilih atribut untuk menghitung opsi yang dipilih berdasarkan salary", opsi1)

    col1, col2 = st.columns(2)

    if col1.button("Tampilkan data", key=1):
        col2.empty()
        st.divider()
        st.write(f"""Total penggajian berdasarkan {pilihan1} dengan Salary""")
        data = df.groupby([pilihan1])['Salary'].sum().sort_values(ascending=True)
        st.bar_chart(data)

    if col2.button("Bersihkan output", key=2):
        col1.empty()
        col2.empty()

    
    st.divider()
    
    # Bagian 2
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
        'United Kingdom of Great Britain and Northern Ireland',
        'United States of America'
    ]
    
    pilihan2 = st.selectbox("Pilih negara untuk menghitung opsi yang dipilih berdasarkan salary", opsi2)

    col3, col4 = st.columns(2)

    if col3.button("Tampilkan data", key=3):
        col4.empty()
        st.divider()
        st.write(f"""Menampilkan negara {pilihan2} dengan 5 Salary tertinggi""")
        data = df[df['Country'] == pilihan2].sort_values(by='Salary', ascending=False).head(5)
        table_data = pd.DataFrame({'Salary': data['Salary']})
        st.table(table_data)

    if col4.button("Bersihkan output", key=4):
        col3.empty()
        col4.empty()

        
    # Bagian 3
    opsi3 = [
        'Associate',
        'Bachelor',
        'Doctoral',
        'Master',
        'Other degree',
        'Primary school',
        'Professional',
        'Secondary school'
    ]
    
    pilihan3 = st.selectbox("Pilih tingkat edukasi untuk menghitung opsi yang dipilih berdasarkan salary", opsi3)

    col5, col6 = st.columns(2)

    if col5.button("Tampilkan data", key=5):
        col6.empty()
        st.divider()
        st.write(f"""Menampilkan  {pilihan3} dengan 5 Salary tertinggi""")
        data = df[df['EdLevel'] == pilihan3].sort_values(by='Salary', ascending=False).head(5)
        table_data = pd.DataFrame({'Salary': data['Salary']})
        st.table(table_data)

    if col6.button("Bersihkan output", key=6):
        col5.empty()
        col6.empty()
        
    # Bagian 4
    opsi4 = [
        'Junior Business Analyst',
        'Junior Business Development Associate',
        'Junior Financial Analyst',
        'Junior Marketing Coordinator',
        'Junior Marketing Manager',
        'Junior Marketing Specialist',
        'Junior Operations Analyst',
        'Junior Sales Representative',
        'Other',
        'Senior Business Analyst',
        'Senior Financial Analyst',
        'Senior Operations Manager',
        'Senior Product Manager'
    ]
    
    pilihan4 = st.selectbox("Pilih pekerjaan untuk menghitung opsi yang dipilih berdasarkan salary", opsi4)
    
    col7, col8 = st.columns(2)
    
    if col7.button("Tampilkan data", key=7):
        col8.empty()
        st.divider()
        st.write(f"""Menampilkan  {pilihan4} dengan 5 Salary tertinggi""")
        data = df[df['Job Title'] == pilihan4].sort_values(by='Salary', ascending=False).head(5)
        table_data = pd.DataFrame({'Salary': data['Salary']})
        st.table(table_data)
    
    if col8.button("Bersihkan output", key=8):
        col7.empty()
        col8.empty()
        
    opsi5 = [
        'Country',
        'EdLevel',
        'Employment',
        'Job Title',
        'Gender',
    ]

    st.divider()

    # Bagian 5
    df2 = df.nlargest(5, 'Salary')
    pilihan5 = st.selectbox("Pilih atribut untuk menampilkan opsi dengan 5 gaji tertinggi", opsi5)

    col9, col10 = st.columns(2)

    if col9.button("Tampilkan data", key=9):
        col10.empty()
        st.divider()
        st.write(f"Menampilkan 5 {pilihan5} dengan gaji tertinggi")

        if pilihan5 == 'Country':
            table_data = df2[['Country', 'Salary']].reset_index(drop=True)
            st.table(table_data)
        elif pilihan5 == 'EdLevel':
            table_data = df2[['EdLevel', 'Salary']].reset_index(drop=True)
            st.table(table_data)
        elif pilihan5 == 'Employment':
            table_data = df2[['Employment', 'Salary']].reset_index(drop=True)
            st.table(table_data)
        elif pilihan5 == 'Job Title':
            table_data = df2[['JobTitle', 'Salary']].reset_index(drop=True)
            st.table(table_data)
        elif pilihan5 == 'Gender':
            table_data = df2[['Gender', 'Salary']].reset_index(drop=True)
            st.table(table_data)

    if col10.button("Bersihkan output", key=10):
        col9.empty()
        col10.empty()

                