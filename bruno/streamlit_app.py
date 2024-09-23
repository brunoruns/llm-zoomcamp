import streamlit as st
import requests
import os

geitje_service_url = os.getenv("GEITJE_SERVICE_URL", "http://localhost:8000")

st.title("Chat met Geitje")

#context = st.text_area("Context:", height=200)
context = ""
question = st.text_input("Geef hier je tekst:")

if st.button("Kijk na"):
    if question:
        response = requests.post(f"{geitje_service_url}/ask/", json={"context": context, "question": question})
        answer = response.json()["answer"]
        st.write("Antwoord:", answer)
    else:
        st.write("Geef een tekst in.")
