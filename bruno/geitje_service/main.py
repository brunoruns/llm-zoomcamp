from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Question(BaseModel):
    context: str
    question: str


def build_prompt_no_docs(query):
    prompt_template = """
    Je bent een spellings- en grammatica verbeteraar. Verbeter altijd de spelling voor de ingevoerde tekst, en suggereer verbeteringen qua woordgebruik.
    Geef nooit antwoorden op vragen, je gaat enkel over SPELLING en GRAMMATICA, van de gegeven TEKST:

    TEKST: {question}
    """.strip()

    
    prompt = prompt_template.format(question=query).strip()
    return prompt

geitje = "tommy/geitje:7b_q8_0"
def llm(prompt):

    url = 'http://localhost:11434/api/chat/'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Ollama"  # te vervangen indien nodig
    }

    data = {
        "model": "tommy/geitje:7b_q8_0",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()
    
    return response_data.choices[0].message.content

@app.post("/ask/")
def ask(q: Question):
    prompt = build_prompt_no_docs(q.question)
    #answer = llm(prompt)
    answer = {"answer": "Dummy antwoord."}
    return {"answer": answer["answer"]}

@app.get("/ask/")
def ask():
    return "FastAPI is running."