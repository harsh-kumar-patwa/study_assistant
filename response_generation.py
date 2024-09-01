import google.generativeai as genai
from config import GEMINI_API_KEY

def setup_gemini():
    genai.configure(api_key=GEMINI_API_KEY)
    return genai.GenerativeModel('gemini-pro')

def generate_response(model, query, context=None):
    try:
        if context:
            prompt = f"Context: {context}\n\nQuery: {query}\n\nProvide a response based on the given context. If the context doesn't contain relevant information, say so and then provide a general response to the query."
            source = "Retrieved Document"
        else:
            prompt = f"Query: {query}\n\nProvide a response to this query based on your general knowledge."
            source = "General Knowledge"
        
        response = model.generate_content(prompt)
        
        if response.parts:
            return response.text, source
        else:
            if response.prompt_feedback.safety_ratings:
                safety_issues = [rating.category for rating in response.prompt_feedback.safety_ratings if rating.probability != "NEGLIGIBLE"]
                if safety_issues:
                    return f"I apologize, but I can't provide a response due to safety concerns related to: {', '.join(safety_issues)}.", source
            
            return "I'm sorry, but I couldn't generate a response for this query. Could you please rephrase or try a different question?", source

    except Exception as e:
        return f"An error occurred while generating the response: {str(e)}. Please try again or rephrase your question.", "Error"