# http https://api.apis.net.pe/v1/dni?numero=40180182
from flask_cors import CORS
from flask import Flask, request, jsonify
import requests as http
import json
from dotenv import load_dotenv
import os
import apis

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route('/<dni>', methods=['GET'])
def default_main(dni):
    #  if request.args.get('dni'):
    if dni:
        return apis.apitec(dni)
    return ''
