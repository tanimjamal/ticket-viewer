"""
Main module for the flask app
"""

from flask import Flask, send_from_directory
from flask_restful import Api, Resource

# Initializes the flask app
app = Flask(__name__, static_url_path="", static_folder="./build")
api = Api(app)


@app.route("/", defaults={"path": ""})
def serve(path):
    return send_from_directory(app.static_folder, "index.html")


api.add_resource(HelloApiHandler, "/flask/hello")

if __name__ == "__main__":
    app.run()
