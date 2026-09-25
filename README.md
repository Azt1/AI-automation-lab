# AI Automation Lab

> Laboratório prático para construir produtos de Inteligência Artificial e Automação com foco em problemas reais de negócio.

## Sobre

Este repositório registra minha evolução como desenvolvedor **Full Stack com foco em IA e Automação**. Cada entrega parte de um problema concreto, é documentada e evolui em incrementos pequenos e verificáveis.

## O que vou construir

- Processamento inteligente de documentos com OCR e IA.
- Agentes para suporte e consulta de bases de conhecimento.
- Automação de fluxos entre APIs, e-mails e bancos de dados.
- Ferramentas de monitoramento de execuções e falhas.

## Stack em evolução

`Python` · `FastAPI` · `React` · `TypeScript` · `PostgreSQL` · `APIs de IA` · `n8n` · `Docker` · `GitHub Actions`

## Roadmap

O plano de entregas está em [docs/roadmap.md](docs/roadmap.md). O progresso real de cada sessão fica em [docs/progress-log.md](docs/progress-log.md).

## Primeira entrega técnica

O módulo `document_analyzer` começa o projeto **AI Document Processor**. Nesta etapa, ele identifica o provável tipo de um documento a partir do texto e extrai CPF, CNPJ, datas e valores em reais. A evolução natural é receber PDFs e imagens, aplicar OCR e usar IA para interpretar campos menos padronizados.

### Como executar localmente

Após instalar o Python 3.11 ou superior:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
python -m document_analyzer --text "Nota Fiscal emitida em 25/09/2026. CNPJ 12.345.678/0001-95. Total R$ 1.250,00."
```

O comando retorna um JSON com o tipo provável de documento, confiança e campos encontrados.

## Estrutura

```text
src/        # Aplicações e serviços
tests/      # Testes automatizados
docs/       # Decisões, roadmap e registros de progresso
```

## Princípios do projeto

- Commits pequenos, com uma mudança clara por vez.
- Código acompanhado de documentação e testes quando aplicável.
- Automação usada para resolver tarefas reais, não apenas como demonstração.
- Progresso documentado com honestidade e contexto.

---

*A practical portfolio focused on building AI-powered automation products.*
