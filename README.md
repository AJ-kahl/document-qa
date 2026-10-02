# Document Q&A

A command-line tool that reads a text document and answers questions
about it using a large language model. Point it at a file, ask a
question, and it returns an answer grounded in that document's contents.

## How it works

1. Reads a local text file into memory
2. Sends the document text along with a question to an LLM (via the Groq API)
3. Prints the model's answer

This is the core pattern behind retrieval-augmented generation (RAG):
inject document context into an LLM prompt so the model answers from
your data rather than only its training.

## Setup

1. Install dependencies:
pip install requests python-dotenv

2. Create a `.env` file in the project root with your Groq API key:
GROQ_API_KEY=your_key_here

3. Add the document you want to query as `notes.txt`

## Usage
python app.py


## Built with

- Python
- Groq API (LLaMA / GPT-OSS models)
- requests, python-dotenv