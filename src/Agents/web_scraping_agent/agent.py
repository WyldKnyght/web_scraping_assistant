# \scr\Agents\web_scraping_agent\agent.py

import os
import requests
from os.path import expanduser
from bs4 import BeautifulSoup
from langchain.prompts import ChatPromptTemplate
from langchain.agents import Agent, Tool
from langchain.schema.agent import AgentFinish
from langchain.document_loaders import AsyncChromiumLoader
from langchain.embeddings import LlamaCppEmbeddings
from langchain.retrievers.web_research import WebResearchRetriever
from langchain.vectorstores import Chroma
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from web_scraping.scraper import Scraper
from web_scraping.data_preprocessing import Preprocessor
from web_scraping.data_transformation import DataTransformer   
from langchain.llms import LlamaCpp
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from selenium.webdriver.chrome.options import Options

# Define model path
script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.abspath(os.path.join(script_directory, "../../../models/llama-2-13b-chat.Q4_K_M.gguf"))
model_path = expanduser(file_path)

# Initialize LlamaCpp and model
llm = LlamaCpp(
    model_path=model_path,
    streaming=False,
)
chat_model = Llama2Chat(llm=llm)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Use the prompt in the initialization of LLMChain
llm_chain = LLMChain(llm=chat_model, prompt=prompt, memory=memory)

# Initialize compression retriever
llm = LlamaCpp(temperature=0)
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=retriever)

# HEADERS definition
HEADERS = {
    'User-Agent': 'Your User Agent String',  # Replace with your actual user agent
    'other_header': 'other_value',  # Add other headers as needed
}

class GetWebSchema:
    def __init__(self):
        with requests.Session() as session:
            self.session = session
        self.chrome_options = Options()  # Import Options from Selenium
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-gpu")
        self.llama_agent = LlamaCpp()

class WebScrapingTool(Tool):
    def __init__(self, scraper, preprocessor, data_transformer):
        self.scraper = scraper
        self.preprocessor = preprocessor
        self.data_transformer = data_transformer

    def fetch_web_page(self, user_url: str) -> str:
        # Use the user input as the URL to fetch
        with requests.get(user_url, headers=HEADERS) as web_response:
            soup = BeautifulSoup(web_response.content, 'html.parser')  # Use BeautifulSoup for parsing
            return soup.get_text()
  
    def run(self, input_data):
        # Use the agent's chat function to get user input
        user_input = agent.chat(input_data)
        web_response = self.scraper.send_get_request(user_input)
        soup = self.scraper.parse_html(web_response)
        extracted_text = self.scraper.extract_text(soup)
        preprocessed_text = self.preprocessor.preprocess_text(extracted_text)
        transformed_data = self.data_transformer.transform_and_save_data(preprocessed_text)
        return transformed_data

# Use the LlamaCPP agent instead of the Flask app
if __name__ == '__main__':
    llama_agent.run(debug=True)
