import os
from PIL import Image

directory = "./images/tutorials/"
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        print(os.path.join(directory, filename))
        im = Image.open(directory+filename)
        im.save(directory+filename, dpi=(72,72))
        continue
    else:
        continue

directory = "./images/tutorials/jump_server_load_balancer/"
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        print(os.path.join(directory, filename))
        im = Image.open(directory+filename)
        im.save(directory+filename, dpi=(72,72))
        continue
    else:
        continue
