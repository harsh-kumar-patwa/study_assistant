import logging
from setup import setup_directories
from embedding import load_sentence_transformer
from indexing import setup_faiss_indexes
from classification import load_subject_content, setup_tfidf_vectorizer, classify_query
from retrieval import retrieve_document
from response_generation import setup_gemini, generate_response
from utils import read_document

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        logging.info("Starting the Study Helper system")
        setup_directories()
        sentence_model = load_sentence_transformer()
        subject_docs = load_subject_content()
        vectorizer = setup_tfidf_vectorizer(subject_docs)
        indexes = setup_faiss_indexes(sentence_model)
        gemini_model = setup_gemini()

        logging.info("Setup complete. Starting interactive loop")

        print("Welcome to the Study Helper! Type 'exit' to quit.")
        while True:
            query = input("Enter your query: ")
            if query.lower() == 'exit':
                break

            try:
                subject = classify_query(query, vectorizer, subject_docs)
                if subject == "General":
                    response, source = generate_response(gemini_model, query)
                    print(f"Query: {query}\n")
                    print(f"Subject: General\n")
                    print(f"Source: {source}\n")
                    print(f"Generated response\n: {response}\n")
                else:
                    doc_name = retrieve_document(query, subject, indexes, sentence_model)
                    context = read_document(subject, doc_name)
                    response, source = generate_response(gemini_model, query, context)
                    print(f"Query: {query}\n")
                    print(f"Subject: {subject}\n")
                    print(f"Retrieved document: {doc_name}\n")
                    print(f"Source: {source}\n")
                    print(f"Generated response\n: {response}\n")
            except Exception as e:
                logging.error(f"Error processing query: {str(e)}")
                print(f"An error occurred while processing your query: {str(e)}. Please try again.")

            print()

        print("Thank you for using the Study Helper!\n")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        print("An error occurred while setting up the Study Helper. Please check the logs for more information.")

if __name__ == "__main__":
    main()