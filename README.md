# 📊 CSV-Chatbot: Retrieval-Augmented Generation (RAG) Chatbot for CSV Data

A powerful Streamlit-based chatbot that lets you **chat with your CSV files** using Retrieval-Augmented Generation (RAG) and open-source Hugging Face language models. Upload any CSV, ask questions in natural language, and get accurate, context-aware answers—powered by [LangChain](https://python.langchain.com/), [Hugging Face](https://huggingface.co/), [FAISS](https://github.com/facebookresearch/faiss), and [Streamlit](https://streamlit.io/).

---

## 🌟 Features

- **Upload any CSV** (auto delimiter/encoding detection)
- **Semantic search**: Embeds your data and retrieves the most relevant rows for each question
- **RAG pipeline**: Answers are grounded in your data, not hallucinated
- **Open-source LLMs**: Uses Hugging Face models (e.g., Zephyr, Mistral, Llama-3)
- **Interactive chat UI**: Powered by Streamlit's chat interface
- **Easy customization**: Swap out models or tweak prompts as you wish

---

## 🗂️ Directory Structure

csv-chatbot/
├── app.py # Main Streamlit app
├── core/ # Core logic modules
│ ├── data_loader.py # CSV loading and preprocessing
│ ├── embeddings.py # Embedding model initialization
│ ├── vector_store.py # Vector store creation and management
│ └── rag_chain.py # Retrieval-augmented generation chain setup
├── data/ # Folder for uploaded CSVs or sample datasets
├── requirements.txt # Python dependencies
├── README.md # Project overview and instructions
└── .env.example # Example environment variables (e.g., HF token)

text

---

## 🚀 Quickstart

### 1. Clone the repository

git clone https://github.com/Birajlayek/round_2_task.git
cd csv-chatbot

text

### 2. Install dependencies

pip install -r requirements.txt

text

### 3. Set up Hugging Face API token

- Copy `.env.example` to `.env` and add your Hugging Face token:
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here


### 4. Run the Streamlit app

streamlit run app.py

text

- The app will open in your browser (usually at http://localhost:8501).

---

## 💡 How It Works

1. **CSV Loading**  
   - Handles any delimiter and encoding automatically.

2. **Data Chunking & Embedding**  
   - Converts each row (or chunk) into a text document.
   - Embeds the documents using a Hugging Face embedding model (e.g., BGE).

3. **Vector Store (FAISS)**  
   - Stores embeddings for fast semantic search and retrieval.

4. **Retrieval-Augmented Generation (RAG)**  
   - Retrieves the most relevant rows for each query.
   - Sends the context and your question to a Hugging Face LLM for answer generation.

5. **Chat Interface**  
   - Streamlit's chat UI displays conversation history and responses.

---

## 🛠️ Configuration

- **Change LLM or embedding model**: Edit `core/embeddings.py` or `core/rag_chain.py` to use your preferred Hugging Face models.
- **Tune retrieval**: Adjust `k` in `vector_store.as_retriever(search_kwargs={"k": 5})` for more or fewer context rows.
- **Prompt engineering**: Modify the prompt template in `core/rag_chain.py` for your use case.

---

## 🧑‍💻 Example Usage

1. **Upload a CSV**  
   (e.g., `products.csv`)

2. **Ask:**  
   - "List all products above $100"
   - "Which region had the highest sales in 2024?"
   - "Compare features between Product A and Product B"

---

## 📝 Troubleshooting

- **Hugging Face token errors**:  
  Ensure your token is valid and has inference access.
- **Large CSVs**:  
  For very large files, increase chunk size or memory as needed.
- **Model loading issues**:  
  Try a smaller model or check your internet connection.

---

## 📚 Dependencies

See `requirements.txt` for the full list.  
Key packages include:  
- streamlit  
- pandas  
- langchain  
- langchain-community  
- langchain-core  
- huggingface_hub  
- faiss-cpu  

---

## 📄 License

MIT License

---

## 🙏 Acknowledgments

- [LangChain](https://python.langchain.com/)
- [Hugging Face](https://huggingface.co/)
- [Streamlit](https://streamlit.io/)
- [FAISS](https://github.com/facebookresearch/faiss)


Happy chatting with your CSVs!