import os
import tempfile

def save_uploaded_file(uploaded_file):
    """Saves uploaded file to temporary storage"""
    temp_dir = "data/uploads"
    os.makedirs(temp_dir, exist_ok=True)
    
    with tempfile.NamedTemporaryFile(
        dir=temp_dir,
        delete=False,
        suffix=".csv"
    ) as tmp:
        tmp.write(uploaded_file.getbuffer())
        return tmp.name
