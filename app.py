import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'HEAD'])
def handle_request():
    # 1. Render ရဲ့ Health Check အတွက် (HEAD method)
    if request.method == 'HEAD':
        return "", 200
    
    # 2. Browser ကနေစမ်းသပ်ဖို့ (GET method)
    if request.method == 'GET':
        return "Bot is running perfectly!"
    
    # 3. Google Chat ကလာမယ့် စာတွေအတွက် (POST method)
    payload = request.get_json(silent=True)
    
    if payload and payload.get('type') == 'MESSAGE':
        message_data = payload.get('message', {})
        user_text = message_data.get('text', '')
        return jsonify({
            "text": f"Hello! သင်ပြောတာကို ကျွန်တော်လက်ခံရရှိပါပြီ: {user_text}"
        })
    
    # တခြား event များအတွက်
    return jsonify({"text": "Hello, I am your bot!"})

if __name__ == '__main__':
    # Render ပေးတဲ့ PORT ကို အလိုအလျောက်ရယူခြင်း
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
