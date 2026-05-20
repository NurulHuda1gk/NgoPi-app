import streamlit as st
import requests

# Konfigurasi Tampilan Utama
st.set_page_config(page_title="Aplikasi NgoPi", page_icon="☕", layout="centered")

st.title("☕ Aplikasi NgoPi (Ngobrol Pintar)")
st.subheader("Asisten Digital Penyusun Teks Khotbah & Ceramah Keagamaan")
st.write("Sambil ngopi, susun draf khotbah Jumat dan kultum jadi lebih cepat, rapi, dan berkah.")
st.markdown("---")

# Pengaturan Menu Samping
st.sidebar.markdown("## ☕ Menu NgoPi")
tema = st.sidebar.text_input("Tema Obrolan / Khotbah", placeholder="Contoh: Menjaga Kerukunan Warga")
jenis_acara = st.sidebar.selectbox("Jenis Teks", ["Khotbah Jumat Lengkap", "Kultum / Ceramah Singkat", "Sambutan Acara Desa"])
durasi = st.sidebar.select_slider("Target Durasi Baca", options=["7 Menit", "10 Menit", "15 Menit"])

st.sidebar.markdown("---")
st.sidebar.caption("Aplikasi NgoPi v1.3 © 2026")

# Proses Pembuatan Teks Menggunakan Jalur Server Stabil
if st.button("☕ Seduh Teks (Generate)"):
    if not tema:
        st.warning("Temanya masih kosong nih, silakan diisi dulu ya Pak.")
    else:
        with st.spinner("Sedang meracik draf terbaik... Mohon tunggu sebentar..."):
            try:
                # Menggunakan endpoint publik cadangan yang sangat stabil
                url = "https://openrouter.ai/api/v1/chat/completions"
                
                prompt_sistem = f"""
                Anda adalah seorang ulama kharismatik, ahli fikih, dan orator yang bijaksana.
                Buatlah draf teks {jenis_acara} dengan tema spesifik: "{tema}" untuk durasi pembacaan {durasi}.
                
                Aturan Penulisan:
                1. Jika ini 'Khotbah Jumat Lengkap', harus dibagi tegas menjadi Khotbah Pertama dan Khotbah Kedua.
                2. Khotbah Pertama WAJIB mengandung rukun formal: Pujian kepada Allah (Alhamdulillah), Shalawat, Wasiat Takwa, dan minimal satu potong Ayat Al-Qur'an/Hadits yang sesuai tema.
                3. Gunakan bahasa Indonesia yang santun, sejuk, mengayomi, dan mudah dipahami masyarakat.
                4. Khotbah Kedua wajib berisi kesimpulan singkat dan doa penutup berbahasa Arab.
                """
                
                # Menggunakan model alternatif gratis yang kapasitasnya sangat longgar
                payload = {
                   "model": "google/gemini-2.5-flash:free",
 
                   "messages": [{"role": "user", "content": prompt_sistem}]
                }
                
                response = requests.post(url, json=payload, timeout=30)
                data = response.json()
                
                if "choices" in data and len(data["choices"]) > 0:
                    teks_hasil = data["choices"][0]["message"]["content"]
                    st.success("☕ Racikan Teks Selesai!")
                    st.markdown("### 📝 Draf Hasil Teks:")
                    st.write(teks_hasil)
                else:
                    st.error("Jalur komunikasi sedang ramai, silakan klik kembali tombol Seduh Teks.")
            except Exception as e:
                st.error(f"Terjadi kendala koneksi: {e}")
