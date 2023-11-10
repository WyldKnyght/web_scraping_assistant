from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

local_path : str = "models/llama-2-13b-chat.Q4_K_M.gguf"

llm = CTransformers(model=local_path, model_type='llama')

template = """Question: {question}

Answer: {answer}"""

prompt = PromptTemplate(template=template, input_variables=["question"], output_variables=["answer"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

response = llm_chain.run({"question": "What is AI?", "answer": ""})
print(response)