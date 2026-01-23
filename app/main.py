from fastapi import FastAPI, File, UploadFile
from app.predict import predict_digit  # should accept a NumPy array
import io

app = FastAPI()


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read uploaded file
    image_bytes = await file.read()

    digit = predict_digit(image_bytes)

    return {"predicted_digit": int(digit)}  # make sure JSON serializable
