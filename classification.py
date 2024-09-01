import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from config import BASE_DIR, SUBJECTS, GENERAL_QUERY_THRESHOLD

def load_subject_content():
    subject_docs = []
    for subject in SUBJECTS:
        subject_content = []
        subject_dir = os.path.join(BASE_DIR, subject)
        print(f"Loading content for subject: {subject}")
        print(f"Directory path: {subject_dir}")
        
        if not os.path.exists(subject_dir):
            print(f"Warning: Directory does not exist: {subject_dir}")
            continue

        for filename in os.listdir(subject_dir):
            if filename.endswith(".txt"):
                file_path = os.path.join(subject_dir, filename)
                print(f"Reading file: {file_path}")
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read().strip()
                        if content:
                            subject_content.append(content)
                            print(f"Successfully read {len(content)} characters from {filename}")
                        else:
                            print(f"Warning: Empty file: {filename}")
                except Exception as e:
                    print(f"Error reading file {filename}: {str(e)}")
        
        if subject_content:
            combined_content = " ".join(subject_content)
            subject_docs.append(combined_content)
            print(f"Total content length for {subject}: {len(combined_content)} characters")
        else:
            print(f"Warning: No content found for subject: {subject}")
    
    if not subject_docs:
        raise ValueError("No content found in any subject. Please check your data files.")
    
    return subject_docs

def setup_tfidf_vectorizer(subject_docs):
    if not subject_docs:
        raise ValueError("No subject documents provided for vectorization.")
    vectorizer = TfidfVectorizer(stop_words='english')
    vectorizer.fit(subject_docs)
    return vectorizer

def classify_query(query, vectorizer, subject_docs):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, vectorizer.transform(subject_docs))
    if np.max(similarities) < GENERAL_QUERY_THRESHOLD:
        return "General"
    return SUBJECTS[np.argmax(similarities)]