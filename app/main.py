from fastapi import FastAPI, File, UploadFile, HTTPException 
from app.predict import predict_digit
import io

app = FastAPI()


@app.get("/")
def home():
    return {"message": "MNIST API is running!"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    receive an image file and predict the handwritten digit.
    Returns JSON with:
        - digit: predicted digit (0-9)
        - confidence: model probability
    """
    # Validate file type
    # if file.content_type not in ["image/png", "image/jpeg"]:
    #     raise HTTPException(status_code=400, detail="Please upload png/jpeg image")

    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload an image file")

    try:
        # Read bytes from uploaded file
        image_bytes = await file.read()

        # Here, we will Call the predict_digit function (returns digit + confidence)
        digit, confidence = predict_digit(image_bytes)

        # Return JSON response
        return {"digit": int(digit), "confidence": round(confidence, 4)}

    except Exception as e:
        # Catch all errors and return as JSON (prevents HTML/error pages)
        raise HTTPException(status_code=500, detail=str(e))
