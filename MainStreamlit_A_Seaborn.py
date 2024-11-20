import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu
import numpy as np

# testing
with st.sidebar:
    selected = option_menu(
        'Proyek UTS PMDPM_A_Seaborn',
        ['Klasifikasi', 'Regresi', 'Catatan'],
        default_index=0
    )

if selected == 'Klasifikasi':
    st.title('Prediksi Kategori Rumah')

    model_path = r'BestModel_CLF_RF_Seaborn.pkl'
    
    with open(model_path, 'rb') as f:
        loaded_model = pickle.load(f)

    rf_model = loaded_model

    st.header("Masukkan Fitur Rumah")

    luas_tanah = st.number_input("Luas Tanah (m²)", min_value=0.0, step=0.1)
    jumlah_kamar = st.number_input("Jumlah Kamar", min_value=1, step=1)
    lantai = st.number_input("Jumlah Lantai", min_value=1, step=1)
    kota_kode = st.selectbox("Kode Kota", [310, 340, 350, 390])
    area_kota = st.selectbox("Kode Area Kota", [1, 2, 3, 4, 5])
    pemilik_sebelumnnya = st.number_input("Jumlah Pemilik Sebelumnya", min_value=0)
    dibuat = st.number_input("Tahun Dibuat", min_value=1900, max_value=2024)

    hasyard = st.selectbox("Ada Halaman?", ["Tidak", "Ya"])
    haspool = st.selectbox("Ada Kolam Renang?", ["Tidak", "Ya"])
    isnewbuilt = st.selectbox("Bangunan Baru?", ["Tidak", "Ya"])
    hasstormprotector = st.selectbox("Ada Pelindung Badai?", ["Tidak", "Ya"])
    hasstorageroom = st.selectbox("Ada Gudang?", ["Tidak", "Ya"])

    basement = st.number_input("Luas Basement (m²)", min_value=0.0, step=0.1)
    attic = st.number_input("Luas Attic (m²)", min_value=0.0, step=0.1)
    garage = st.number_input("Luas Garasi (m²)", min_value=0.0, step=0.1)

    hasyard = 1 if hasyard == "Ya" else 0
    haspool = 1 if haspool == "Ya" else 0
    isnewbuilt = 1 if isnewbuilt == "Ya" else 0
    hasstormprotector = 1 if hasstormprotector == "Ya" else 0
    hasstorageroom = 1 if hasstorageroom == "Ya" else 0

    input_data = np.array([[luas_tanah, jumlah_kamar, lantai, kota_kode, area_kota, pemilik_sebelumnnya, dibuat, hasyard,
                            haspool, isnewbuilt, hasstormprotector, hasstorageroom,
                            basement, attic, garage, 0, 0, 0, 0, 0, 0,]])

    if st.button("Prediksi Kategori"):
        try:
            rf_model_prediction = rf_model.predict(input_data)
            outcome = {'Basic': 'Basic', 'Luxury': 'Luxury', 'Middle': 'Middle'}
            st.success(f"Prediksi Kategori Rumah Adalah :  *{outcome[rf_model_prediction[0]]}*")
        except Exception as e:
            st.error(f"Terjadi kesalahan saat melakukan prediksi: {str(e)}")

if selected == 'Regresi':
    st.title('Prediksi Harga Rumah')

    model_path = r'BestModel_REG_SVR_Seaborn.pkl'
    
    with open(model_path, 'rb') as f:
        loaded_model = pickle.load(f)

    rf_model = loaded_model

    st.header("Masukkan Fitur Rumah")

    luas_tanah = st.number_input("Luas Tanah (m²)", min_value=0.0, step=0.1)
    jumlah_kamar = st.number_input("Jumlah Kamar", min_value=1, step=1)
    lantai = st.number_input("Jumlah Lantai", min_value=1, step=1)
    kota_kode = st.selectbox("Kode Kota", [310, 340, 350, 390])
    area_kota = st.selectbox("Kode Area Kota", [1, 2, 3, 4, 5])
    pemilik_sebelumnnya = st.number_input("Jumlah Pemilik Sebelumnya", min_value=0)
    dibuat = st.number_input("Tahun Dibuat", min_value=1900, max_value=2024)

    hasyard = st.selectbox("Ada Halaman?", ["Tidak", "Ya"])
    haspool = st.selectbox("Ada Kolam Renang?", ["Tidak", "Ya"])
    isnewbuilt = st.selectbox("Bangunan Baru?", ["Tidak", "Ya"])
    hasstormprotector = st.selectbox("Ada Pelindung Badai?", ["Tidak", "Ya"])
    hasstorageroom = st.selectbox("Ada Gudang?", ["Tidak", "Ya"])

    basement = st.number_input("Luas Basement (m²)", min_value=0.0, step=0.1)
    attic = st.number_input("Luas Attic (m²)", min_value=0.0, step=0.1)
    garage = st.number_input("Luas Garasi (m²)", min_value=0.0, step=0.1)

    hasyard = 1 if hasyard == "Ya" else 0
    haspool = 1 if haspool == "Ya" else 0
    isnewbuilt = 1 if isnewbuilt == "Ya" else 0
    hasstormprotector = 1 if hasstormprotector == "Ya" else 0
    hasstorageroom = 1 if hasstorageroom == "Ya" else 0

    input_data = np.array([[luas_tanah, jumlah_kamar, lantai, kota_kode, area_kota, pemilik_sebelumnnya, dibuat, hasyard,
                            haspool, isnewbuilt, hasstormprotector, hasstorageroom,
                            basement, attic, garage, 0, 0, 0, 0, 0, 0,]])

    if st.button("Prediksi Harga"):
        try:
            prediksi_harga = rf_model.predict(input_data)
            st.success(f"Prediksi Harga Rumah: Rp {prediksi_harga[0]:,.0f}")
        except Exception as e:
            st.error(f"Terjadi kesalahan saat melakukan prediksi: {str(e)}")
