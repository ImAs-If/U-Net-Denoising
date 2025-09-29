import streamlit as st
import numpy as np
import cv2
from PIL import Image
from tensorflow.keras.models import load_model

# Load model
model_path = "/content/drive/MyDrive/U-Net-Denoising-Project/model/unet_model.h5"
model = load_model(model_path)

# Function to preprocess image
def preprocess_image(uploaded_file):
    img = Image.open(uploaded_file).convert("RGB")
    img = img.resize((128, 128))
    img_array = np.array(img) / 255.0
    return img_array, img

# Function to denoise
def denoise_image(image_array):
    input_img = np.expand_dims(image_array, axis=0)  # Add batch dimension
    denoised_img = model.predict(input_img)[0]
    denoised_img = np.clip(denoised_img * 255, 0, 255).astype(np.uint8)
    return denoised_img

# Streamlit UI
st.title("🧼 Image Denoising using U-Net")

uploaded_file = st.file_uploader("Upload a noisy image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Noisy Input", use_column_width=True)
    img_array, orig_img = preprocess_image(uploaded_file)
    denoised = denoise_image(img_array)
    st.image(denoised, caption="Denoised Output", use_column_width=True)
