from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/", methods=["GET", "POST"])
def handle_request():
    if request.method == "GET":
        return "Bot is running!", 200

    app.logger.info("Headers: %s", dict(request.headers))
    app.logger.info("Body: %s", request.get_data(as_text=True))

    return jsonify({
        "text": "Hello from Render!"
    }), 200
