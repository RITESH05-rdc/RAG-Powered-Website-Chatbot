import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
def load_documents():

    documents = []

    for file in os.listdir("data/pages"):

        path = f"data/pages/{file}"

        with open(path, encoding="utf-8") as f:
            documents.append(f.read())

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100
    )

    chunks = []

    for doc in documents:
        chunks.extend(splitter.split_text(doc))

    return chunks