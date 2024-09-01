from sentence_transformers import SentenceTransformer

def load_sentence_transformer():
    return SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(model, text):
    return model.encode(text)