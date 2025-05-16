from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://unique-kleicha-411291.netlify.app/"])

PISTON_URL = "https://emkc.org/api/v2/piston/execute"

EXTENSIONS = {
    "python": "py",
    "javascript": "js",
    "cpp": "cpp"
}

@app.route("/run", methods=["POST"])
def run_code():
    data = request.json
    language = data.get("language", "python")
    code = data.get("code", "")

    try:
        filename = f"main.{EXTENSIONS.get(language, 'txt')}"
        response = requests.post(PISTON_URL, json={
            "language": language,
            "version": "*",
            "files": [{"name": filename, "content": code}]
        })
        result = response.json()
        return jsonify({"output": result.get("run", {}).get("output", "No output")})
    except Exception as e:
        return jsonify({"output": str(e)}), 500
