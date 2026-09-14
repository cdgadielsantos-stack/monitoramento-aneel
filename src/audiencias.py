from bs4 import BeautifulSoup
from datetime import datetime


def buscar_audiencias(html):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    audiencias = []

    links = soup.find_all("a")

    for link in links:

        titulo = link.find(
            "h5",
            class_="titulo-audiencia"
        )

        if not titulo:
            continue

        numero = titulo.get_text(
            strip=True
        )

        objeto = link.get_text(
            " ",
            strip=True
        )

        objeto = (
            objeto
            .replace(numero, "")
            .replace("Objeto", "")
            .strip()
        )

        objeto = (
            objeto
            .replace(numero, "")
            .replace("Objeto", "")
            .strip()
        )

        href = link.get("href")

        audiencias.append({
            "tipo": "AP",
            "numero": numero,
            "objeto": objeto,
            "link": href,
            "data_coleta": datetime.now().strftime("%Y-%m-%d")
        })

    return audiencias