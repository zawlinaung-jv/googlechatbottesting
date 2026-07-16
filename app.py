from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def handle_request():

    print("Method:", request.method)
    print("Headers:", dict(request.headers))
    print("Content-Type:", request.content_type)
    print("Content-Length:", request.content_length)
    print("Raw Body:", request.get_data(as_text=True))

    if request.method == "GET":
        return "Bot is running!", 200

    return jsonify({
        "text": "Hello from Render!"
    }), 200
