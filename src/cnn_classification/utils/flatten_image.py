import numpy as np
from PIL import Image

def flatten_and_normalize_image(image: Image.Image) -> np.ndarray:
    """
    Resize to 224x224, normalize to [0,1], and flatten to 1D vector for ML models.

    Args:
        image (PIL.Image.Image): Input RGB image

    Returns:
        np.ndarray: Flattened image of shape (1, 150528)
    """
    image = image.resize((224, 224)).convert("RGB")
    image_array = np.array(image) / 255.0
    return image_array.reshape(1, -1)
