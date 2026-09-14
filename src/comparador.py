import pandas as pd
from pathlib import Path


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ARQUIVO_HISTORICO = BASE_DIR / "dados" / "historico.csv"


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

        return []

    df_historico = pd.read_csv(
        ARQUIVO_HISTORICO
    )

    novos = df_atual[
        ~df_atual["numero"].isin(
            df_historico["numero"]
        )
    ]

    df_atual.to_csv(
        ARQUIVO_HISTORICO,
        index=False
    )

    return novos.to_dict(
        orient="records"
    )