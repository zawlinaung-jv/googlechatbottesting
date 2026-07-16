from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    payload = request.get_json(silent=True) # JSON ကို အမှားမပါအောင် ဖတ်ပါ
    
    # Payload မရှိရင် Error မတက်အောင် စစ်ပါ
    if not payload:
        return jsonify({"text": "Hello, I am running!"})
    
    event_type = payload.get('type')
    
    if event_type == 'MESSAGE':
        message_data = payload.get('message', {})
        user_text = message_data.get('text', '')
        
        return jsonify({
            "text": f"Hello! သင်ပြောတာကို ကျွန်တော်လက်ခံရရှိပါပြီ: {user_text}"
        })
    
    elif event_type == 'ADDED_TO_SPACE':
        return jsonify({
            "text": "မင်္ဂလာပါ! ကျွန်တော်နဲ့ စကားပြောဖို့ အဆင်သင့်ဖြစ်ပါပြီ။"
        })
    
    return jsonify({"text": "Hello, I am your bot!"})

# if __name__ == '__main__': အပိုင်းကို ဖယ်လိုက်ပါ
# Gunicorn က Dockerfile ထဲက CMD အတိုင်း သူ့ဟာသူ ခေါ်ယူသွားပါလိမ့်မယ်။