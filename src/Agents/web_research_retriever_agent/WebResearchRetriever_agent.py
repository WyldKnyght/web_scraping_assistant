from langchain.embeddings import LlamaCppEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import AsyncHtmlLoader

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

# Vectorstore
vectorstore = Chroma(
	embedding_function=LlamaCppEmbeddings(), persist_directory="./chroma_db_oai"
)

# Initialize the loader with the URLs you want to scrape
loader = AsyncHtmlLoader(["http://example.com"])

# Load the web pages
docs = loader.load()

# Now, you can access the content of each web page
for doc in docs:
  print(doc.page_content)
