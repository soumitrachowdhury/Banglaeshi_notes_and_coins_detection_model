from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
import io
from PIL import Image

app = FastAPI(title="Object Detection API")

# Load model ONCE at startup to conserve memory
model = YOLO("best.pt", task="detect")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read the uploaded image file into memory
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data)).convert("RGB")

    # Running inference explicitly on the CPU
    results = model.predict(image, device="cpu")

    # Formatting the results cleanly for Postman
    detections = []
    for box in results[0].boxes:
        detections.append({
            "class_name": model.names[int(box.cls)],
            "confidence": round(float(box.conf), 4),
            "bounding_box": box.xyxy[0].tolist() # [x1, y1, x2, y2]
        })

    return {
        "filename": file.filename, 
        "detections": detections
    }