import streamlit as st

def show_homepage():
    st.title("Aplikasi prediksi penggajian")
    st.write(
        """
        Aplikasi ini digunakan untuk memprediksi gaji anda ketika melamar kerja di perusahaan **KELOMPOK 3**!
        """
    )
    
    st.divider()
    
    # Membuat tabel pada streamlit
    value = {
        '**Nama**': ['Akmal Muzakki Bakir', 'Namira Salsabilla', 'Haura Adzkia Delfina'],
        '**NIM**' : ['1305210087', '1305210091', '1305213006']
    }
    
    st.table(value)