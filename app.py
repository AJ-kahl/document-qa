import os
import requests
from dotenv import load_dotenv

load_dotenv()
with open("notes.txt") as file:
    text = file.read()
api_key = os.environ["GROQ_API_KEY"]
url = "https://api.groq.com/openai/v1/chat/completions"

headers = {"Authorization": "Bearer " + api_key}
question = input("Ask something about the file: ")
payload = {
    "model": "openai/gpt-oss-20b",
    "messages": [{"role": "user", "content": "%s\n\n%s" % (question, text)}]
}

try:
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out — the server took too long.")
    exit()

if "choices" in data:
    print(data["choices"][0]["message"]["content"])  
else:
    print("Something went wrong:", data)



