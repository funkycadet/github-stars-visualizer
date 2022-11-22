#!/usr/bin/env python3
"""
Main module which calls the flask environment and program logic
"""
from app import app
from flask import Flask, jsonify
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


sentry_sdk.init(
    dsn="https://931c99850545422d884595637d052617@o4504176793747456.ingest.sentry.io/4504176806133764",
    integrations=[
        FlaskIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=0
)

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
