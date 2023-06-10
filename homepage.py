import streamlit as st

def show_homepage():
    st.title("Salary Prediction App")
    st.write(
        """
        This app predicts the **Salary** of an employee!
        """
    )
    
    st.divider()
    
    # Membuat tabel pada streamlit
    value = {
        'Nama': ['Akmal Muzakki Bakir', 'Namira Salsabilla', 'Haura Adzkia Delfina'],
        'NIM' : ['1305210087', '1305210091', '1305213006']
    }
    
    st.table(value)