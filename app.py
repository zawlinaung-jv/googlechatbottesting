from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    payload = request.json
    
    # 1. Event Type ကို အရင်စစ်ဆေးပါ
    event_type = payload.get('type')
    
    # 2. User က Message ပို့လာတဲ့အခါ
    if event_type == 'MESSAGE':
        # 'message' key ရှိမရှိ သေချာအောင် စစ်ဆေးခြင်း
        message_data = payload.get('message', {})
        user_text = message_data.get('text', '')
        
        # သင့် Bot ရဲ့ တုံ့ပြန်မှု
        return jsonify({
            "text": f"Hello! သင်ပြောတာကို ကျွန်တော်လက်ခံရရှိပါပြီ: {user_text}"
        })
    
    # 3. Bot ကို Space ထဲ Add လုပ်လိုက်တဲ့အခါ (Added to space)
    elif event_type == 'ADDED_TO_SPACE':
        return jsonify({
            "text": "မင်္ဂလာပါ! ကျွန်တော်နဲ့ စကားပြောဖို့ အဆင်သင့်ဖြစ်ပါပြီ။"
        })
    
    # တခြား event များအတွက်
    return jsonify({"text": "Hello, I am your bot!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)