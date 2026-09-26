import socket
import requests


DOMINIO = "gacetaoficialdebolivia.gob.bo"
IP = "181.115.190.188"
RUTA = "/normas/listadonor/10"

URL = f"http://{DOMINIO}{RUTA}"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


print("=" * 60)
print("PRUEBA DE GACETA OFICIAL DE BOLIVIA")
print("=" * 60)


# --------------------------------------------------
# 1. PROBAR DNS
# --------------------------------------------------

print("\n[1] Probando DNS...")
print("Dominio:", DOMINIO)

try:
    resultado = socket.gethostbyname_ex(DOMINIO)

    print("DNS OK")
    print("Nombre:", resultado[0])
    print("Alias:", resultado[1])
    print("IPs:", resultado[2])

except Exception as error:
    print("ERROR DNS:")
    print(repr(error))


# --------------------------------------------------
# 2. PROBAR CONEXIÓN HTTP POR DOMINIO
# --------------------------------------------------

print("\n[2] Probando HTTP mediante dominio...")
print("URL:", URL)

try:
    respuesta = requests.get(
        URL,
        headers=HEADERS,
        timeout=30
    )

    print("CONEXIÓN OK")
    print("Código HTTP:", respuesta.status_code)
    print("URL final:", respuesta.url)
    print("Tamaño:", len(respuesta.content), "bytes")

    print("\nPrimeros 500 caracteres:")
    print(respuesta.text[:500])

except Exception as error:
    print("ERROR HTTP:")
    print(repr(error))


# --------------------------------------------------
# 3. PROBAR CONEXIÓN DIRECTA A LA IP
# --------------------------------------------------

print("\n[3] Probando conexión directa a la IP...")
print("IP:", IP)

URL_IP = f"http://{IP}{RUTA}"

try:
    respuesta_ip = requests.get(
        URL_IP,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Host": DOMINIO
        },
        timeout=30
    )

    print("CONEXIÓN POR IP OK")
    print("Código HTTP:", respuesta_ip.status_code)
    print("URL:", respuesta_ip.url)
    print("Tamaño:", len(respuesta_ip.content), "bytes")

    print("\nPrimeros 500 caracteres:")
    print(respuesta_ip.text[:500])

except Exception as error:
    print("ERROR CONEXIÓN POR IP:")
    print(repr(error))


# --------------------------------------------------
# 4. INFORMACIÓN FINAL
# --------------------------------------------------

print("\n" + "=" * 60)
print("FIN DE LA PRUEBA")
print("=" * 60)
