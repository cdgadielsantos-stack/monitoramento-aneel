import win32com.client

from datetime import datetime
from html import escape
from pathlib import Path


def enviar_email_novidades(novidades):

    outlook = win32com.client.Dispatch(
        "Outlook.Application"
    )

    email = outlook.CreateItem(0)

    email.BodyFormat = 2

    # ======================================
    # BANNER
    # ======================================

    banner_path = (
        Path(__file__).resolve().parent.parent
        / "assets"
        / "banner_monitor.png"
    )

    banner = email.Attachments.Add(
        str(banner_path)
    )

    banner.PropertyAccessor.SetProperty(
        "http://schemas.microsoft.com/mapi/proptag/0x3712001F",
        "banner_monitor"
    )

    # ======================================
    # DESTINATÁRIO
    # ======================================

    email.To = "gadiel.caminos@light.com.br"

    quantidade = len(novidades)

    email.Subject = (
        f"🚨 Monitor ANEEL | {quantidade} nova(s) publicação(ões)"
    )

    html = f"""
<!DOCTYPE html>

<html>

<body style="
    margin:0;
    padding:0;
    background:#D9FF15;
    font-family:Segoe UI, Arial, sans-serif;
">

<table
width="100%"
cellpadding="0"
cellspacing="0"
style="
    background:#D9FF15;
">

<tr>
<td align="center">

<table
width="900"
cellpadding="0"
cellspacing="0">

<tr>
<td>

cid:banner_monitor

</td>
</tr>

<tr>
<td
style="
    padding-top:25px;
">

<table
width="100%"
cellpadding="0"
cellspacing="0"
style="
    background:#F4F4F4;
    border-radius:28px;
">

<tr>
<td
style="
    padding:40px;
">
"""

    for item in novidades:

        tipo = escape(
            str(item["tipo"])
        )

        numero = escape(
            str(item["numero"])
        )

        objeto = escape(
            str(item["objeto"])
        )

        link = escape(
            str(item["link"]),
            quote=True
        )

        titulo = tipo

        if tipo == "CP":
            titulo = "CONSULTA PÚBLICA"

        elif tipo == "AP":
            titulo = "AUDIÊNCIA PÚBLICA"

        elif tipo == "TS":
            titulo = "TOMADA DE SUBSÍDIOS"

        html += f"""
<h1 style="
    margin:0;
    color:#103B35;
    font-size:64px;
    line-height:1;
    font-weight:800;
">

NOVA {titulo}
IDENTIFICADA!

</h1>

<h2 style="
    margin-top:20px;
    color:#103B35;
    font-size:58px;
    line-height:1;
    font-weight:800;
">

{tipo} | {numero}

</h2>

<p style="
    margin-top:30px;
    color:#103B35;
    font-size:22px;
    line-height:1.5;
    font-weight:600;
">

{objeto}

</p>

<br>

<p style="
    font-size:22px;
">

{link}
CLIQUE AQUI
</a>

e confira.

</p>
"""

    html += f"""

</td>
</tr>

</table>

</td>
</tr>

<tr>
<td
style="
    padding-top:25px;
    padding-bottom:30px;
">

<p style="
    color:#103B35;
    font-size:14px;
    font-weight:600;
">

Monitor Regulatório ANEEL

</p>

<p style="
    color:#103B35;
    font-size:12px;
">

Mensagem automática gerada em
{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

</p>

</td>
</tr>

</table>

</td>
</tr>

</table>

</body>
</html>
"""

    email.HTMLBody = html

    email.Display()

    # email.Send()


if __name__ == "__main__":

    novidades_teste = [
        {
            "tipo": "CP",
            "numero": "Consulta 027/2026",
            "objeto": (
                "Obter subsídios para aprimorar a proposta "
                "referente à Revisão Tarifária Periódica "
                "de 2026 da Companhia Estadual de "
                "Distribuição de Energia Elétrica."
            ),
            "link": "https://www.aneel.gov.br"
        }
    ]

    enviar_email_novidades(
        novidades_teste
    )