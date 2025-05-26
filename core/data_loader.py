import pandas as pd
import csv
from io import TextIOWrapper

class CSVProcessor:
    @staticmethod
    def load_csv(uploaded_file):
        """Handle CSV loading with automatic delimiter/encoding detection"""
        try:
            # Detect delimiter
            data = uploaded_file.read(1024).decode('utf-8')
            uploaded_file.seek(0)
            delimiter = csv.Sniffer().sniff(data).delimiter
            
            # Handle encoding
            try:
                return pd.read_csv(
                    TextIOWrapper(uploaded_file, encoding='utf-8'),
                    delimiter=delimiter,
                    on_bad_lines='warn'
                )
            except UnicodeDecodeError:
                uploaded_file.seek(0)
                return pd.read_csv(
                    TextIOWrapper(uploaded_file, encoding='latin-1'),
                    delimiter=delimiter,
                    on_bad_lines='warn'
                )
        except Exception as e:
            raise ValueError(f"CSV processing failed: {str(e)}")

    @staticmethod
    def df_to_documents(df):
        """Convert DataFrame to list of document strings"""
        return [
            "; ".join([f"{col}: {row[col]}" for col in df.columns])
            for _, row in df.iterrows()
        ]
