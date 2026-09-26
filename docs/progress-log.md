# Registro de Progresso

Este arquivo registra entregas reais do projeto. Não é um calendário planejado: cada entrada é adicionada após a atividade acontecer.

## 2026-09-23 — Início do laboratório

- Criação do repositório e primeiro commit publicado no GitHub.
- Definição do foco: desenvolvimento Full Stack com IA e Automação.
- Criação do roadmap inicial e organização para acompanhar as próximas entregas.

## 2026-09-24 — Primeiro módulo de automação documental

- Criação do `document_analyzer` em Python.
- Implementação de classificação inicial para nota fiscal, comprovante e documento cadastral.
- Extração local de CPF, CNPJ, datas e valores monetários.
- Inclusão de testes para um texto de nota fiscal e um documento desconhecido.

## 2026-09-25 — Uso do analisador pelo terminal

- Configuração do pacote Python com `pyproject.toml`.
- Criação de uma interface de linha de comando para analisar texto documental.
- Saída estruturada em JSON para facilitar a integração com outros sistemas.
- Instalação do Python 3.13 e criação do ambiente virtual local.
- Execução dos testes: 5 aprovados.

## 2026-09-25 — Leitura de arquivos PDF

- Adição de leitura de arquivos PDF com texto selecionável.
- Suporte a arquivos `.txt` para testes e integrações simples.
- Mensagem clara para PDFs escaneados, que ainda dependem da etapa de OCR.

## 2026-09-26 — Primeira API

- Criação da API com FastAPI.
- Rota de saúde para verificar se o serviço está ativo.
- Rota para analisar texto de documentos via HTTP.
- Testes para rota de saúde, análise e validação de entrada.
- Suíte completa executada: 8 testes aprovados.
