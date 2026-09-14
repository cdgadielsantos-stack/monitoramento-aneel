from dataclasses import dataclass


@dataclass
class ProcessoRegulatorio:
    tipo: str
    numero: str
    descricao: str
    link: str