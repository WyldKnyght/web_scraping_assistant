#\src\Agents\llama_generative_agent\llama_generative_agent.py

from langchain.llms import LlamaCpp
from langchain.embeddings import LlamaCppEmbeddings
from vectorestores.chroma import EnhancedChroma
from retrivers.llama_time_weighted_retriever import LlamaTimeWeightedVectorStoreRetriever
from generative_agents.llama_generative_agent import LlamaGenerativeAgent
from generative_agents.llama_memory import LlamaGenerativeAgentMemory
import os

# Define model path
script_directory = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.abspath(os.path.join(script_directory, "../../../models/llama-2-13b-chat.Q4_K_M.gguf"))

# Initialize LlamaCpp
llm = LlamaCpp(
    model_path=model_path,
    verbose=True,
    n_batch=256,
    temperature=0.3,
    n_ctx=2048,
    use_mmap=False,
    stop=["###"]
)

# Set up the ChromaDB Vector Store
embeddings_model = LlamaCppEmbeddings(model_path=model_path)
vs = EnhancedChroma(embedding_function=embeddings_model, collection_name="my_collection")

# Define memory retriever function
def create_new_memory_retriever():
    return LlamaTimeWeightedVectorStoreRetriever(vectorstore=vs, other_score_keys=["importance"], k=15)


# Set up the Generative Agent
tommies_memory = LlamaGenerativeAgentMemory(
    llm=llm,
    memory_retriever=create_new_memory_retriever(),
    reflection_threshold=8,
    verbose=True,
)

tommie = LlamaGenerativeAgent(
    name="Tommie",
    age=25,
    traits="anxious, likes design, talkative",
    status="looking for a job",
    memory_retriever=create_new_memory_retriever(),
    llm=llm,
    memory=tommies_memory,
    verbose=True,
)


print(tommie.get_summary(force_refresh=True))

# We can add memories directly to the memory object
tommie_observations = [
    "Tommie remembers his dog, Bruno, from when he was a kid",
    "Tommie feels tired from driving so far",
    "Tommie sees the new home",
    "The new neighbors have a cat",
    "The road is noisy at night",
    "Tommie is hungry",
    "Tommie tries to get some rest.",
]
for observation in tommie_observations:
    tommie.memory.add_memory(observation)



# Now that Tommie has 'memories', their self-summary is more descriptive, though still rudimentary.
# We will see how this summary updates after more observations to create a more rich description.
print(tommie.get_summary(force_refresh=True))



print(tommie.generate_reaction("Tommie sees his neighbor's cat"))



tommie.generate_dialogue("Dad", "Have you got a new job?")

