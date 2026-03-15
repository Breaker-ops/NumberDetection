import numpy as np
from resize import DATA_DIR
import os
import cv2
import streamlit as st
from PIL import Image

st.title("Test de modèle de classification d'image")
st.write("Uploader une image pour faire une prédiction.")
uploaded_file = st.file_uploader("Choisir une image", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Image uploadée", use_container_width=True)
path_dir = os.path.join("./", DATA_DIR)
directory = os.listdir(path_dir)
directory.sort()

images = []
labels = []


for dirs in directory :
    each_dir = os.path.join(DATA_DIR, dirs)
    for file in os.listdir(each_dir) :
        img = cv2.imread(os.path.join(each_dir, file))
        img = img.flatten()
        
        images.append(img)
        labels.append(dirs)
images = np.array(images) / 255.0
labels = np.array(labels)

img_test = images[27]

def predict(img_test) :
    distances = []
    i = 0
    for image in images :
        neig = np.sqrt(np.sum((image - img_test) ** 2))
        distances.append(neig)
        
    distances = np.array(distances)
    print(distances.shape)
    k_indices = distances.argsort()[:3]
    k_labels = labels[k_indices]

    values, counts = np.unique(k_labels, return_counts=True)

    prediction = values[np.argmax(counts)]
    return prediction

prediction = predict(img_test)
print(prediction)