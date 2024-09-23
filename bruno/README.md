# Geitje service

This setup consists of 2 docker containers. The first container runs a fastapi service that sets up a webservice, whose only goal is to forward requists to a running local instance of ollama on port 11434. If another local model is used, change the call in the main.py ask routine to point to the correct instance.
The second container contains a very simple streamlit frontend connecting to this webservice. Both can be easly spun up together with the `docker-compose.yml` file.