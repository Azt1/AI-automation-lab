# AI Document Processor

Esse é o primeiro projeto do meu laboratório de IA e automação.

A ideia é simples: receber o texto de um documento e transformar as informações importantes em dados organizados. É o tipo de tarefa que costuma tomar tempo quando feita manualmente.

## O que já funciona

O projeto aceita texto copiado, arquivo `.txt` ou PDF com texto selecionável. Ele tenta identificar se o conteúdo parece ser uma nota fiscal, comprovante ou documento cadastral e procura por:

- CPF e CNPJ
- datas
- valores em reais

Também retorna uma confiança inicial para a classificação. Se o documento não tiver sinais suficientes, ele fica como `desconhecido`.

## Exemplo

Entrada:

```text
Nota Fiscal emitida em 25/09/2026. CNPJ 12.345.678/0001-95. Total R$ 1.250,00.
```

Saída esperada:

```json
{
  "document_type": "nota_fiscal",
  "confidence": 70,
  "cnpj": ["12.345.678/0001-95"],
  "dates": ["25/09/2026"],
  "amounts_brl": ["1250.00"]
}
```

## Rodar localmente

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
python -m document_analyzer --text "Nota Fiscal emitida em 25/09/2026. CNPJ 12.345.678/0001-95. Total R$ 1.250,00."
```

Para analisar um arquivo:

```bash
python -m document_analyzer --file "C:\caminho\para\nota-fiscal.pdf"
```

## Próximos passos

- Ler imagem e PDF escaneado usando OCR
- Criar uma API com FastAPI
- Adicionar uma tela para enviar o documento
- Usar IA para lidar com documentos menos padronizados

Os testes ficam na pasta `tests/` e o código principal está em `src/document_analyzer/`.
