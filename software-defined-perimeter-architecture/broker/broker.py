from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "component": "SDP Broker",
        "status": "active",
        "message": "Broker is coordinating trusted access requests"
    })

@app.route("/authenticate")
def authenticate():
    client_ip = request.headers.get("X-Real-IP", request.remote_addr)
    return jsonify({
        "authenticated": True,
        "client_ip": client_ip,
        "policy": "trusted_connection_allowed"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
