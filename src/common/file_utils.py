from pathlib import Path

def create_directory(directory):
    # Create the directory if it doesn't exist
    Path(directory).mkdir(parents=True, exist_ok=True)

def find_unique_file_name(directory, website_name):
    # Find a unique file name
    i = 1
    while (file_path := Path(directory, f"{website_name}-{i}.txt")).exists():
        i += 1
    return file_path.name

def save_text_to_file(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

def save_links_to_file(file_path, links):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(f"{link}\n" for link in links)