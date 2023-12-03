# /src/model_handler/model_handler.py

import logging
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from huggingface_hub import hf_hub_download

# Set up logging
logging.basicConfig(level=logging.INFO)

# Global variable to store the model
llm_chain = None

def create_model_chain(system_prompt):
    global llm_chain

    # If the model has already been created, just return it
    if llm_chain is not None:
        logging.info("Model already created. Returning existing model.")
        return llm_chain

    try:
        (repo_id, model_file_name) = ("TheBloke/Llama-2-13B-chat-GGUF", "llama-2-13b-chat.Q4_K_M.gguf")

        model_path = hf_hub_download(repo_id=repo_id, filename=model_file_name, repo_type="model")

        llm = LlamaCpp(
            model_path=model_path,
            temperature=0,
            max_tokens=512,
            top_p=1,
            stop=["[INST]"],
            verbose=False,
            streaming=True,
        )

        template = """
        [INST]{}[/INST]
        """.format(system_prompt, "{question}")

        prompt = PromptTemplate(template=template, input_variables=["question"])

        # Store the model in the global variable
        llm_chain = prompt | llm

        logging.info("Model created successfully.")

    except Exception as e:
        logging.error(f"Failed to create model: {e}")

    return llm_chain