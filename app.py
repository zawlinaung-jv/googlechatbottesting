from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_request():
    payload = request.json
    # Google Chat ကနေ message ဝင်လာတဲ့အခါ
    if payload.get('type') == 'MESSAGE':
        user_text = payload['message']['text']
        return jsonify({"text": f"Hello! သင်ပြောတာကို ကျွန်တော်လက်ခံရရှိပါပြီ: {user_text}"})
    
    return jsonify({"text": "Hello, I am your bot!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)