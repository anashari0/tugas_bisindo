import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Edukasi BISINDO", page_icon="🤟", layout="centered")

API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    st.error("API Key belum disetel di pengaturan server!")
    st.stop()

genai.configure(api_key=API_KEY)

st.title("🤟 Mari Berbicara dengan Tangan: Kenali BISINDO")

st.image("https://lh3.googleusercontent.com/d/1XQSoEZ1fPWrcZ9zA4q33KrOfGJHXsami", use_container_width=True)

st.markdown("""
<div style="text-align: center; font-size: 1.05em; line-height: 1.6;">
    <strong>Membangun dunia yang inklusif dimulai dari komunikasi.</strong><br>
    Kesenjangan informasi seringkali membuat teman Tuli merasa terpinggirkan. Bahasa Isyarat Indonesia (BISINDO) adalah kunci untuk menjembatani ruang antara teman dengar dan teman Tuli. Melalui teknologi AI, mari kita mulai langkah kecil untuk belajar dan peduli.
</div>

<hr style="margin-top: 20px; margin-bottom: 20px;">

<div style="text-align: center; font-size: 0.95em;">
    <strong>Ingin belajar BISINDO secara langsung? Kunjungi:</strong><br><br>
    <a href="https://www.instagram.com/silang.ig?igsh=MTJ5eGx4dGpxcnk1MA==" target="_blank" style="text-decoration: none; color: #0056b3;">🔗 @silang.ig</a> &nbsp; | &nbsp;
    <a href="https://www.instagram.com/pusbisindo?igsh=MTl4c2hldmY1dDVieg==" target="_blank" style="text-decoration: none; color: #0056b3;">🔗 @pusbisindo</a> &nbsp; | &nbsp;
    <a href="https://www.instagram.com/parakerja?igsh=MTAzNjE2Mzc4N3lidA==" target="_blank" style="text-decoration: none; color: #0056b3;">🔗 @parakerja</a>
</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("🤖 Tutor AI BISINDO")
st.write("Tanyakan kata, kalimat, atau etika berinteraksi dengan teman Tuli. AI akan membantu menjelaskannya untuk Anda.")

user_input = st.text_input("Ketik di sini (Contoh: Bagaimana cara isyarat 'Terima Kasih'?):")

if st.button("Tanya AI", type="primary"):
    if user_input:
        with st.spinner('AI sedang berpikir...'):
            prompt = f"""
            Anda adalah advokat inklusi sosial dan BISINDO.
            Pengguna bertanya: '{user_input}'.
            Berikan deskripsi singkat bagaimana mengekspresikan hal tersebut menggunakan gerakan BISINDO.
            Gunakan bahasa Indonesia yang ramah, edukatif, dan mudah dipahami.
            """
            models_to_try = [
                "gemini-2.0-flash",
                "gemini-2.5-flash",
                "gemini-flash-latest",
            ]

            jawaban = None

            for nama_model in models_to_try:
                try:
                    m = genai.GenerativeModel(nama_model)
                    res = m.generate_content(prompt)
                    jawaban = res.text
                    break  # Berhasil dapat jawaban? Langsung stop loop!
                except Exception:
                    continue
            
            if jawaban:
                st.success("Tersedia!")
                st.write(jawaban)
                
            else:
                st.error(
                    "⏳ Server AI sedang mengalami kepadatan trafik global."
                    " Silakan coba klik tombolnya kembali dalam 30 detik."
                )
