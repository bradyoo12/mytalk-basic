# pip install "fastapi[all]"
# uvicorn gemini-api:app --reload 

from fastapi import FastAPI
from dotenv import load_dotenv
import google.generativeai as gen_ai
import os
import textwrap
from IPython.display import Markdown

app = FastAPI()

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))

# http://127.0.0.1:8000/ask/hi
@app.get('/ask/{query}')
async def root(query: str):
    response = model.generate_content(query)
    answer = to_markdown(response.text)
    return answer
