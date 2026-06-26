import streamlit as st
import google.generativeai as genai
import os

API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    st.error("API Key belum disetel di pengaturan server!")
    st.stop()

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-lite")

st.set_page_config(page_title="Edukasi BISINDO", page_icon="🤟", layout="centered")

st.title("🤟 Mari Berbicara dengan Tangan: Kenali BISINDO")

st.image("https://lh3.googleusercontent.com/d/1XQSoEZ1fPWrcZ9zA4q33KrOfGJHXsami", use_column_width=True)

st.markdown("""
**Membangun dunia yang inklusif dimulai dari komunikasi.** \n
Kesenjangan informasi seringkali membuat teman Tuli merasa terpinggirkan. Bahasa Isyarat Indonesia (BISINDO) adalah kunci untuk menjembatani ruang antara teman dengar dan teman Tuli. Melalui teknologi AI, mari kita mulai langkah kecil untuk belajar dan peduli.
""")

st.divider()

st.subheader("🤖 Tutor AI BISINDO")
st.write("Tanyakan kata, kalimat, atau etika berinteraksi dengan teman Tuli. AI akan membantu menjelaskannya untuk Anda.")

user_input = st.text_input("Ketik di sini (Contoh: Bagaimana cara isyarat 'Terima Kasih'?):")

if st.button("Tanya AI"):
    if user_input:
        with st.spinner('AI sedang berpikir...'):
            prompt = f"""
            Anda adalah advokat inklusi sosial dan BISINDO.
            Pengguna bertanya: '{user_input}'.
            Berikan deskripsi singkat bagaimana mengekspresikan hal tersebut menggunakan gerakan BISINDO.
            Gunakan bahasa Indonesia yang ramah, edukatif, dan mudah dipahami.
            """
            try:
                response = model.generate_content(prompt)
                st.success("ini jawaban")
                st.write(response.text)
                st.markdown("""
                ---
                **Ingin belajar BISINDO secara langsung? Kunjungi:**
                * [🔗 Instagram @silang.ig](https://www.instagram.com/silang.ig?igsh=MTJ5eGx4dGpxcnk1MA==)
                * [🔗 Instagram @pusbisindo](https://www.instagram.com/pusbisindo?igsh=MTl4c2hldmY1dDVieg==)
                * [🔗 Instagram @parakerja](https://www.instagram.com/parakerja?igsh=MTAzNjE2Mzc4N3lidA==)
                """)
            except Exception as e:
                st.error(f"Terjadi kesalahan sistem: {e}")        
    else:
        st.warning("Silakan ketikkan sesuatu terlebih dahulu.")
