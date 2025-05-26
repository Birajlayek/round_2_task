from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import HuggingFaceHub

class RAGSystem:
    def __init__(self, retriever, model_name="HuggingFaceH4/zephyr-7b-beta"):
        self.retriever = retriever
        self.llm = HuggingFaceHub(
            repo_id=model_name,
            model_kwargs={
                "temperature": 0.2,
                "max_new_tokens": 512,
                "max_length": 4096
            }
        )
        self.prompt = ChatPromptTemplate.from_template(
            """You are a professional data analyst. Use the following context to answer the question.
            Always provide accurate, verifiable answers based on the data.
            
            Context: {context}
            
            Question: {input}
            
            Answer:"""
        )
        self.chain = create_retrieval_chain(self.retriever, self.llm, prompt=self.prompt)

    def query(self, question):
        return self.chain.invoke({"input": question})
