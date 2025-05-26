from langchain.agents import create_csv_agent
from langchain_community.llms import Ollama

def get_csv_agent(file_path):
    llm = Ollama(model="llama3")  # Or any open-source LLM
    return create_csv_agent(
        llm,
        file_path,
        verbose=True,
        agent_type="zero-shot-react-description",
    )
