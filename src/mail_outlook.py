import win32com.client
from datetime import datetime
from html import escape


def enviar_email_novidades(novidades):

    outlook = win32com.client.Dispatch(
        "Outlook.Application"
    )

    email = outlook.CreateItem(0)

    email.BodyFormat = 2

    email.To = "gadiel.caminos@light.com.br"

    quantidade = len(novidades)

    if quantidade == 1:
        assunto = (
            "🚨 Monitor ANEEL | 1 nova publicação identificada"
        )
    else:
        assunto = (
            f"🚨 Monitor ANEEL | {quantidade} novas publicações identificadas"
        )

    email.Subject = assunto

    data_deteccao = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

    html = f"""
<!DOCTYPE html>
<html>

<head>
<meta charset="UTF-8">
<title>Monitor ANEEL</title>
</head>

<body style="
    margin:0;
    padding:30px;
    background-color:#F2F2F2;
    font-family:'Segoe UI', Arial, sans-serif;
">

<table width="100%" cellpadding="0" cellspacing="0">
<tr>
<td align="center">

<table width="800"
       cellpadding="0"
       cellspacing="0"
       style="
            background:white;
            border-radius:12px;
            overflow:hidden;
       ">

<tr>
<td style="
    background-color:#F58220;
    color:white;
    padding:20px 25px;
">

<h1 style="
    margin:0;
    font-size:32px;
">
⚡ Monitor Regulatório ANEEL
</h1>

<p style="
    margin-top:8px;
    font-size:15px;
">
Monitoramento automatizado de Audiências Públicas,
Consultas Públicas e Tomadas de Subsídios.
</p>

</td>
</tr>

<tr>
<td style="padding:25px;">

<p style="font-size:16px;">

Prezados,

<br><br>

O Monitor Regulatório ANEEL identificou
<strong>{quantidade}</strong>
{"nova publicação" if quantidade == 1 else "novas publicações"}.

<br><br>

Recomenda-se avaliar a pertinência do tema para sua área
e, quando aplicável, a participação no respectivo
processo regulatório.

</p>

<p>

<strong>
Data da detecção:
</strong>

{data_deteccao}

</p>

<hr>
"""

    for item in novidades:

        tipo = escape(
            str(item.get("tipo", ""))
        )

        numero = escape(
            str(item.get("numero", ""))
        )

        objeto = escape(
            str(item.get("objeto", ""))
        )

        link_original = str(
            item.get("link", "")
        ).strip()

        link = escape(
            link_original,
            quote=True
        )

        cor = "#0078D4"

        if tipo == "AP":
            cor = "#28A745"

        elif tipo == "CP":
            cor = "#F2C811"

        elif tipo == "TS":
            cor = "#0078D4"

        html += f"""
<table width="100%"
       cellpadding="0"
       cellspacing="0"
       style="
            border:1px solid #D9D9D9;
            border-radius:12px;
            margin-top:20px;
       ">

<tr>
<td style="
    background:{cor};
    color:white;
    padding:14px;
    font-size:18px;
    font-weight:bold;
">

{tipo} | {numero}

</td>
</tr>

<tr>
<td style="
    padding:20px;
">

<p style="
    margin-top:0;
    font-weight:bold;
">
Objeto
</p>

<div style="
    background:#FFF8E8;
    border-left:5px solid #F58220;
    padding:15px;
    line-height:1.6;
">

{objeto}

</div>

<br>

{link}

🔗 Abrir Publicação

</a>

<p style="
    margin-top:20px;
">

<strong>
Link direto:
</strong>

<br><br>

{link}

{link}

</a>

</p>

</td>
</tr>

</table>
"""

    html += """
<br>

<hr>

<p style="
    color:#777777;
    font-size:12px;
">

Mensagem gerada automaticamente pelo
<strong>Monitor Regulatório ANEEL</strong>.

</p>

<p style="
    color:#777777;
    font-size:12px;
">

Objetivo:
ampliar a disseminação interna de informações
regulatórias e apoiar a participação em
Audiências Públicas, Consultas Públicas e
Tomadas de Subsídios.

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

    # Quando estiver validado:
    # email.Send()


if __name__ == "__main__":

    novidades_teste = [
        {
            "tipo": "CP",
            "numero": "Consulta 027/2026",
            "objeto": (
                "Obter subsídios para aprimorar "
                "a proposta referente à "
                "Revisão Tarifária Periódica de 2026."
            ),
            "link": "https://www.aneel.gov.br"
        }
    ]

    enviar_email_novidades(
        novidades_teste
    )