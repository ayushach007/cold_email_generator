import uuid
import chromadb
import pandas as pd

class Portfolio:
    def __init__(self, file_path: str = "data/my_portfolio.csv"):
        self.file_path = file_path
        self.df = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient()
        self.collection = self.chroma_client.get_or_create_collection("portfolio")
        
    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.df.iterrows():
                self.collection.add(
                    documents=row['Techstack'],
                    metadatas={'links': row['Links']},
                    ids=str(uuid.uuid4())
                )
    
    def query_link(self, skills: str):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])