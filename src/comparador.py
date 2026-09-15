import pandas as pd
from pathlib import Path


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ARQUIVO_HISTORICO = BASE_DIR / "dados" / "historico.csv"
ARQUIVO_NOVOS = BASE_DIR / "dados" / "novos.csv"

def detectar_novidades(registros):

    df_atual = pd.DataFrame(registros)

    if (
        not Path(ARQUIVO_HISTORICO).exists()
        or Path(ARQUIVO_HISTORICO).stat().st_size == 0
    ):

        df_atual.to_csv(
            ARQUIVO_HISTORICO,
            index=False
        )

        pd.DataFrame(
            columns=df_atual.columns
        ).to_csv(
            ARQUIVO_NOVOS,
            index=False
        )

        return []

    df_historico = pd.read_csv(
        ARQUIVO_HISTORICO
    )

    novos = df_atual[
        ~df_atual["numero"].isin(
            df_historico["numero"]
        )
    ]

    novos.to_csv(
        ARQUIVO_NOVOS,
        index=False
    )

    df_atual.to_csv(
        ARQUIVO_HISTORICO,
        index=False
    )

    return novos.to_dict(
        orient="records"
    )

    if not novos.empty:

        novos.to_csv(
            ARQUIVO_NOVOS,
            index=False
        )

    else:

        pd.DataFrame().to_csv(
            ARQUIVO_NOVOS,
            index=False
        )

    df_atual.to_csv(
        ARQUIVO_HISTORICO,
        index=False
    )

    return novos.to_dict(
        orient="records"
    )