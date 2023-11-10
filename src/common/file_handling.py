#\src\common\file_handling.py

import os

def create_directory(directory):
    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

def find_unique_file_name(directory, website_name):
    # Find a unique file name
    file_name = f"{website_name}-1.txt"
    i = 1
    while os.path.exists(os.path.join(directory, file_name)):
        i += 1
        file_name = f"{website_name}-{i}.txt"
    return file_name

def save_text_to_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
