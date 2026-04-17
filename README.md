# Bangladeshi Currency Detection 

## 📌 Project Overview
This project is an end-to-end Machine Learning pipeline designed to detect and classify Bangladeshi currency from images. 

The pipeline covers the entire lifecycle of a professional ML project: from data collection and augmentation in Roboflow, to fine-tuning a YOLO model to distinguish between paper notes and metallic coins, and finally, deploying the model as a containerized RESTful API using FastAPI and Docker.

---

## 🏗️ Architecture & Tech Stack
* **Computer Vision:** YOLO (Ultralytics), OpenCV
* **API Framework:** FastAPI, Uvicorn
* **Containerization:** Docker
* **Cloud Deployment:** Render
* **Data Processing:** Roboflow

---

## 📊 Dataset & Preprocessing
The dataset was processed and augmented using Roboflow to ensure model robustness against different angles, lighting, and currency formats (paper vs. coin).
* **Total Original Images:** 433
* **Total Generated Images (After Augmentation):** 1,039
* **Classes Detected (11):** `10 tk`, `100 tk`, `1000 tk`, `2 tk`, `2 tk coin`, `20 tk`, `200 tk`, `5 tk`, `5 tk coin`, `50 tk`, `500 tk`.
* **Dataset Link:** *(Paste your Google Drive or Roboflow link here)*

---

## 🧠 Model Training & Fine-Tuning
The project required expanding the initial paper-note detection model to also recognize metallic coins. The model was fine-tuned using a YOLO architecture (`yolo26n.pt`) to achieve high accuracy on this mixed-media dataset while remaining lightweight enough for CPU cloud deployment.

### Training Parameters
* **Base Model:** YOLO (`yolo26n.pt`)
* **Epochs:** 30
* **Image Size:** 512x512

### Performance Metrics
The fine-tuning phase successfully allowed the model to differentiate between paper notes and metallic coins of the same monetary value (e.g., `5 tk` note vs. `5 tk coin`). 

### 📸 Training Proof & Predictions

*<img width="636" height="468" alt="training_proof" src="https://github.com/user-attachments/assets/fa1926f3-6682-413c-920b-513703a6e36f" />*

---

## 🚀 Deployment & Testing Stages
To ensure reliability, the API was rigorously tested at three different stages of the CI/CD pipeline.

### Stage 1: Local Virtual Environment Testing
The raw FastAPI application was tested locally using a Python virtual environment to verify the core prediction logic.
**Proof of Local FastAPI and Postman Test:**
*FastAPI(in browser)*

*<img width="1366" height="2092" alt="using_fastapi" src="https://github.com/user-attachments/assets/a91cbe2a-9684-4b46-a413-5e18d37d8722" />*

*FastAPI(in Postman)*

*<img width="1366" height="768" alt="fastapi_postman" src="https://github.com/user-attachments/assets/80385500-dc75-4c2c-a9a0-e91c52d0267c" />*

*VScode terminal*

*<img width="849" height="464" alt="fastapi_terminal" src="https://github.com/user-attachments/assets/84176734-e7b3-469d-a98f-752c57973ace" />*

### Stage 2: Local Docker Container Testing
The application was containerized using `python:3.10-slim` and tested locally to ensure all dependencies (like PyTorch and Uvicorn) functioned correctly in an isolated Linux environment.

**Proof of Docker Test:**

*Postman*

*<img width="1366" height="768" alt="docker postman" src="https://github.com/user-attachments/assets/99040352-8070-4f4a-9cab-107731d74287" />*

*Docker Destop Logs*

*<img width="1366" height="768" alt="docker logs" src="https://github.com/user-attachments/assets/fff6c8cc-1ae4-408b-bcdf-9122bad45568" />*


### Stage 3: Live Cloud Deployment (Render)
The final Docker image was pushed to GitHub and automatically built and hosted on Render's cloud servers. 
👉 **[Test the Live API Here](https://bd-currency-api.onrender.com/docs)**

**Proof of Live Cloud Testing (Swagger Web UI):**

*<img width="1332" height="595" alt="render_web" src="https://github.com/user-attachments/assets/b8656f34-2cb9-4085-9e3b-28390c5036a1" />*


**Proof of Live Cloud Testing (Postman):**
*
<img width="1366" height="768" alt="render_postman" src="https://github.com/user-attachments/assets/5b2d7927-bb59-4b9b-b1a3-8f341482b52c" />*


---

## 💻 How to Run Locally

### Run via Docker (Recommended)
1. Clone this repository and navigate to `Model_Deployment`.
2. Build the Docker image:
   ```bash
   docker build -t bd-currency-api .

   ---

## 👤 Author

Soumitra Chowdhury
