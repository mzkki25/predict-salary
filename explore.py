import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pydeck as pdk

@st.cache
def load_data():
    df = pd.read_csv("survey_results_public_preprocessing.csv")
    return df

df = load_data()

def show_explore_page():
    st.title("Eksplorasi penggajian")
    
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
    
    # Ambil data country dengan salary untuk di eksprot ke pydeck
    
    # chart_data = pd.DataFrame(
    #     df[['Country', 'Salary']],
    #     columns=['Country', 'Salary']
    # )

    # st.pydeck_chart(pdk.Deck(
    #     map_style=None,
    #     initial_view_state=pdk.ViewState(
    #         latitude=0,
    #         longitude=0,
    #         zoom=11,
    #         pitch=50,
    #     ),
    #     layers=[
    #         pdk.Layer(
    #             'ScatterplotLayer',
    #             data=chart_data,
    #             get_position='[Salary, Country]',
    #             get_color='[200, 30, 0, 160]',
    #             get_radius=200,
    #         ),
    #     ],
    # ))
    
    dataq = {'Country': ['USA', 'China', 'Japan', 'Germany', 'India'],
        'Salary': [5000, 4000, 3000, 2000, 1000]}

    df = pd.DataFrame(dataq)

    # Mengurutkan DataFrame berdasarkan kolom 'Salary' secara menurun
    df_sorted = df.sort_values('Salary', ascending=False)

    # Mengatur skala warna

    # Mengubah nilai warna menjadi format RGBA
    rgba_color = df_sorted['Salary'].apply(lambda x: [200, 30, 0, int((x/df_sorted['Salary'].max()) * 255)])

    # Membuat chart data
    chart_data = pd.DataFrame(
        {'Country': df_sorted['Country'], 'Salary': df_sorted['Salary'], 'rgba_color': rgba_color}
    )

    # Menampilkan ScatterplotLayer menggunakan PyDeck
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=0,
            longitude=0,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[Salary, 0]',
                get_color='rgba_color',
                get_radius=200,
                opacity=0.8,
                pickable=True,
            ),
        ],
    ))