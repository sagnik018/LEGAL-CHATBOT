from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from utils.legal_responses import generate_response

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = generate_response(user_input)
    return jsonify({"response": response})

if __name__ == "_main_":
    app.run(debug=True, port=5000)