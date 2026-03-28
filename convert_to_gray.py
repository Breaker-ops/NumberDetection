from PIL import Image
import os

def convert_image_to_gray(source_dir:str, dest_dir:str) :
    for file in os.listdir(source_dir) :
        try :
            os.makedirs(dest_dir)
        except :
            pass
        file_path = os.path.join(source_dir, file)

        image = Image.open(file_path)
        image_to_gray = image.convert("L")

        file_dest = os.path.join(dest_dir, file)
        image_to_gray.save(file_dest)