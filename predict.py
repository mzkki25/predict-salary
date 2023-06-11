import pandas as pd
import streamlit as st
import pickle
import numpy as np
import torch
from torch import nn

COUNTRIES = [
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

EDUCATION = [
    'Associate',
    'Bachelor',
    'Doctoral',
    'Master',
    'Other degree',
    'Primary school',
    'Professional',
    'Secondary school'
    ]

EMPLOYMENT = [
    'freelancer',
    'full-time',
    'part-time'
]

JOB = [
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

GENDER = [
    'Female',
    'Male'
]

class SalaryPredict(nn.Module):
    def __init__(self, n_input_featrues):
        super().__init__()
        self.l1 = nn.Linear(n_input_featrues, 128)
        self.relu1 = nn.ReLU()
        self.l2 = nn.Linear(128, 64)
        self.relu2 = nn.ReLU()
        self.l3 = nn.Linear(64, 32)
        self.relu3 = nn.LeakyReLU()
        self.l4 = nn.Linear(32, 16)
        self.relu4 = nn.LeakyReLU()
        self.l5 = nn.Linear(16, 8)
        self.relu5 = nn.LeakyReLU()
        self.l6 = nn.Linear(8, 1)
        self.dropout = nn.Dropout(p=0.1)
        
    def forward(self, x):
        x = self.l1(x)
        x = self.relu1(x)
        x = self.dropout(x)
        x = self.l2(x)
        x = self.relu2(x)
        x = self.dropout(x)
        x = self.l3(x)
        x = self.relu3(x)
        x = self.dropout(x)
        x = self.l4(x)
        x = self.relu4(x)
        x = self.dropout(x)
        x = self.l5(x)
        x = self.relu5(x)
        x = self.dropout(x)
        x = self.l6(x)
        return x

def load_model(pytorch_model=SalaryPredict):
    with open('model.pkl', 'rb') as f:
        data = pickle.load(f)
        
    loader = torch.load('model.pt')
    model = pytorch_model(data['n_input'])
    model.load_state_dict(loader['Model'])
    data['pytorch_model'] = model
    return data

def show_predict_page():
    st.title('Prediksi penggajian')
    st.write("""### Kami membutuhkan beberapa informasi untuk memprediksi gaji Anda!""")
    st.divider()
    
    country = st.selectbox('Negara', COUNTRIES)
    education = st.selectbox('Pendidikan', EDUCATION)
    employment = st.selectbox('Status pekerjaan', EMPLOYMENT)
    job = st.selectbox('Pekerjaan', JOB)
    gender = st.selectbox("Jenis kelamin", GENDER)
    experience = st.slider('Pengalaman (dalam tahun)', 0, 25, 1)
    
    ok = st.button('Hitung prediksi gaji Anda')
    if ok:
        params = np.array([[country, education, employment, job, gender, experience]])
        st.table(pd.DataFrame(params, columns=['Negara', 'Pendidikan', 'Status pekerjaan', 'Pekerjaan', 'Jenis Kelamin', 'Pengalaman (dalam tahun)']))
        
        params[:, 0] =  country_encoder.transform(params[:, 0])
        params[:, 1] =  education_encoder.transform(params[:, 1])
        params[:, 2] =  employment_encoder.transform(params[:, 2])
        params[:, 3] =  job_encoder.transform(params[:, 3])
        params[:, 4] =  gender_encoder.transform(params[:, 4])
        params = params.astype(np.float32)
        
        st.divider()
        st.subheader('Prediksi penggajian berdasarkan berbagai model')
        
        linear_predict = round(linear.predict(params)[0], 2)
        decission_predict = round(decission.predict(params)[0], 2)
        # random_predict = round(random.predict(params)[0], 2)
        neural_predict = round(neural(torch.from_numpy(params)).item(), 2)
        
        st.table(pd.DataFrame([linear_predict, decission_predict, neural_predict], 
                                columns=['Prediksi Penggajian'],
                                index=['Linear Regression', 'Decission Tree', 'Neural Network']))
        st.write(f"Prediksi gaji Anda adalah sekitar: ${round(np.mean([linear_predict, decission_predict, neural_predict]), 2)} per-tahun")
        
data = load_model()
linear = data['LinearRegression']
decission = data['DecissionTree']
# random = data['RandomForest']
neural = data['pytorch_model']
country_encoder = data['country_encoder']
education_encoder = data['ed_encoder']
employment_encoder = data['employment_encoder']
job_encoder = data['job_encoder']
gender_encoder = data['gender_encoder']