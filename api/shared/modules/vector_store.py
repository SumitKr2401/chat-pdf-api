import os
import pickle
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings


class VectorStore:
    def __init__(self, path="/vectorstore"):
        self.path = path
        self.embeddings = OpenAIEmbeddings()

    def new(self, chunks):
        return FAISS.from_texts(texts=chunks, embedding=self.embeddings)

    def save(self, vectorstore, name="default"):
        with open(os.path.join(self.path, name + ".pkl"), "wb") as file:
            pickle.dump(vectorstore, file)

    def load(self, name="default"):
        path = os.path.join(self.path, name + ".pkl")
        if os.path.exists(path):
            with open(path, "rb") as file:
                return pickle.load(file)
