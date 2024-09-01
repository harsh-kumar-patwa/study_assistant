# Study Assistant

## Overview

The Study Assistant is an intelligent query routing system designed to assist students in their studies. It uses Retrieval Augmented Generation (RAG) techniques to provide accurate and contextually appropriate responses to queries across multiple subjects.

## Demo video 
[Click here](https://www.loom.com/share/75696347a79643448e439c04fe3a3736?sid=4448407e-d44e-4df5-ae06-7d5d70c18c01)

## Features

- Query classification into specific subjects or general knowledge
- Document retrieval from subject-specific transcripts
- Response generation using the Gemini AI model
- Clear indication of information source (retrieved document or general knowledge)

## Project Structure

```
study_assistant/
├── main.py
├── config.py
├── setup.py
├── embedding.py
├── indexing.py
├── classification.py
├── retrieval.py
├── response_generation.py
├── utils.py
├── requirements.txt
└── study_helper_data/
    ├── ML/
    │   └── script.txt
    ├── DSA/
    │   └── script.txt
    └── WebDev/
        └── script.txt
```

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/harsh-kumar-patwa/study_assistant.git
   cd study-assistant
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Gemini API key:
   - Open `config.py`
   - Replace `"YOUR_GEMINI_API_KEY"` with your actual Gemini API key

5. Prepare your study materials:
   - Place your subject transcripts in the appropriate directories under `data/`

## Usage

Run the main script:

```
python main.py
```

Follow the prompts to enter your queries. Type 'exit' to quit the program.

## Example Queries

1. "What is CSS used for in web development?"
2. "Explain the concept of neural networks in machine learning."
3. "How does bubble sort work?"

## Troubleshooting

If you encounter any issues:

1. Check that your Gemini API key is set correctly in `config.py`.
2. Ensure all transcript files are present and named correctly.
3. Verify that all required packages are installed.
4. Check the console output for any error messages.

