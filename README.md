U-Net Image Denoising Project (Built in Google Colab)
-------------------------------------------------------

👤 Author: [ASIF AHMED]
📅 Date: [12/072025]

📁 Project Structure:
---------------------
1. U-Net-Denoising.ipynb       → Main Google Colab notebook
2. streamlit_app.py            → Streamlit UI for denoising images
3. unet_model.h5               → Trained U-Net model
4. dataset.zip                 → Clean + Noisy image folders
5. Report.pdf                  → Final project report

💻 How to Run This Project:
---------------------------

✅ STEP 1: Open the Colab Notebook
- Upload and open `U-Net-Denoising.ipynb` in Google Colab.
- Run all cells:
    - This will mount Google Drive, generate noisy images, train the U-Net model, and save it.

✅ STEP 2: Launch the Streamlit UI in Colab
- Upload `streamlit_app.py` into your Colab environment.
- Install required tools:
    ```python
    !pip install streamlit pyngrok
    ```

- Add your ngrok authtoken (only once):
    ```python
    !ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
    ```

- Start Streamlit in background:
    ```python
    !nohup streamlit run streamlit_app.py --server.port 8501 > /dev/null 2>&1 &
    ```

- Open the tunnel:
    ```python
    from pyngrok import ngrok
    public_url = ngrok.connect(addr="http://localhost:8501", proto="http")
    print(public_url)
    ```

- Click the link to open the web app and upload a noisy image to see the result.

📦 Dataset Info:
----------------
- Located in `dataset/` folder:
    - `clean/`: Original clean images
    - `noisy/`: Same images with added Gaussian noise

🧠 Model Info:
--------------
- U-Net architecture with encoder-decoder structure
- Trained for 20 epochs using MSE loss and Adam optimizer

📄 Report:
----------
- Contains explanation of dataset, model, training, UI, results, and references

📌 Requirements (already handled in Colab):
------------------------------------------
- Python 3.x
- TensorFlow / Keras
- OpenCV
- Streamlit
- Pyngrok
