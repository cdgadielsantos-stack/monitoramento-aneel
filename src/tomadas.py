from bs4 import BeautifulSoup
from datetime import datetime


def buscar_tomadas(html):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    tomadas = []

    links = soup.find_all("a")

    for link in links:

        titulo = link.find("h5")

        if not titulo:
            continue

        numero = titulo.get_text(strip=True)

        if not numero.startswith("Tomada"):
            continue

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

        href = link.get("href")

        tomadas.append({
            "tipo": "TS",
            "numero": numero,
            "objeto": objeto,
            "link": href,
            "data_coleta": datetime.now().strftime("%Y-%m-%d")
        })

    return tomadas