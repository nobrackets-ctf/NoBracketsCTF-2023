#!/usr/bin/env python3

import os
import random
import base64
from secret import flag

# Set the path to the folder containing your images
image_folder = 'dog_cat'

# Get a list of image files in the folder
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]

count = 0

for i in range(500):
    # Choose a random image file
    random_image = random.choice(image_files)

    # Display the random image
    random_image_path = os.path.join(image_folder, random_image)
    with open(random_image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        print(base64_image)

    if "cat" in random_image:
        animal = "cat"
    else:
        animal = "dog"

    user_label = input("Is this image a cat or a dog? (Enter 'cat' or 'dog'): ").strip().lower()

    if user_label == animal:
        count += 1

if count > 450:
    print(f"FLAG : {flag}")
