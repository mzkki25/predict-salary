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
    'Sweden',
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
    'Independent contractor',
    'freelancer',
    'full-time',
    'part-time',
    'self-employed'
]

# Membuat class SalaryPredict dengan menggunakan nn.Module
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
        
    loader = torch.load('model_15k.pt')
    model = pytorch_model(loader['n_input_features'])
    model.load_state_dict(loader['model'])
    data['pytorch_model'] = model
    return data

def show_predict_page(data):
    st.title('Salary Prediction')
    st.write('Please fill in the form below to predict your salary')
    st.write('---')
    with st.form(key='predict_form'):
        country = st.selectbox('Country', COUNTRIES)
        education = st.selectbox('Education', EDUCATION)
        employment = st.selectbox('Employment', EMPLOYMENT)
        experience = st.slider('Experience (Years)', 0, 50, 0)
        submit_button = st.form_submit_button(label='Predict')
        
    if submit_button:
        # Preprocess data
        country = data['country_encoder'].transform([country])[0]
        education = data['education_encoder'].transform([education])[0]
        employment = data['employment_encoder'].transform([employment])[0]
        experience = np.array([experience])
        
        # Predict
        x = np.array([country, education, employment, experience])
        x = torch.from_numpy(x).float()
        y_pred = data['pytorch_model'](x)
        y_pred = data['scaler'].inverse_transform(y_pred.detach().numpy())
        y_pred = y_pred[0][0]
        
        # Show prediction
        st.write('---')
        st.write(f'Your estimated salary is ${y_pred:.2f}')
        
if __name__ == '__main__':
    data = load_model()
    linear = data['Linear']
    decission = data['DecissionTree']
    random = data['RandomForest']
    neural = data['pytorch_model']
    country_encoder = data['country_encoder']
    education_encoder = data['education_encoder']
    employment_encoder = data['employment_encoder']