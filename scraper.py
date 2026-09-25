import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from datetime import datetime
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


URL = "https://gacetaoficialdebolivia.gob.bo/normas/listadonor/10"


headers = {
    "User-Agent": "Mozilla/5.0 RSS Bot"
}


# Sesión con reintentos
session = requests.Session()

retry = Retry(
    total=5,
    backoff_factor=5,
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(max_retries=retry)

session.mount("https://", adapter)
session.mount("http://", adapter)


try:

    print("Descargando:", URL)

    respuesta = session.get(
        URL,
        headers=headers,
        timeout=30
    )

    respuesta.raise_for_status()

    print("Código HTTP:", respuesta.status_code)


except Exception as error:

    print("Error al descargar la página:")
    print(error)

    raise SystemExit(1)



soup = BeautifulSoup(
    respuesta.text,
    "html.parser"
)



fg = FeedGenerator()


fg.title(
    "Gaceta Oficial Bolivia - Normas"
)


fg.link(
    href="https://TUUSUARIO.github.io/rss-gaceta-bolivia/feed.xml"
)


fg.description(
    "Actualizaciones de normas de la Gaceta Oficial de Bolivia"
)



contador = 0


for elemento in soup.find_all("h3")[:20]:

    titulo = elemento.get_text(strip=True)

    if titulo:

        entrada = fg.add_entry()

        entrada.title(titulo)

        entrada.description(
            "Nueva publicación de la Gaceta Oficial de Bolivia"
        )

        entrada.link(
            href=URL
        )

        entrada.pubDate(
            datetime.now()
        )

        contador += 1



print("Entradas creadas:", contador)



fg.rss_file(
    "feed.xml"
)


print("RSS generado correctamente")
