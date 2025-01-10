import json

from bot_llm.response_ai import ResponseAI
bot = ResponseAI()
def extract_data_from_message(data, intent = ""):
    if (intent) != "":
        answer = bot.query_LLM(
            query_name = intent,
            data = data,
        )
    return answer
def extract_data_ft_message(data):
    answer = bot.first_stage(data)
    return answer 

