import streamlit as st
import numpy as np
from PIL import Image
from cnn_classification.utils.preprocessing import preprocess_image
from cnn_classification.utils.flatten_image import flatten_and_normalize_image
from cnn_classification.utils.models import load_all_models

def main():
        
    with st.spinner("🔄 Loading models... Please wait."):
        # Loading Models
        models = load_all_models()
    st.success("✅ Models loaded successfully!")

    # Header
    st.markdown("<h1 style='text-align: center;'>Pneumonia Detection</h1>", unsafe_allow_html = True)

    with st.sidebar:
        uploaded_image = st.file_uploader("Upload the X-Ray image here.", type = ["jpg", "jpeg"])

        if uploaded_image:
            st.image(uploaded_image, caption = "Uploaded X-Ray", use_container_width = True)

    model_name = st.selectbox("Select your preferred Model: ", options = ["Logistic Regression", "Random Forest Classifier", "Deep Convolution Network", "VGG-16 (Transfer Learning)"])

    if uploaded_image:
        image = Image.open(uploaded_image)
        if model_name in ["Deep Convolution Network", "VGG-16 (Transfer Learning)"]:
            processed_image = preprocess_image(image)
        else:
            processed_image = flatten_and_normalize_image(image)

    # Get the selected model
    selected_model = models[model_name]

    if st.button("Make Predictions"):
        prediction = selected_model.predict(processed_image)

        class_labels = ["NORMAL", "PNEUMONIA"]

        try:
            # For DL models or proba output
            predicted_class = np.argmax(prediction)
            confidence = prediction[0][predicted_class] if prediction.ndim == 2 else prediction[predicted_class]
        except:
            # For ML models
            predicted_class = prediction[0]
            confidence = None
            if hasattr(selected_model, "predict_proba"):
                proba = selected_model.predict_proba(processed_image)
                confidence = proba[0][predicted_class]

        st.write(f"🩺 **Prediction:** {class_labels[predicted_class]}")
        if confidence is not None:
            st.write(f"📊 **Confidence:** {confidence * 100:.2f}%")

if __name__ == "__main__":
    main()