import os
from PIL import Image



def folder_creation():
   new_folder_name =  "PNG_outputs"
   new_folder_path = os.path.join(os.getcwd(),new_folder_name)
   os.makedirs(new_folder_path)





def check_exist(folder_path):
    if not os.path.isdir(folder_path):
        folder_creation()

def convert_to_JPG(image):
    img = Image.open(image)
    output = f"{image}.png"
    img.save(output,'PNG')
    img.close()
    print(f"conversion of {image} to {output} is completed")


# def get_file():

folder_path = "D:\\Programming\\Py\\PycharmProjects\\ztm\\image_processing\\PNG_outputs" #expected folder for output

jpg_path ='D:\\Programming\\Py\\PycharmProjects\\ztm\\image_processing\\pokedex'

# files = os.listdir(jpg_path)
folder = ["pokedex/pikachu.jpg"] #list of all the pics to be converted
# print(files)

check_exist(folder_path)

for pictures in os.listdir(jpg_path):
    img = pictures
    clean_name = os.path.splitext(pictures)
    convert_to_JPG(img)
    print(clean_name)
