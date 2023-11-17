# \src\web_scraping\data_transformation.py
import os
import pandas as pd
from common.file_handling import create_directory, save_text_to_file
from transformers import AutoModelForCausalLM
from llama_cpp import Llama

class DataTransformer:
    def label_and_save_data(self, text, filename):
        if not text:
            raise ValueError("Text is empty")

        # Load the GGUF model

        model_path = './models/llama-2-13b-chat.Q4_K_M.gguf'
        
        llm = Llama(model_path,
            model_type="llama",
            wbits=4,
            groupsize=512,
            gpu_layers=0
        )

        # Split the text into smaller chunks based on a delimiter
        delimiter = ". "
        text_chunks = text.split(delimiter)

        # Initialize an empty list to store the labeled text chunks
        labeled_chunks = []

        # Loop through each text chunk and apply the labeling rules using the loaded model
        for chunk in text_chunks:
            # Check if the chunk is within the maximum context length of the model
            if len(chunk.split()) <= llm.config.max_position_embeddings:
                # Apply the labeling rules using the loaded model
                input_ids = llm.tokenizer.encode(chunk, return_tensors="pt")
                output = llm.generate(input_ids, max_length=1024, do_sample=True)
                labeled_chunk = llm.tokenizer.decode(output[0], skip_special_tokens=True)

                # Append the labeled chunk to the list of labeled chunks
                labeled_chunks.append(labeled_chunk)
            else:
                # Split the chunk into smaller sub-chunks and apply the labeling rules to each sub-chunk
                sub_chunks = chunk.split(delimiter)
                for sub_chunk in sub_chunks:
                    # Check if the sub-chunk is within the maximum context length of the model
                    if len(sub_chunk.split()) <= llm.config.max_position_embeddings:
                        # Apply the labeling rules using the loaded model
                        input_ids = llm.tokenizer.encode(sub_chunk, return_tensors="pt")
                        output = llm.generate(input_ids, max_length=1024, do_sample=True)
                        labeled_sub_chunk = llm.tokenizer.decode(output[0], skip_special_tokens=True)

                        # Append the labeled sub-chunk to the list of labeled chunks
                        labeled_chunks.append(labeled_sub_chunk)

        # Join the labeled chunks back into a single string
        labeled_text = delimiter.join(labeled_chunks)

        # Save the labeled text to a file
        output_dir = create_directory("output")
        output_path = os.path.join(output_dir, f"{filename}.txt")
        save_text_to_file(labeled_text, output_path)

        return output_path
