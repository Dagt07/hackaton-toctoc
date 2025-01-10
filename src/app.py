from flask import Flask, render_template, request, jsonify
from main import extract_data_from_message

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

# Lista para almacenar el historial del chat
chat_history = []
user_prompts = ""

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/send_message", methods=["POST"])
def send_message():
    global chat_history
    global user_prompts

    # Obtener el mensaje del usuario del cuerpo de la solicitud
    user_message = request.json.get("message", "")

    # Guardar el mensaje del usuario en el historial
    chat_history.append({"role": "user", "message": user_message})
    user_prompts += user_message + " "

    try:
        # Extraer la información del mensaje del usuario
        data = extract_data_from_message(user_prompts)
        bot_response = data
    except Exception as e:
        print(e)
        bot_response = "An error occurred while processing the message. Please try again."


    chat_history.append({"role": "bot", "message": bot_response})

    # Devolver la respuesta del bot como JSON
    return jsonify({"response": bot_response, "chat_history": chat_history})

if __name__ == "__main__":
    app.run(debug=True)
