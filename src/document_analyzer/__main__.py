"""Interface de linha de comando para o analisador de documentos."""

import argparse
import json

from .analyzer import analyze_document
from .reader import DocumentReadError, read_document_text


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Classifica documentos e extrai campos básicos."
    )
    input_source = parser.add_mutually_exclusive_group(required=True)
    input_source.add_argument("--text", help="Texto extraído do documento.")
    input_source.add_argument("--file", help="Caminho para um arquivo PDF ou TXT.")
    args = parser.parse_args()

    try:
        text = args.text if args.text is not None else read_document_text(args.file)
    except DocumentReadError as error:
        parser.error(str(error))

    result = analyze_document(text)
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
