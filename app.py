import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# Fungsi untuk mengonversi gambar menjadi link yang dapat diunduh
def get_image_download_link(img, filename, text):
    buffered = BytesIO()
    plt.savefig(buffered, format="JPEG")
    buffered.seek(0)
    base64_img = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:image/jpeg;base64,{base64_img}" download="{filename}">{text}</a>'
    return href

# Judul Aplikasi
st.title('Tag Cloud Generator')

# Upload File
uploaded_file = st.file_uploader("Pilih file teks untuk dijadikan tag cloud", type="txt")
if uploaded_file is not None:
    # Membaca isi file
    text = uploaded_file.read().decode('utf-8')

    # Membuat tag cloud
    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                min_font_size = 10).generate(text)

    # Menampilkan tag cloud
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")

    st.pyplot(fig)

    # Tautan untuk mengunduh gambar
    st.markdown(get_image_download_link(fig, "tag_cloud.jpg", 'Download Tag Cloud as JPEG'), unsafe_allow_html=True)
