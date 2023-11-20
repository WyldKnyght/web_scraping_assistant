from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "TheBloke/Llama-2-13B-chat-GGUF"
model_file = "llama-2-13b-chat.q4_K_M.gguf"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, model_file=model_file)

custom_directory = "M:/dev_env/web_scraping_assistant/models"

model.save_pretrained(custom_directory)
tokenizer.save_pretrained(custom_directory)
