from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    # 1. GET request ဖြစ်ရင် (Browser ကနေဖွင့်ရင်)
    if request.method == 'GET':
        return "Bot is running perfectly!"
    
    # 2. POST request ဖြစ်ရင် (Google Chat ကနေလာရင်)
    # silent=True ကိုသုံးရင် JSON မဟုတ်ရင်လည်း Error မတက်တော့ပါဘူး
    payload = request.get_json(silent=True)
    
    if not payload:
        return jsonify({"text": "Invalid request"})

    event_type = payload.get('type')
    
    if event_type == 'MESSAGE':
        message_data = payload.get('message', {})
        user_text = message_data.get('text', '')
        return jsonify({
            "text": f"Hello! သင်ပြောတာကို ကျွန်တော်လက်ခံရရှိပါပြီ: {user_text}"
        })
    
    return jsonify({"text": "Hello, I am your bot!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
