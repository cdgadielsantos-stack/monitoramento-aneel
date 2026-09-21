# teste_email_novidades.py

import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from mail_outlook import enviar_email_novidades

novidades = [
    {
        "tipo": "CP",
        "numero": "Consulta 027/2026",
        "objeto": "Obter subsídios para aprimorar a proposta referente à Revisão Tarifária Periódica de 2026.",
        "link": "https://www.aneel.gov.br"
    }
]

enviar_email_novidades(
    novidades
)