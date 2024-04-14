from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Assuming you've safely stored your OpenAI API key in an environment variable or a secure place
openai.api_key = 'YOUR API KEY'

@app.route("/")
def index():
    return render_template('chat.html')  # Ensure you have this HTML file in a 'templates' folder

@app.route("/get", methods=["POST"])
def chat():
    user_message = request.form["msg"]
    chat_response = get_chat_response(user_message)
    return jsonify({"response": chat_response})

def get_chat_response(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Adjust model as necessary
            messages=[
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, I couldn't process that request."

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
