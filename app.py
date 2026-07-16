from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def handle_request():
    print("========== NEW REQUEST ==========")
    print("Method:", request.method)
    print("Headers:", dict(request.headers))
    print("Raw Body:", request.get_data(as_text=True))

    # Health Check
    if request.method == "GET":
        return "Bot is running!", 200

    # JSON Parse
    payload = request.get_json(silent=True)
    print("Payload:", payload)

    if not payload:
        return jsonify({"text": "No payload received"}), 200

    event_type = payload.get("type")
    print("Event Type:", event_type)

    if event_type == "MESSAGE":
        user_text = payload.get("message", {}).get("text", "")
        print("User Text:", user_text)

        return jsonify({
            "text": f"လက်ခံရရှိပါပြီ: {user_text}"
        }), 200

    elif event_type == "ADDED_TO_SPACE":
        print("Bot added to a space")

        return jsonify({
            "text": "မင်္ဂလာပါ! စကားပြောဖို့ အဆင်သင့်ဖြစ်ပါပြီ။"
        }), 200

    print("Unknown event")

    return jsonify({
        "text": "Hello!"
    }), 200
