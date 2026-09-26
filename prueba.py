import socket
import requests


DOMINIO = "gacetaoficialdebolivia.gob.bo"
IP = "181.115.190.188"
RUTA = "/normas/listadonor/10"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


print("=" * 60)
print("PRUEBA DE GACETA OFICIAL DE BOLIVIA")
print("=" * 60)


# --------------------------------------------------
# 1. DNS
# --------------------------------------------------

print("\n[1] DNS")

try:
    resultado = socket.gethostbyname_ex(DOMINIO)

    print("DNS OK")
    print("Nombre:", resultado[0])
    print("IPs:", resultado[2])

except Exception as error:
    print("ERROR DNS:")
    print(repr(error))


# --------------------------------------------------
# 2. HTTP
# --------------------------------------------------

print("\n[2] HTTP - puerto 80")

URL_HTTP = f"http://{DOMINIO}{RUTA}"

try:

    respuesta = requests.get(
        URL_HTTP,
        headers=HEADERS,
        timeout=15
    )

    print("HTTP OK")
    print("Código:", respuesta.status_code)
    print("URL final:", respuesta.url)
    print("Tamaño:", len(respuesta.content))

except Exception as error:

    print("ERROR HTTP:")
    print(repr(error))


# --------------------------------------------------
# 3. HTTPS
# --------------------------------------------------

print("\n[3] HTTPS - puerto 443")

URL_HTTPS = f"https://{DOMINIO}{RUTA}"

try:

    respuesta = requests.get(
        URL_HTTPS,
        headers=HEADERS,
        timeout=15
    )

    print("HTTPS OK")
    print("Código:", respuesta.status_code)
    print("URL final:", respuesta.url)
    print("Tamaño:", len(respuesta.content))

    print("\nPrimeros 1000 caracteres:")
    print(respuesta.text[:1000])

except Exception as error:

    print("ERROR HTTPS:")
    print(repr(error))


# --------------------------------------------------
# 4. PUERTO 80
# --------------------------------------------------

print("\n[4] TCP puerto 80")

try:

    sock = socket.create_connection(
        (DOMINIO, 80),
        timeout=10
    )

    print("Puerto 80 ABIERTO")

    sock.close()

except Exception as error:

    print("Puerto 80 NO accesible:")
    print(repr(error))


# --------------------------------------------------
# 5. PUERTO 443
# --------------------------------------------------

print("\n[5] TCP puerto 443")

try:

    sock = socket.create_connection(
        (DOMINIO, 443),
        timeout=10
    )

    print("Puerto 443 ABIERTO")

    sock.close()

except Exception as error:

    print("Puerto 443 NO accesible:")
    print(repr(error))


print("\n" + "=" * 60)
print("FIN DEL DIAGNÓSTICO")
print("=" * 60)
