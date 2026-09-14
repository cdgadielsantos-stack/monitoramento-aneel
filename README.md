#  Monitoramento ANEEL (SETOR ELÉTRICO BRASILEIRO)

### Sistema automatizado de monitoramento das publicações regulatórias da ANEEL

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-Automation-45ba4b?logo=playwright&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Parsing-yellow)
![Pandas](https://img.shields.io/badge/Pandas-DataAnalysis-150458?logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-orange)



##  Descrição Executiva

O **Monitoramento ANEEL** é uma solução de automação desenvolvida em Python que realiza a coleta, o rastreamento e a comparação de publicações regulatórias divulgadas pela **Agência Nacional de Energia Elétrica (ANEEL)**.

O sistema navega de forma automatizada pelas páginas públicas da ANEEL, extrai informações estruturadas sobre **Audiências Públicas (AP)**, **Consultas Públicas (CP)** e **Tomadas de Subsídios (TS)**, armazena um histórico consolidado em formato CSV e identifica automaticamente **novas publicações** a cada execução, eliminando a necessidade de acompanhamento manual.

O projeto foi construído com foco em **modularidade**, **rastreabilidade** e **escalabilidade**, servindo como base sólida para futuras integrações com notificações, dashboards e pipelines de dados regulatórios.

---

##  Motivação do Negócio

Empresas do setor elétrico — geradoras, distribuidoras, comercializadoras, consultorias regulatórias e escritórios de advocacia energética — precisam acompanhar **constantemente** as publicações da ANEEL, pois elas impactam diretamente:

- Tarifas e receitas regulatórias
- Processos de concessão e permissão
- Obrigações de compliance regulatório
- Participação em consultas e audiências que podem alterar normas do setor

O acompanhamento manual dessas publicações é um processo **repetitivo, sujeito a falhas humanas e que consome tempo de profissionais especializados** que poderiam estar focados em análise estratégica, e não em coleta de dados.

---

##  Problema que o Projeto Resolve

| Problema | Impacto no Negócio |
|---|---|
| Monitoramento manual das páginas da ANEEL | Alto consumo de tempo e risco de perda de prazos regulatórios |
| Falta de histórico estruturado das publicações | Dificuldade de auditoria e rastreabilidade |
| Dificuldade em identificar o que é "novo" a cada verificação | Retrabalho e possibilidade de duplicidade de análise |
| Ausência de padronização dos dados coletados | Baixa qualidade para análises futuras (BI, dashboards, etc.) |

O **Monitoramento ANEEL** resolve esses problemas ao automatizar toda a cadeia de coleta, padronização, armazenamento e comparação das publicações regulatórias.

---

##  Objetivos

- ✅ Automatizar a coleta de publicações regulatórias da ANEEL
- ✅ Padronizar as informações extraídas em um formato estruturado
- ✅ Manter um histórico confiável e auditável em CSV
- ✅ Detectar automaticamente novas publicações entre execuções
- ✅ Criar uma base modular e escalável para futuras evoluções (notificações, dashboards, APIs)

---

##  Funcionalidades

| Funcionalidade | Status |
|---|---|
| Coleta automatizada de Audiências Públicas (AP) | ✅ Implementado |
| Coleta automatizada de Consultas Públicas (CP) | ✅ Implementado |
| Coleta automatizada de Tomadas de Subsídios (TS) | ✅ Implementado |
| Captura de Tipo, Número, Objeto, Link e Data da coleta | ✅ Implementado |
| Histórico consolidado em CSV | ✅ Implementado |
| Comparação entre execuções | ✅ Implementado |
| Detecção automática de novas publicações | ✅ Implementado |
| Estrutura modular do código | ✅ Implementado |
| Versionamento com Git | ✅ Implementado |

---

##  Fluxo de Funcionamento

1. O sistema é iniciado a partir do `app.py`
2. Cada módulo especializado (`audiencias.py`, `consultas.py`, `tomadas.py`) aciona o navegador automatizado
3. O `navegador.py` controla o **Playwright**, que acessa as páginas públicas da ANEEL
4. O HTML retornado é processado pelo **BeautifulSoup**, extraindo os dados relevantes
5. Os dados extraídos são estruturados via **Pandas**
6. O `comparador.py` confronta os dados atuais com o `historico.csv`
7. Novas publicações são identificadas e reportadas
8. O histórico é atualizado para a próxima execução

---

##  Arquitetura do Sistema

```
                         ┌─────────────┐
                         │   app.py    │
                         │ (Orquestra) │
                         └──────┬──────┘
                                │
             ┌──────────────────┼──────────────────┐
             │                  │                  │
     ┌───────▼──────┐   ┌───────▼──────┐   ┌───────▼──────┐
     │ audiencias.py│   │ consultas.py │   │  tomadas.py  │
     │     (AP)     │   │     (CP)     │   │     (TS)     │
     └───────┬──────┘   └───────┬──────┘   └───────┬──────┘
             │                  │                  │
             └──────────────────┼──────────────────┘
                                │
                        ┌───────▼────────┐
                        │  navegador.py  │
                        │ (Controle Web) │
                        └───────┬────────┘
                                │
                        ┌───────▼────────┐
                        │   Playwright   │
                        │ (Automação Web)│
                        └───────┬────────┘
                                │
                        ┌───────▼────────┐
                        │ BeautifulSoup  │
                        │ (Parsing HTML) │
                        └───────┬────────┘
                                │
                        ┌───────▼────────┐
                        │ comparador.py  │
                        │ (Detecção de   │
                        │  Novidades)    │
                        └───────┬────────┘
                                │
                        ┌───────▼────────┐
                        │ historico.csv  │
                        │  (Persistência)│
                        └────────────────┘
```

---

##  Tecnologias Utilizadas

| Tecnologia | Finalidade no Projeto |
|---|---|
| **Python** | Linguagem principal do projeto |
| **Playwright** | Automação de navegação e coleta de páginas dinâmicas da ANEEL |
| **BeautifulSoup** | Parsing e extração de dados do HTML coletado |
| **Pandas** | Estruturação, manipulação e persistência dos dados em CSV |
| **Git** | Controle de versão do código-fonte |
| **GitHub** | Hospedagem, versionamento e colaboração do projeto |

---

##  Módulos do Sistema

| Módulo | Responsabilidade |
|---|---|
| `app.py` | Ponto de entrada da aplicação; orquestra a execução dos demais módulos |
| `audiencias.py` | Coleta e estrutura os dados de Audiências Públicas (AP) |
| `consultas.py` | Coleta e estrutura os dados de Consultas Públicas (CP) |
| `tomadas.py` | Coleta e estrutura os dados de Tomadas de Subsídios (TS) |
| `navegador.py` | Camada de abstração sobre o Playwright, responsável pela navegação automatizada |
| `comparador.py` | Compara execuções e identifica novas publicações em relação ao histórico |
| `modelos.py` | Define as estruturas/modelos de dados utilizados no projeto |

---

##  Fontes Monitoradas

| Sigla | Tipo de Publicação | Descrição |
|---|---|---|
| **AP** | Audiência Pública | Processos abertos pela ANEEL para debate presencial/remoto sobre temas regulatórios |
| **CP** | Consulta Pública | Processos abertos para recebimento de contribuições escritas da sociedade |
| **TS** | Tomada de Subsídios | Processos para coleta preliminar de subsídios técnicos antes de normatizações |

---

##  Estrutura de Diretórios

```
Monitoramento_ANEEL/
│
├── dados/                  # Armazena os arquivos de dados coletados e históricos
│
├── logs/                   # Armazena logs de execução do sistema
│
├── src/                     # Código-fonte da aplicação
│   ├── app.py               # Ponto de entrada / orquestrador
│   ├── audiencias.py        # Coleta de Audiências Públicas
│   ├── consultas.py         # Coleta de Consultas Públicas
│   ├── tomadas.py           # Coleta de Tomadas de Subsídios
│   ├── comparador.py        # Comparação e detecção de novidades
│   ├── navegador.py         # Camada de automação web (Playwright)
│   └── modelos.py           # Modelos/estruturas de dados
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

##  Estrutura dos Dados Coletados

Cada publicação coletada é armazenada com os seguintes atributos:

| Campo | Descrição | Exemplo |
|---|---|---|
| `tipo` | Categoria da publicação (AP, CP ou TS) | `Consulta Pública` |
| `numero` | Número oficial do processo | `CP 015/2026` |
| `objeto` | Descrição/objeto da publicação | `Revisão das regras de qualidade do serviço` |
| `link` | URL de acesso à publicação original | `https://www.gov.br/aneel/...` |
| `data_coleta` | Data e hora em que o dado foi coletado | `2026-09-14 08:32:10` |

### Exemplo em formato CSV

```csv
tipo,numero,objeto,link,data_coleta
Consulta Pública,CP 015/2026,Revisão das regras de qualidade do serviço,https://www.gov.br/aneel/consulta-015,2026-09-14 08:32:10
Audiência Pública,AP 042/2026,Discussão sobre tarifas de distribuição,https://www.gov.br/aneel/audiencia-042,2026-09-14 08:32:15
Tomada de Subsídios,TS 007/2026,Subsídios técnicos para geração distribuída,https://www.gov.br/aneel/tomada-007,2026-09-14 08:32:20
```

---

##  Instalação

### Pré-requisitos

- Python 3.10 ou superior
- Git instalado
- Acesso à internet (para coleta de dados e instalação de dependências)

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/Monitoramento_ANEEL.git

# 2. Acesse o diretório do projeto
cd Monitoramento_ANEEL

# 3. Crie um ambiente virtual (recomendado)
python -m venv venv

# 4. Ative o ambiente virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 5. Instale as dependências
pip install -r requirements.txt

# 6. Instale os navegadores necessários para o Playwright
playwright install
```

---

## ▶️ Execução

Para executar o monitoramento completo (AP, CP e TS):

```bash
python src/app.py
```

Ao final da execução, o sistema irá:

1. Coletar os dados atualizados das três fontes
2. Comparar com o histórico salvo em `dados/historico.csv`
3. Exibir/registrar as novas publicações encontradas
4. Atualizar o histórico para a próxima execução

>  Recomenda-se agendar a execução periódica (ex: via **cron**, **Task Scheduler** ou **GitHub Actions**) para monitoramento contínuo.

---

##  Exemplo de Saída

```text
[2026-09-14 08:32:05] Iniciando monitoramento ANEEL...
[2026-09-14 08:32:06] Coletando Audiências Públicas...
[2026-09-14 08:32:15] Coletando Consultas Públicas...
[2026-09-14 08:32:25] Coletando Tomadas de Subsídios...
[2026-09-14 08:32:30] Comparando com histórico existente...

✅ 3 novas publicações encontradas:

- [Consulta Pública] CP 015/2026 - Revisão das regras de qualidade do serviço
- [Audiência Pública] AP 042/2026 - Discussão sobre tarifas de distribuição
- [Tomada de Subsídios] TS 007/2026 - Subsídios técnicos para geração distribuída

[2026-09-14 08:32:31] Histórico atualizado com sucesso em dados/historico.csv
[2026-09-14 08:32:31] Execução finalizada.
```

---

## 🗺️ Roadmap Futuro

- [ ]  Envio automático de notificações (E-mail, Slack, Telegram) para novas publicações
- [ ]  Dashboard interativo (Streamlit ou Power BI) para visualização do histórico
- [ ]  Agendamento automatizado via GitHub Actions
- [ ]  Migração do armazenamento de CSV para banco de dados (PostgreSQL/SQLite)
- [ ]  Filtros inteligentes por palavra-chave/setor de interesse
- [ ]  API REST para consulta dos dados coletados
- [ ]  Cobertura de testes automatizados (pytest)

---


## 📚 Aprendizados Adquiridos

Durante o desenvolvimento deste projeto, foram consolidados conhecimentos em:

- **Automação web avançada** com Playwright, incluindo tratamento de páginas dinâmicas
- **Web scraping estruturado** com BeautifulSoup, aplicando boas práticas de parsing
- **Manipulação e persistência de dados** com Pandas, incluindo comparação entre datasets
- **Arquitetura modular em Python**, separando responsabilidades por domínio (AP, CP, TS)
- **Versionamento de código com Git/GitHub**, incluindo boas práticas de commits e organização de repositório
- **Design de pipelines de dados**, desde a coleta até a persistência e comparação histórica
- Importância da **documentação profissional** para portfólio e comunicação técnica

---

## 👨‍💻 Sobre o Autor

Projeto desenvolvido como parte de um portfólio de soluções em **automação, engenharia de dados e monitoramento regulatório** aplicado ao setor elétrico brasileiro.


---

<p align="center">
  Feito ⚡ para o setor elétrico brasileiro
</p>
