import streamlit as st

def show_homepage():
    st.title("Aplikasi prediksi penggajian")
    st.write(
        """
        Aplikasi ini digunakan untuk memprediksi gaji anda ketika melamar kerja di perusahaan **KELOMPOK 3**!
        """
    )
    
    st.divider()
    
    value = {
        'Nama': ['Akmal Muzakki Bakir', 'Namira Salsabilla', 'Haura Adzkia Delfina'],
        'NIM' : ['1305210087', '1305210091', '1305213006']
    }
    st.table(value)
    
    st.divider()
    
    # st.text_area("Deskripsi singkat", "")
    
    st.write(
        """
        Aplikasi penggajian karyawan ini dibuat oleh **KELOMPOK 3** untuk memenuhi tugas akhir mata kuliah **Perancangan Aplikasi Untuk Sains Data**.
        Aplikasi penggajian ini bekerja dengan memanfaatkan model machine learning yang telah dilatih sebelumnya. dengan menggunakan 7 atribut yaitu:
        - Country
        - Employment
        - EdLevel
        - YearsCodePro
        - Job Title
        - Gender
        - Salary
        
        dengan atribut salary sebagai target.
        """
    )