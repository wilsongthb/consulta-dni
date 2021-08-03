# importamos requests
import requests

# consultamos el dni
dni = input('indica el DNI?: ')

try:
    # realizamos la consulta a la api
    result = requests.get(f'https://api.apis.net.pe/v1/dni?numero={dni}')
    # convertimos el resultado a un diccionario
    jsonedResponse = result.json()
    print("Se llama : " + jsonedResponse['nombre'])
except:
    print("no obtuve resultados :(")
