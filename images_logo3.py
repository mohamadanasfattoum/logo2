from PIL import Image
import os


output_folder = input('Enter output_folder Name: ')
logo_name = input('Enter logo_name Name: ')

os.chdir('images')
if not os.path.isdir(output_folder):
    os.mkdir(output_folder)
    
logo= Image.open(logo_name)
logo_width , logo_height = logo.size





for filename in os.listdir('.'):
    if filename.endswith(('.jpg','.png','.jpeg')):
        image = Image.open(filename)
        width , heigth = image.size

        image.paste(logo,(width - logo_width , heigth - logo_height),logo)
        image.save(os.path.join(output_folder,filename.lower()))

print('FINISHED...')