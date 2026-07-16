from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET', 'POST'])
def handle_request():

    if request.method == 'GET':
        return "Bot is running!", 200

    payload = request.get_json(force=True)

    app.logger.info("========== PAYLOAD ==========")
    app.logger.info(payload)

    return jsonify({
        "text": "Hello from Render!"
    }), 200
