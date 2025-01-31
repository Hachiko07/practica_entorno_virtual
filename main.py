# -*- coding: utf-8 -*-

import requests

response = requests.get("https://api.github.com")
if response.status_code == 200:
    print("¡Conexión exitosa a la API de GitHub!")
else:
    print("Algo salió mal:", response.status_code)

