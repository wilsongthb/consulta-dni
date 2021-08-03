# servicio de consulta de DNI
```
pip install -r requirements.txt
export FLASK_APP=buscador-dni.py && flask run
```

# ejecutar con pm2
```
pm2 start 'export FLASK_APP=buscador-dni.py && ~/.local/bin/flask run -p PUERTO -h 0.0.0.0'
```
