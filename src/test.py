''''import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

for m in genai.list_models():
    if 'embedContent' in m.supported_generation_methods:
        print(f"Supported Embedding Model: {m.name}")'''


import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("Available models for your key:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"-> {m.name}")