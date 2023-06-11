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
    
    chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
            'HexagonLayer',
            data=chart_data,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))