import numpy as np
from embedding import get_embedding

def retrieve_document(query, subject, indexes, model):
    if subject == "General":
        return None
    index, files = indexes[subject]
    query_embedding = get_embedding(model, query)
    D, I = index.search(np.array([query_embedding]).astype('float32'), 1)
    return files[I[0][0]]
