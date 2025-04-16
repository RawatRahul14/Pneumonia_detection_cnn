import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array

def preprocess_image(image):
    # Convert to RGB just in case
    image = image.convert("RGB")
    image = image.resize((224, 224))
    image_array = img_to_array(image)
    image_array = image_array / 255.0  # Normalize
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    return image_array