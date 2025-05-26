import streamlit as st
from agents.csv_agent import get_csv_agent
from utils.file_handler import save_uploaded_file

def main():
    st.title("CSV Query Assistant")
    
    # File upload and agent initialization
    uploaded_file = st.file_uploader("Upload CSV")
    if uploaded_file:
        file_path = save_uploaded_file(uploaded_file)
        agent = get_csv_agent(file_path)
        
        # Query interface
        query = st.text_input("Ask about your data:")
        if query:
            response = agent.run(query)
            st.write(response)

if __name__ == "__main__":
    main()
