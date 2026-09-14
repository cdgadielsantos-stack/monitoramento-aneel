from navegador import obter_html
from consultas import buscar_consultas
from audiencias import buscar_audiencias
from tomadas import buscar_tomadas
from comparador import detectar_novidades
from datetime import datetime
from bs4 import BeautifulSoup


URL_AUDIENCIAS = (
    "https://antigo.aneel.gov.br/"
    "audiencias-publicas"
)

URL_CONSULTAS = (
    "https://antigo.aneel.gov.br/"
    "web/guest/consultas-publicas"
)

URL_TOMADAS = (
    "https://antigo.aneel.gov.br/"
    "web/guest/tomadas-de-subsidios"
)


def executar_monitoramento():

    print(
        "Iniciando monitoramento..."
    )
    

    html_ap = obter_html(
        URL_AUDIENCIAS
    )

    audiencias = buscar_audiencias(
        html_ap
    )

    html_cp = obter_html(
        URL_CONSULTAS
    )

    consultas = buscar_consultas(
        html_cp
    )

    html_ts = obter_html(
    URL_TOMADAS
    )

    tomadas = buscar_tomadas(
        html_ts
    )

    registros = []

    registros.extend(audiencias)
    registros.extend(consultas)
    registros.extend(tomadas)

    novidades = detectar_novidades(
        registros
    )

    if novidades:

        print(
            "\nNovidades encontradas:"
        )

        for item in novidades:
            print(item)

    else:

        print(
            "\nNenhuma novidade."
        )


if __name__ == "__main__":
    executar_monitoramento()

