from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

# Configure Google Generative AI API
GOOGLE_API_KEY = "AIzaSyAjMEIeQ0q6Pnnh9vKBH_0KUWcJ9CDNaK8"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Generative AI Chat Model
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

app = Flask(__name__)

# Route to serve the chat template
@app.route('/')
def index():
    return render_template('chat.html')

# Route to handle chat messages
@app.route('/chat', methods=['POST'])
def chat_response():
    user_input = request.json.get('message')
    
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Send user input to Google Generative AI model and get response
        response_raw = chat.send_message(user_input)
        response = response_raw.text  # Extract the response text
        return jsonify({"response": response})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

# Start Flask app
if __name__ == '__main__':
    app.run(debug=True)
