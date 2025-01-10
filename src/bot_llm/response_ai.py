from openai import OpenAI
from definitions import ROOT_DIR
import yaml
import os
import json
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file
class ResponseAI:

    def __init__(self, temperature=0):
        self.key = os.environ["OPENAI_KEY"]
        self.client = OpenAI(api_key=self.key)
        self.temperature = temperature
        self.prefix_system_message = ""
        self.contextdata = ""
        stream = open(os.path.join(ROOT_DIR, "resources/test.yaml"), "r")
        self.queries = yaml.safe_load(stream).get("query")
        stream.close()

    def _complete_response(self, data, system_message=""):
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
        self.contextdata += data
        FIRST_STAGE_MESSAGE = self.queries.get("preparse")
        response = self._complete_response(data, FIRST_STAGE_MESSAGE)
        intent_dict = response.choices[0].message.content
        json_intent = json.loads(intent_dict)
        return json_intent["intent"]

        
        # Revisamos si hay campos con valores vacíos
        print(answer)
        
        missing_fields = []

        for item in answer.get("response", []):
            print
            if item['value'] is False:  # Comprobamos si el valor es False
                missing_fields.append(item['key'])

        # Si hay campos faltantes, generar un mensaje amable
        if missing_fields:
            missing_fields_str = ', '.join(missing_fields)
            message = f"Parece que falta información en los siguientes campos: {missing_fields_str}. ¿Podrías proporcionarnos los datos faltantes?"
        else:
            message = "¡Gracias por toda la información! Todo está completo."
        return message


    # Probably this method could replace every upper method
    def query_LLM(self, query_name, data):
        query = self.queries.get(query_name)
        response = ""
        boolval= False
        self.contextdata += data
        if query_name == "buscar":
            MESSAGE = self.queries.get("buscar")
            data += "algo" # Use the chatbot here
            response = self._complete_response(self.contextdata, MESSAGE)
            data = response.choices[0].message.content
            print(data)
        if query_name == "tasar":
            MESSAGE = self.queries.get("tasar")
            data += "en la comuna Las condes"
            response = self._complete_response(self.contextdata, MESSAGE)
            data = response.choices[0].message.content

        if query_name == "hipotecario":
            MESSAGE = self.queries.get("hipotecario")
<<<<<<< Updated upstream
            data += "mi renta es de 1millon 500mil pesos" # Use the chatbot here
            response = self._complete_response(data, MESSAGE)
=======
            data += "algo" # Use the chatbot here
            response = self._complete_response(self.contextdata, MESSAGE)
>>>>>>> Stashed changes
            data = response.choices[0].message.content
            print(data)

        return boolval, response.choices[0].message.content