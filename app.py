import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'GET':
        return "Bot is running perfectly!"
    
    # POST request logic...
    payload = request.get_json(silent=True)
    if payload and payload.get('type') == 'MESSAGE':
        user_text = payload.get('message', {}).get('text', '')
        return jsonify({"text": f"Hello! ရရှိပါပြီ: {user_text}"})
    
    return jsonify({"text": "Hello, I am your bot!"})

if __name__ == '__main__':
    # Render ပေးတဲ့ PORT ကို ရှာခိုင်းပြီး အဲ့ဒီ port မှာ run ပါ
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
