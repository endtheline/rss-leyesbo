import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from datetime import datetime

URL = "http://www.gacetaoficialdebolivia.gob.bo/normas/listadonor/10"

headers = {
    "User-Agent": "Mozilla/5.0 RSS Bot"
}

respuesta = requests.get(URL, headers=headers, timeout=30)

soup = BeautifulSoup(respuesta.text, "html.parser")

fg = FeedGenerator()

fg.title("Gaceta Oficial Bolivia - Normas")
fg.link(
    href="https://TUUSUARIO.github.io/rss-gaceta-bolivia/feed.xml"
)

fg.description(
    "Actualizaciones de normas de la Gaceta Oficial de Bolivia"
)

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

        entrada.pubDate(datetime.now())


fg.rss_file("feed.xml")
