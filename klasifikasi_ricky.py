import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('churn_bank.sav', 'rb'))

st.title('Prediksi Nasabah Menutup Rekening Bank')
c1, c2 = st.columns(2)

with c1:
    CustomerId = st.number_input('ID nasabah')
    Gender = st.number_input('Jenis kelamin')
    Tenure = st.number_input('Jumlah tahun menjadi nasabah bank')
    NumOfProducts = st.number_input('Jumlah produk bank yang digunakan nasabah')
    IsActiveMember = st.number_input('Nasabah aktif ?')

with c2:
    CreditScore = st.number_input('Kredit skor nasabah')
    Age = st.number_input('Usia nasabah')
    Balance = st.number_input('Saldo nasabah')
    HasCrCard = st.number_input('Memiliki kartu kredit')
    EstimatedSalary = st.number_input('Estimasi gaji')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[CustomerId, CreditScore, Gender, Age, Tenure, Balance, NumOfProducts,
                               HasCrCard, IsActiveMember, EstimatedSalary]])

    if (prediksi [0] == 0):
        prediksi = ('Nasabah bertahan dengan rekening banknya')
    else:
        prediksi = ('Nasabah menutup rekening banknya')
st.success(prediksi)