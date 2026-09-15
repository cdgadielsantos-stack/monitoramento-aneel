import time

inicio = time.time()

from datetime import datetime
from navegador import obter_html
from consultas import buscar_consultas
from audiencias import buscar_audiencias
from tomadas import buscar_tomadas
from comparador import detectar_novidades
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

    fim = time.time()
        
    tempo_execucao = round(
        fim - inicio,
        2
    )

    with open(
        "logs/monitor.log",
        "a",
        encoding="utf-8"
    ) as log:

        log.write("\n" + "=" * 50 + "\n")

        log.write(
            f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        )

        log.write(
            f"AP encontradas: {len(audiencias)}\n"
        )

        log.write(
            f"CP encontradas: {len(consultas)}\n"
        )

        log.write(
            f"TS encontradas: {len(tomadas)}\n"
        )

        log.write(
            f"Total registros: {len(registros)}\n"
        )

        log.write(
            f"Novidades: {len(novidades)}\n"
        )

        log.write(
            "Status: SUCESSO\n"
        )

        log.write("\n" + "=" * 50 + "\n")

        log.write(
            f"Tempo de execução: {tempo_execucao}s\n"
        )

        log.write(
            "Fontes monitoradas:\n"
        )

        log.write(
            "AP, CP e TS da ANEEL\n"
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