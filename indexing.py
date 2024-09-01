import os
import numpy as np
import faiss
from config import BASE_DIR, SUBJECTS, EMBEDDING_DIM
from embedding import get_embedding

def create_faiss_index(subject, model):
    index = faiss.IndexFlatL2(EMBEDDING_DIM)
    subject_dir = os.path.join(BASE_DIR, subject)
    embeddings = []
    files = []
    for filename in os.listdir(subject_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(subject_dir, filename), "r") as f:
                content = f.read()
                embedding = get_embedding(model, content)
                embeddings.append(embedding)
                files.append(filename)
    if embeddings:
        index.add(np.array(embeddings))
    return index, files

def setup_faiss_indexes(model):
    return {subject: create_faiss_index(subject, model) for subject in SUBJECTS}
