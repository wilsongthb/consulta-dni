# http https://api.apis.net.pe/v1/dni?numero=40180182
from flask_cors import CORS
from flask import Flask, request, jsonify
import requests as http
import json


app = Flask(__name__)
CORS(app)


@app.route('/<dni>', methods=['GET'])
def default_main(dni):
    #  if request.args.get('dni'):
    if dni:
        #  dni = request.args.get('dni')
        #  r = http.get(f'https://api.apis.net.pe/v1/dni?numero=40180182')

        try:
            #  dni = '01784547'
            token = 'apis-token-704.-xNqHkxR3NWNMFFRUASsH8aRfkSgCNz2'
            result = http.get(f'https://api.apis.net.pe/v1/dni?numero={dni}', {
                "headers": {
                    "Authorization": "Bearer {token}"
                    }
                })
            #  jsonedResponse = json.loads(result.text)
            jsonedResponse = result.json()
            nombreContribuyente = jsonedResponse['nombre'].split(' ')
            nombreFinal = jsonedResponse['nombre']
            if len(nombreContribuyente) >= 3:
                nombres = ' '.join(nombreContribuyente[2:])
                nombreFinal = f'{nombres} {nombreContribuyente[0]} {nombreContribuyente[1]}'
            responseData = {
                'nombre': nombreFinal,
                'apellidos_nombres': jsonedResponse['nombre'],
                'numeroDocumento': dni
            }
            return jsonify(responseData)
            #  return jsonify(jsonedResponse)
        except:
            return jsonify({
                'message': 'No lo encontre :/',
                'code': '1'
            }), 404
    return ''
