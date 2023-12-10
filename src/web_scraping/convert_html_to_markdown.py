# \src\web_scraping\convert_html_to_markdown.py

import logging
import os
from common.save_to_file import save_to_file
from common.create_directory import create_directory
import html2text

# Set up logging
logging.basicConfig(level=logging.INFO)

def convert_to_markdown(html_content, unique_filename):
    if unique_filename is None:
        logging.error("Unique filename is None. Unable to proceed with conversion.")
        return None

    try:
        # Convert HTML to Markdown using html2text
        html2text_converter = html2text.HTML2Text()
        markdown_content = html2text_converter.handle(html_content)

        # Save Markdown content to a file
        markdown_file_directory = os.path.join('data', 'scraped_data', 'markdown_data')
        create_directory(markdown_file_directory)
        markdown_file_path = os.path.join(markdown_file_directory, f"{unique_filename}.md")

        # Fix the function call by adding 'md' as the file_extension
        save_to_file(markdown_file_path, markdown_content, 'md')

    except Exception as e:
        logging.error(f"Failed to convert HTML to Markdown: {e}")
        return None

    return markdown_file_path