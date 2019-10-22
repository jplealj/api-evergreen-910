from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers.Mediciones import Mediciones

app = Flask(__name__)
CORS(app)

@app.route('/Mediciones', methods=['GET'])
def getAll():
    return (Mediciones.list())

@app.route('/Mediciones', methods=['POST'])
def postOne():
    print("5")
    body = request.json
    return (Mediciones.create(body))

