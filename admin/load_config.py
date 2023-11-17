from transformers import AutoModelForCausalLM

model_name = "TheBloke/Llama-2-13B-chat-GGUF"
# Load the model and its configuration file
model = AutoModelForCausalLM.from_pretrained(model_name)

# Access the model's configuration
config = model.config

# Print the maximum position embeddings
print(config.max_position_embeddings)