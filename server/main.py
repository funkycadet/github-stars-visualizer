#!/usr/bin/env python3
"""
Main module which calls the flask environment and program logic
"""
from app import app
from flask import Flask, jsonify


server = Flask(__name__)
server.register_blueprint(app)

@server.errorhandler(404)
def error404(error):
    """error 404 handler"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5000
    server.run(host=host, port=port, threaded=True)
