
import streamlit as st
from backend import process_text, process_image, process_pdf

#page configuration

st.set_page_config(
    page_title="Smart Study Assistant",
    layout="centered"
)

# App header

st.title("📘 Smart Study Assistant")
st.write("Upload notes or paste text to get summaries, definitions, and quizzes.")

#  Input section 

st.subheader("Input")

text_input = st.text_area(
    "Paste your study material here:",
    height=200
)

# File uploader supports images and PDFs

uploaded_file = st.file_uploader(
    "Or upload an image (notes / textbook page):",
    type=["png", "jpg", "jpeg","pdf"]
)

generate_clicked = st.button("Generate Study Guide")

#  Processing 
# Streamlit reruns this script top-to-bottom on every interaction.

if generate_clicked:
    if text_input.strip():
        result = process_text(text_input)

    elif uploaded_file is not None:
        file_bytes = uploaded_file.read()
        if uploaded_file.type.startswith("image/"):
            result = process_image(file_bytes)
        elif uploaded_file.type == "application/pdf":
            result = process_pdf(file_bytes)

    else:
        st.warning("Please provide text or upload an image.")
        st.stop()

    #  Output section 
    
    st.subheader("Summary")
    st.write(result["summary"])

    st.subheader("Key Definitions")
    for d in result["definitions"]:
        st.markdown(f"- {d}")

    st.subheader("Self-Test Quiz")
    for i, q in enumerate(result["quiz"], start=1):
        st.markdown(f"**Q{i}.** {q}")
