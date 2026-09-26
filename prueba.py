import requests

URL = "http://gacetaoficialdebolivia.gob.bo/normas/listadonor/10"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    respuesta = requests.get(
        URL,
        headers=headers,
        timeout=30
    )

    print("Código HTTP:", respuesta.status_code)
    print("URL final:", respuesta.url)
    print("Primeros 500 caracteres:")
    print(respuesta.text[:500])

except Exception as e:
    print("Error de conexión:")
    print(e)
