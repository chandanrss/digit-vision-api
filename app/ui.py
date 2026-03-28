import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import requests
from PIL import Image

API_URL = "http://localhost:8080/predict"  # change

st.title("🖍️ MNIST Digit Classifier")

st.write("Draw a digit below and let the Machine Learning model guess it!")

canvas = st_canvas(
    fill_color="#000000",
    stroke_width=12,
    stroke_color="#FFFFFF",
    background_color="#000000",
    width=500,
    height=300,
    drawing_mode="freedraw"
)

if st.button("Predict"):
    if canvas.image_data is not None:
        img = Image.fromarray(canvas.image_data.astype("uint8")).convert("RGB")  # convert to RGB
        img.save("temp.png")  # PNG format

        with open("temp.png", "rb") as f:
            response = requests.post(API_URL, files={"file": ("temp.png", f, "image/png")})

        try:
            result = response.json()
            print(result)
            print("Status code:", response.status_code)
            print("Response text:", response.text)
        except Exception as e:
            st.error(f"Server returned invalid JSON: {response.text}")
        else:
            st.write(result)
