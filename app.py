import streamlit as st
from core.data_loader import CSVProcessor
from core.embeddings import EmbeddingManager
from core.vector_store import VectorStoreManager
from core.rag_chain import RAGSystem
import os

def main():
    st.set_page_config(
        page_title="CSV Chat Analyst",
        layout="wide",
        page_icon="📊"
    )
    
    st.title("📊 CSV Data Chat Analyst")
    
    # Initialize components
    embedding_model = EmbeddingManager().model
    vector_mgr = VectorStoreManager(embedding_model)
    
    # File upload
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    if uploaded_file:
        with st.status("Processing CSV..."):
            try:
                # Load and process CSV
                df = CSVProcessor.load_csv(uploaded_file)
                documents = CSVProcessor.df_to_documents(df)
                
                # Create vector store
                vector_store = vector_mgr.create_vector_store(documents)
                retriever = vector_store.as_retriever(search_kwargs={"k": 5})
                
                # Initialize RAG system
                rag_system = RAGSystem(retriever)
                st.session_state.rag_system = rag_system
                st.success("Analysis system ready!")
                
                # Show preview
                with st.expander("CSV Preview"):
                    st.dataframe(df.head())
                    
            except Exception as e:
                st.error(f"Error processing file: {str(e)}")
                return
        
        # Chat interface
        user_query = st.chat_input("Ask about your data...")
        if user_query:
            with st.spinner("Analyzing..."):
                try:
                    response = st.session_state.rag_system.query(user_query)
                    st.chat_message("user").write(user_query)
                    st.chat_message("assistant").write(response['answer'])
                except Exception as e:
                    st.error(f"Query failed: {str(e)}")

if __name__ == "__main__":
    if "HUGGINGFACEHUB_API_TOKEN" not in os.environ:
        st.error("Please set HUGGINGFACEHUB_API_TOKEN in environment variables")
    else:
        main()
