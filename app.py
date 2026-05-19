import streamlit as st
import requests

# Konfigurasi Tampilan Aplikasi
st.set_page_config(page_title="Aplikasi NgoPi", page_icon="☕", layout="centered")

st.title("☕ Aplikasi NgoPi (Ngobrol Pintar)")
st.subheader("Asisten Digital Penyusun Teks Khotbah & Ceramah Keagamaan")
st.write("Sambil ngopi, susun draf khotbah Jumat dan kultum jadi lebih cepat, rapi, dan berkah.")
st.markdown("---")

# Menu Samping
st.sidebar.markdown("## ☕ Menu NgoPi")
tema = st.sidebar.text_input("Tema Obrolan / Khotbah", placeholder="Contoh: Menjaga Kerukunan Warga")
jenis_acara = st.sidebar.selectbox("Jenis Teks", ["Khotbah Jumat Lengkap", "Kultum / Ceramah Singkat", "Sambutan Acara Desa"])
durasi = st.sidebar.select_slider("Target Durasi Baca", options=["7 Menit", "10 Menit", "15 Menit"])

st.sidebar.markdown("---")
st.sidebar.caption("Aplikasi NgoPi v1.2 © 2026")

# Logika Pemrosesan AI Alternatif
if st.button("☕ Seduh Teks (Generate)"):
    if not tema:
        st.warning("Temanya masih kosong nih, silakan diisi dulu ya Pak.")
    else:
        with st.spinner("Sedang meracik draf terbaik secara instan... Mohon tunggu..."):
            try:
                url = "https://openrouter.ai/api/v1/chat/completions"
                
                prompt_sistem = f"Buatlah draf teks {jenis_acara} dengan tema: '{tema}' untuk durasi pembacaan {durasi}. Jika ini Khotbah Jumat, wajib mengandung rukun formal khotbah (pujian, shalawat, wasiat takwa, ayat Al-Qur'an, dan doa penutup berbahasa Arab). Gunakan bahasa Indonesia yang sejuk dan menyentuh hati jamaah."
                
                payload = {
                    "model": "google/gemini-2.5-flash:free",
                    "messages": [{"role": "user", "content": prompt_sistem}]
                }
                
                response = requests.post(url, json=payload)
                data = response.json()
                
                if "choices" in data:
                    teks_hasil = data["choices"][0]["message"]["content"]
                    st.success("☕ Racikan Teks Selesai!")
                    st.markdown("### 📝 Draf Hasil Teks:")
                    st.write(teks_hasil)
                else:
                    st.error("Server cadangan sedang sibuk, silakan klik tombol sekali lagi.")
            except Exception as e:
                st.error(f"Terjadi kendala teknis: {e}")
