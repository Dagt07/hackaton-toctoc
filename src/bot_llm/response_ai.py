from openai import OpenAI
from definitions import ROOT_DIR
import yaml
import os


class ResponseAI:
    def __init__(self, temperature=0):
        self.key = os.environ["OPENAI_KEY"]
        self.client = OpenAI(api_key=self.key)
        self.temperature = temperature
        self.prefix_system_message = ""

        stream = open(ROOT_DIR + "/resources/yaml/queries.yaml", "r")
        self.queries = yaml.safe_load(stream).get("query")
        stream.close()

    def _complete_response(self, data, system_message=""):
        print("Bot llamado")
        response = self.client.chat.completions.create(
            temperature=self.temperature,
            model="gpt-4-1106-preview",
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

    # Probably this method could replace every upper method
    def query_LLM(
        self, query_name, data, has_cleanup=True, has_analysis=True, list_of_series=[]
    ):
        query = self.queries.get(query_name)
        response = ""

        if has_cleanup:
            CLEANUP_MESSAGE = query.get("cleanup")
            response = self._complete_response(data, CLEANUP_MESSAGE)
            data = response.choices[0].message.content

        if has_analysis:
            ANALYSIS_MESSAGE = query.get("analysis")
            response = self._complete_response(
                data
                + "also you have to make sure to use the following list of names for the series"
                + str(list_of_series),
                ANALYSIS_MESSAGE,
            )

        return response.choices[0].message.content