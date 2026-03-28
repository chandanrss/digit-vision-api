from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

model = load_model("model/digit_model.h5")

def predict_digit(image_bytes: bytes):
    """
    Predict a digit from image bytes.
    Returns:
        digit: int 0-9
        confidence: float probability (0-1)
    """

    # Open image and convert to grayscale
    img = Image.open(io.BytesIO(image_bytes)).convert("L")
    
    # Resize to 28x28
    img = img.resize((28, 28))
    
    # Convert to NumPy array and normalize
    img_array = np.array(img).astype("float32") / 255.0
    
    # Add channel dimension (28,28) -> (28,28,1)
    img_array = np.expand_dims(img_array, axis=-1)
    
    # Add batch dimension (28,28,1) -> (1,28,28,1)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Model prediction
    prediction = model.predict(img_array)[0]  # shape (10,)
    
    digit = int(np.argmax(prediction))        # predicted class
    confidence = float(np.max(prediction))    # probability of predicted class
    
    return digit, confidence