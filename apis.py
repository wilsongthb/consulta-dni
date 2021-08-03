from flask import request, jsonify
import requests as http
import json


def apisnet(dni, token=''):
    """
    Api de consulta libre
    url: https://apis.net.pe/
    token: APIS_NET_TOKEN
    """
    try:
        result = http.get(f'https://api.apis.net.pe/v1/dni?numero={dni}', headers={
            "Authorization": "Bearer {token}"
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
            'dni': dni
        }
        return jsonify(responseData)
        #  return jsonify(jsonedResponse)
    except:
        return jsonify({
            'message': 'No lo encontre :/',
            'code': '1'
        }), 404


def apifacturacion(dni, token):
    """
    api
    """
    try:
        result = http.post(f"https://api.apifacturacion.com/dni/{dni}", data={
            "token": token
        })
        jsonedResponse = result.json()
        nombreSeparado = jsonedResponse['cliente'].split(' ')
        apellidosNombres = ''
        if len(nombreSeparado) >= 3:
            nombres = ' '.join(nombreSeparado[:-2])
            apellidosNombres = f"{nombreSeparado[-2]} {nombreSeparado[-1]} {nombres}"
        responseData = {
            'nombre': jsonedResponse['cliente'],
            'apellidos_nombres': apellidosNombres,
            'dni': dni
        }
        return jsonify(responseData)
    except:
        return jsonify({
            'message': 'No lo encontre :/',
            'code': '1'
        }), 404
