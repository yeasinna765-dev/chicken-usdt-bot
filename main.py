import os
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder=".")

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/api/status", methods=["GET"])
def status():
    return jsonify({"status": "running", "game": "CHICKEN USDT"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
