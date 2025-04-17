# Pneumonia_detection_cnn

This project is a final group project of Lambton College (Mississauga): Semester - 3.

Running the models locally can be `time-consuming` and `resource-intensive`, especially if your system `doesn't meet` the recommended requirements. To avoid long training times, you can directly download the pre-trained model parameters from the link below and make sure to add the file in the main working directory:

🔗 **[Download Pre-trained Models](https://drive.google.com/drive/folders/10rPB-yi-aqdqs1f5t2e49NXBxmj-2Pdl?usp=sharing)**


## Table of Content:
- [Objective](#objective)
- [Members List](#memebers-list)
- [Dataset](#dataset)
- [Installation](#installation)
    - [Step-1 Cloning the Repo](#step---1)
    - [Stpe-2: Creating the virtual env](#step---2)
    - [Step-3: Installing Dependencies](#step---3)
    - [Step-4: Training the models](#step---4)
    - [Step-5: Running the UI](#step---5)
- [Pre-Processing Steps](#pre-processing-steps)
- [Models Used](#models-used)
- [Results](#results)
- [System Requirements](#system-requirements)


## Objective:
The goal of this project is to build an AI-based system that can detect pneumonia from chest X-ray images using both traditional machine learning and deep learning techniques. This system can assist healthcare professionals in faster diagnosis and treatment planning.


## Memebers List:
- Rahul Rawat
- Ronakkumar Chavda
- Sehaj Singh Jaggi
- Shruthi

## Dataset:
For this project we have choose, Chest X-Ray Images (Pneumonia) data from the Kaggle.

![alt text](img/image.png)

The dataset is organized into 3 folders (train, test, val) and contains subfolders for each image category (Pneumonia/Normal). There are 5,863 X-Ray images (JPEG) and 2 categories (Pneumonia/Normal).

The normal chest X-ray (left panel) depicts clear lungs without any areas of abnormal opacification in the image. Bacterial pneumonia (middle) typically exhibits a focal lobar consolidation, in this case in the right upper lobe (white arrows), whereas viral pneumonia (right) manifests with a more diffuse "interstitial" pattern in both lungs.


## Installation:

### Step - 1:
Clone the repository on your machine and open the folder in VScode.
```bash
git clone https://github.com/RawatRahul14/Pneumonia_detection_cnn.git

cd Pneumonia_detection_cnn

code .
```

### Step - 2:
Create the virtual environment and activate it.
```bash
python -m venv .venv
.venv/Scripts/activate
```

### Step - 3:
Install the required packages.
```bash
pip install -r requirements.txt
```

### Step - 4:
First, run the main.py file to run the file.
```bash
python main.py
```

### Step - 5:
Now, to run the streamlit UI, run the below code.
```bash
streamlit run app.py
```


## Pre-Processing Steps:
We applied two types of preprocessing based on the model type:
- ***For Machine Learning Models:*** Images were flattened into NumPy arrays. This transforms each image into a 1D feature vector suitable for models like Logistic Regression and Random Forest.

- ***For Deep Learning Models (Keras):*** We used `flow_from_directory()` to load and preprocess images in batches. This method automatically resizes images, applies normalization, and efficiently feeds data into the CNN and VGG16 models.


## Models Used:
We’ve implemented and compared four different models for pneumonia detection:

- ***Logisitc Regression:*** A basic linear model used as a baseline. It separates normal and pneumonia cases using extracted image features.
- ***Random Forest Classifier:*** An ensemble of decision trees that handles complex patterns and reduces overfitting for better accuracy.
- ***Deep Convolutional Neural Network***: A custom convolutional neural network that learns features like textures and shapes directly from X-ray images.
- ***VGG16 (Transfer Learning) Model***: A pre-trained model with frozen base layers. We added a custom classifier on top to adapt it for pneumonia detection.


## Results:

| Model                     | Accuracy |
|--------------------------|----------|
| Logistic Regression      | 78%    |
| Random Forest Classifier | 84%    |
| CNN                      | 90.22%    |
| VGG16                    | 91.67%    |

> *Note: Accuracy values are based on test set evaluation.*


## System Requirements
To run this project smoothly, especially when converting high-resolution X-ray images to NumPy arrays for machine learning models, your system should meet the following minimum requirements:

- RAM: 16 GB (32 GB recommended for faster image preprocessing and training)
- CPU: Intel i5 / Ryzen 5 or better
- GPU: (Optional) NVIDIA GPU with CUDA support for faster deep learning model inference
- Storage: ~10 GB (including dataset, virtual environment and saved models)

> *📝 Note: The image flattening and preprocessing steps can consume significant memory. Close other heavy applications to avoid RAM overload or crashes.*