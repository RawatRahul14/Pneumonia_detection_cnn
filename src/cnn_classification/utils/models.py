import joblib
from pathlib import Path
from tensorflow.keras.models import load_model

def load_all_models():
    """
    Loads all ML and DL models and returns them as a dictionary.

    Returns:
        dict: A dictionary of models keyed by their display name.
    """

    ml_models_path = Path("Models/ml_models")
    tf_models_path = Path("Models/tf_models")

    models = {
        "Logistic Regression": joblib.load(ml_models_path / "logistic_regression.pkl"),
        "Random Forest Classifier": joblib.load(ml_models_path / "rfc_model.pkl"),
        "Deep Convolution Network": load_model(tf_models_path / "best_cnn_model.keras"),
        "VGG-16 (Transfer Learning)": load_model(tf_models_path / "transfer_learning_model.keras")
    }
    return models