
import streamlit as st
from backend import process_text, process_image

st.set_page_config(
    page_title="Smart Study Assistant",
    layout="centered"
)

st.title("📘 Smart Study Assistant")
st.write("Upload notes or paste text to get summaries, definitions, and quizzes.")

#  Input section 

st.subheader("Input")

text_input = st.text_area(
    "Paste your study material here:",
    height=200
)

uploaded_image = st.file_uploader(
    "Or upload an image (notes / textbook page):",
    type=["png", "jpg", "jpeg"]
)

generate_clicked = st.button("Generate Study Guide")

#  Processing 

if generate_clicked:
    if text_input.strip():
        result = process_text(text_input)

    elif uploaded_image is not None:
        image_bytes = uploaded_image.read()
        result = process_image(image_bytes)

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
