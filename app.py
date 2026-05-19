import streamlit as st
import google.generativeai as genai

# Konfigurasi Tampilan Aplikasi
st.set_page_config(page_title="Aplikasi NgoPi", page_icon="☕", layout="centered")

st.title("☕ Aplikasi NgoPi (Ngobrol Pintar)")
st.subheader("Asisten Digital Penyusun Teks Khotbah & Ceramah Keagamaan")
st.write("Sambil ngopi, susun draf khotbah Jumat dan kultum jadi lebih cepat, rapi, dan sesuai kaidah fikih.")
st.markdown("---")

# Menu Samping
st.sidebar.markdown("## ☕ Menu NgoPi")
tema = st.sidebar.text_input("Tema Obrolan / Khotbah", placeholder="Contoh: Menjaga Kerukunan Warga")
jenis_acara = st.sidebar.selectbox("Jenis Teks", ["Khotbah Jumat Lengkap", "Kultum / Ceramah Singkat", "Sambutan Acara Desa"])
durasi = st.sidebar.select_slider("Target Durasi Baca", options=["7 Menit", "10 Menit", "15 Menit"])
api_key = st.sidebar.text_input("🔑 Masukkan Gemini API Key", type="password")

st.sidebar.markdown("---")
st.sidebar.caption("Aplikasi NgoPi v1.1 © 2026")

# Logika Pemrosesan AI
if st.button("☕ Seduh Teks (Generate)"):
    if not api_key:
        st.error("Silakan masukkan 'Gemini API Key' di menu samping dulu ya.")
    elif not tema:
        st.warning("Temanya masih kosong nih, silakan diisi dulu.")
    else:
        with st.spinner("Sedang meracik draf khotbah terbaik... Mohon tunggu sebentar..."):
            try:
                # Menggunakan konfigurasi client yang kompatibel dengan library lama/baru
                genai.configure(api_key=api_key)
                
                # Menggunakan model versi 2.0-flash yang sangat stabil untuk generate content
                model = genai.GenerativeModel(model_name='gemini-2.0-flash')
                
                prompt_sistem = f"""
                Anda adalah seorang ulama kharismatik, ahli fikih, dan orator yang bijaksana di masyarakat.
                Buatlah draf teks {jenis_acara} dengan tema spesifik: "{tema}" untuk durasi pembacaan {durasi}.
                
                Aturan Penulisan yang WAJIB dipenuhi:
                1. Jika ini 'Khotbah Jumat Lengkap', harus dibagi tegas menjadi Khotbah Pertama dan Khotbah Kedua.
                2. Khotbah Pertama WAJIB mengandung rukun formal: Pujian kepada Allah (Alhamdulillah), Shalawat kepada Nabi, Wasiat Takwa, dan minimal satu potong Ayat Al-Qur'an/Hadits yang sesuai tema.
                3. Gunakan bahasa Indonesia yang santun, sejuk, mengayomi, mudah dipahami masyarakat, dan selipkan pesan sosial yang relevan dengan kehidupan warga setempat saat ini.
                4. Khotbah Kedua wajib berisi kesimpulan singkat dan doa penutup untuk kemaslahatan kaum muslimin (dalam bahasa Arab).
                """
                
                response = model.generate_content(prompt_sistem)
                
                st.success("☕ Racikan Teks Selesai!")
                st.markdown("### 📝 Draf Hasil Teks:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Terjadi kendala teknis: {e}")
