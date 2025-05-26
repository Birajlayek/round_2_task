from langchain_community.embeddings import HuggingFaceBgeEmbeddings

class EmbeddingManager:
    def __init__(self):
        self.model_name = "BAAI/bge-base-en-v1.5"
        self._model = None
    
    @property
    def model(self):
        if not self._model:
            self._model = HuggingFaceBgeEmbeddings(
                model_name=self.model_name,
                model_kwargs={'device': 'cpu'},
                encode_kwargs={'normalize_embeddings': True}
            )
        return self._model
