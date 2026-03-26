import os
from PIL import Image
DATA_DIR = "DATASET"
i = 0

"""
    name_dir is source directory that we want to take different pictures
    dest_dir is destination directory that we go to make with a new pictures
    file_name is the common name of different file that we go to have in output
    size is a tuple of two values (height, width)
"""

def resize_img(name_dir:str, dest_dir:str, file_name:str, size:tuple) :
    i = 0
    for file in os.listdir(name_dir) :
        try :
            os.makedirs(dest_dir)
        except :
            pass

        image = Image.open(os.path.join(name_dir, file))
        image_resized = image.resize(size)

        file_save = os.path.join(dest_dir, f"{file_name}{i}.png")
        
        image_resized.save(file_save)
        i += 1