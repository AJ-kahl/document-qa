import os
import requests
from dotenv import load_dotenv
load_dotenv()


def read_file(path):
    with open(path, encoding="utf-8") as file:
        return file.read()

def ask_llm(question, context):
    api_key = os.environ["GROQ_API_KEY"]
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": "Bearer " + api_key}
    payload = {
    "model": "openai/gpt-oss-20b",
    "messages": [{"role": "user", "content": "%s\n\n%s" % (question, context)}]
      }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        data = response.json()
    except requests.exceptions.Timeout:
     print("Request timed out — the server took too long.")
     return None
    except (requests.exceptions.RequestException, ValueError) as e:
     print("Request failed:", e)
     return None

    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    print("Something went wrong:", data)
    return None
def main():
    file_path = input("Enter the path to the file you want to ask about: ")
    context = read_file(file_path)
    question = input("Ask something about the file: ")
    result = ask_llm(question, context)
    if result is not None:
       print("Response from LLM:")
       print(result)

if __name__ == "__main__":
    main()


