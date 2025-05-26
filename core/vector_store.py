from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

class VectorStoreManager:
    def __init__(self, embedding_model):
        self.embedding_model = embedding_model
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=200,
            length_function=len,
            is_separator_regex=False,
        )

    def create_vector_store(self, documents):
        """Create FAISS index from documents"""
        split_docs = self.text_splitter.create_documents(documents)
        return FAISS.from_documents(split_docs, self.embedding_model)
