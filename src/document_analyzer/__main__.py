"""Interface de linha de comando para o analisador de documentos."""

import argparse
import json

from .analyzer import analyze_document


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Classifica texto documental e extrai campos básicos."
    )
    parser.add_argument("--text", required=True, help="Texto extraído do documento.")
    args = parser.parse_args()

    result = analyze_document(args.text)
    response = {
        "document_type": result.document_type,
        "confidence": result.confidence,
        "cpf": result.cpf,
        "cnpj": result.cnpj,
        "dates": result.dates,
        "amounts_brl": [str(amount) for amount in result.amounts_brl],
    }
    print(json.dumps(response, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
