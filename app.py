from flask import Flask,render_template,request,jsonify
import google.generativeai as genai
import os
#In place of "MY-SECRET-API-KEY" I have Used my own API key for the project
GOOGLE_API_KEY = "MY-SECRET-API-KEY"  #covering this part as it is confidential 
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat',methods = ['POST'])
def chat_response():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error":"No Message Provided"}),400
    try:
        response_raw = chat.send_message(user_input)
        print(response_raw)
        response = response_raw.text
        return jsonify({"response":response})
    except Exception as e:
        print(f"Error:{e}")
        return jsonify({"error":str(e)}),500

if __name__ == '__main__':
    app.run(debug=True)
