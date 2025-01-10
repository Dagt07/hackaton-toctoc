import json

from bot_llm.response_ai import ResponseAI

def extract_data_from_message(data):
    bot = ResponseAI()
    
    answer = bot.first_stage(
        data = data,
    )

    if (answer) == "":
        answer = "{Error: No Answer}"

    return answer

if __name__ == "__main__":
    data = "Hola, necesito buscar una casa"
    print(extract_data_from_message(data))