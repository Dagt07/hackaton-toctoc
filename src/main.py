import json

from bot_llm.response_ai import ResponseAI

def extract_data_from_message(data):
    bot = ResponseAI()
    
    answer = bot.first_stage(
        data = data,
    )

    if (answer) == "":
        answer = "{Error: No Answer}"

    return json.loads(answer)

if __name__ == "__main__":
    data = "Hola, quiero tasar una propiedad"
    print(extract_data_from_message(data))