from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

model = load_model("model/digit_model.h5")

def predict_digit(image_bytes: bytes):
    
     # Open image using PIL and convert to grayscale
    img = Image.open(io.BytesIO(image_bytes)).convert("L")
    
    # Resize to 28x28 (MNIST expects 28x28)
    img = img.resize((28, 28))
    
    # Convert to NumPy array
    img_array = np.array(img)
    
    # Normalize pixels to 0-1
    img_array = img_array / 255.0
    
    # Add batch dimension for model input shape [1, 28, 28]
    img_array = np.expand_dims(img_array, axis=0)
    
    # Call the prediction function with NumPy array
    
    prediction = model.predict(img_array)
    return np.argmax(prediction)