import streamlit as st
from PIL import Image
from rembg import remove

st.title("AI Background Remover: ")

uploaded_file=st.file_uploader("Upload an Image")
if uploaded_file:
    img=Image.open(uploaded_file)
    st.subheader("Orignal Image")
    st.image(img,use_container_width=True)

    if st.button("Remove Background"):
        with st.spinner("Removing background..."):
            remove()