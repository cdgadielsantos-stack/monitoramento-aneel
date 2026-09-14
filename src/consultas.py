from bs4 import BeautifulSoup
from datetime import datetime


def buscar_consultas(html):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    consultas = []

    links = soup.find_all("a")

    for link in links:

        titulo = link.find("h5")

        if not titulo:
            continue

        numero = titulo.get_text(
            strip=True
        )

        if not numero.startswith("Consulta"):
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

        consultas.append({
            "tipo": "CP",
            "numero": numero,
            "objeto": objeto,
            "link": href,
            "data_coleta": datetime.now().strftime("%Y-%m-%d")
        })

    return consultas