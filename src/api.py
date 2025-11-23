from flask import Flask, jsonify

class Yui:
    app = Flask(__name__)
    
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "test" : "test"
        })
