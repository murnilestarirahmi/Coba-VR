import streamlit as st
import base64
import os
from PIL import Image

# Pengaturan dasar aplikasi
st.set_page_config(page_title="Virtual Tour RS Medina", layout="wide")

# Memuat file CSS eksternal
with open("public/css/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Tambahkan CSS untuk full screen
st.markdown(
    """
    <style>
        /* Menghapus margin dan padding pada body */
        body {
            margin: 0;
            padding: 0;
            overflow-x: hidden; /* Mencegah scroll horizontal */
        }
        /* Menghapus padding pada main dan root Streamlit */
        .main {
            padding: 0 !important;
        }
        .stApp {
            padding: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Fungsi untuk membaca dan menampilkan gambar 
def load_logo(logo_path):
    with open(logo_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
        return f'data:image/png;base64,{encoded_string}'

# Header dengan logo dan kolom chat
logo_url = load_logo("public/images/logo-rumah-sakit-medina.png")
gambar_url = "public/images/L1-1-Gerbang-Masuk.jpg"
st.markdown(
    f"""
    <div class="header">
        <img src="{logo_url}" alt="RS Medina Logo">
        <div class="chat-box">
            <input type="text" placeholder="Tanyakan Sesuatu..." />
            <button>Kirim</button>
        </div>
    </div>
    """, unsafe_allow_html=True
)

# Virtual Tour Viewer dengan deskripsi di samping kanan dan kotak berbentuk persegi panjang
st.markdown(
    """
    <div class="virtual-tour">
        <h2>Virtual Tour RS Medina</h2>
        <div class="vr-image-container">
            <img src="public/images/L1-1-Gerbang-Masuk.jpg" class="vr-image" alt="VR Tour Image">
            <div class="vr-description">
                <p>
                    Selamat datang di Virtual Tour RS Medina. Gunakan kontrol yang tersedia untuk menjelajahi berbagai area di rumah sakit. 
                    Dengan VR Tour ini, Anda dapat memperoleh pengalaman mendalam tentang fasilitas dan layanan yang kami tawarkan. 
                    Nikmati tur virtual kami dan rasakan kehadiran Anda di RS Medina meskipun Anda tidak berada di tempat secara fisik.
                </p>
            </div>
        </div>
        <div class="vr-tour-button-container">
            <a href="public/html/L1 1 Gerbang Masuk.html" class="vr-tour-button">Mulai Tour</a>
        </div>
    </div>
    """, unsafe_allow_html=True
)

# Footer dengan warna hijau toska dan lingkaran kecil di sudut kanan bawah
st.markdown(
    """
    <footer>
        <p>&copy; 2024 RS Medina. All rights reserved.<br>
        <a href="#">Kontak</a></p>
    </footer>
    <a href="https://www.bing.com/maps?osid=1ee41d0f-5c0a-439c-a062-8a43dd99e4d8&cp=-7.18065~107.97183&lvl=16&pi=0&imgid=b603a22d-61a7-4160-b873-9daef1e93ca1&v=2&sV=2&form=S00027" target="_blank" class="map-button">
        📍
    </a>
    """, unsafe_allow_html=True
)
