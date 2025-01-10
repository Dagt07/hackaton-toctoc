import json

from bot_llm.response_ai import ResponseAI

def extract_data_from_message(data):
    bot = ResponseAI()
    
    answer = bot.first_stage(
        data = data,
    )

    if (answer) == "":
        answer = "{Error: No Answer}"

    print(answer)
    return None

if __name__ == "__main__":
    data = "Hola, necesito saber cuanto vale mi casa"
    print(extract_data_from_message(data))