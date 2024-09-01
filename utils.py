import os
from config import BASE_DIR

def read_document(subject, doc_name):
    with open(os.path.join(BASE_DIR, subject, doc_name), "r") as f:
        return f.read()