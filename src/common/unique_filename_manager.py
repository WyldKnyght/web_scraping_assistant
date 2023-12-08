# \src\common\unique_filename_manager.py

import os
import logging
import tldextract

# Set up logging
logging.basicConfig(level=logging.INFO)

class UniqueFilenameManager:
    counter = 1

    @classmethod
    def find_unique_file_name(cls, url):
        extracted_domain = tldextract.extract(url)
        hostname = extracted_domain.domain if extracted_domain.domain else None
        filename = hostname if hostname else None

        candidate_filename = f"{filename}-{cls.counter}"
        file_path = os.path.join('data', 'scraped_data', 'html_data', f"{candidate_filename}.html")
        
        while os.path.exists(file_path):
            cls.counter += 1
            candidate_filename = f"{filename}-{cls.counter}"
            file_path = os.path.join('data', 'scraped_data', 'html_data', f"{candidate_filename}.html")

        logging.info(f"Unique file name found: {candidate_filename}")
        return candidate_filename 

