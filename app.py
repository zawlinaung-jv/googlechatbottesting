from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    # Render ၏ Health Check အတွက် GET ကို စစ်ဆေးခြင်း
    if request.method == 'GET':
        return "Bot is running!", 200
        
    # Google Chat မှ ပို့သော POST Request များကို ကိုင်တွယ်ခြင်း
    payload = request.get_json(silent=True)
    
    if not payload:
        return jsonify({"text": "No payload received"})
        
    event_type = payload.get('type')
    
    if event_type == 'MESSAGE':
        user_text = payload.get('message', {}).get('text', '')
        return jsonify({
            "text": f"လက်ခံရရှိပါပြီ: {user_text}"
        })
    
    elif event_type == 'ADDED_TO_SPACE':
        return jsonify({
            "text": "မင်္ဂလာပါ! စကားပြောဖို့ အဆင်သင့်ဖြစ်ပါပြီ။"
        })
    
    return jsonify({"text": "Hello!"})

# app.run(...) လိုင်းကို ဖယ်ထုတ်ထားပါ