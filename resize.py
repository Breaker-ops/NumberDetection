import os
from PIL import Image
DATA_DIR = "DATASET"
def resize() :
    for label in os.listdir("/home/franc-stile/Bureau/KNN/data/") :
        label_path = os.path.join("/home/franc-stile/Bureau/KNN/data/", label)
        if os.path.isdir(label_path) :
            output_label = os.path.join(DATA_DIR, label)
            os.makedirs(output_label, exist_ok=True)

            for file in os.listdir(label_path) :
                image_path = os.path.join(label_path, file)
                try :
                    img = Image.open(image_path)
                    img_resized = img.resize((600, 600))
                    save_path = os.path.join(output_label, file)
                    img_resized.save(save_path)
                except :
                    print("Erreur avec :", image_path)
    print("Toutes les images ont été redimensionnées")