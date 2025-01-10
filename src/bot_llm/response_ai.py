from openai import OpenAI
from definitions import ROOT_DIR
import yaml
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

class ResponseAI:
    def __init__(self, temperature=0):
        self.key = os.environ["OPENAI_KEY"]
        self.client = OpenAI(api_key=self.key)
        self.temperature = temperature
        self.prefix_system_message = ""

        stream = open("./test.yaml", "r")
        self.queries = yaml.safe_load(stream).get("query")
        stream.close()

    def _complete_response(self, data, system_message=""):
        print("Bot llamado")
        response = self.client.chat.completions.create(
            temperature=self.temperature,
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": system_message,
                },
                {
                    "role": "user",
                    "content": f"Por favor, procesa la siguiente información en español: {data}",
                },
            ],
        )
        return response

    def first_stage(self, data):
        FIRST_STAGE_MESSAGE = self.queries.get("preparse")
        response = self._complete_response(data, FIRST_STAGE_MESSAGE)
        intent = response.choices[0].message.content['intent']
        print(intent)
        #self.query_LLM(intent, data)

    # Probably this method could replace every upper method
    def query_LLM(self, query_name, data):
        query = self.queries.get(query_name)
        response = ""

        if query_name == "buscar":
            MESSAGE = query.get("buscar")
            response = self._complete_response(data, MESSAGE)
            data = response.choices[0].message.content

        if query_name == "tasar":
            MESSAGE = query.get("tasar")
            response = self._complete_response(data, MESSAGE)
            data = response.choices[0].message.content

        if query_name == "hipotecario":
            MESSAGE = query.get("hipotecario")
            response = self._complete_response(data, MESSAGE)
            data = response.choices[0].message.content

        return response.choices[0].message.content