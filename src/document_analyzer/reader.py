from pathlib import Path

from pypdf import PdfReader


class DocumentReadError(ValueError):
    pass


def read_document_text(file_path: str) -> str:
    path = Path(file_path)

    if not path.is_file():
        raise DocumentReadError(f"Arquivo não encontrado: {path}")

    if path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8")

    if path.suffix.lower() != ".pdf":
        raise DocumentReadError("Formato não suportado. Use um arquivo .pdf ou .txt.")

    try:
        reader = PdfReader(path)
        text = "\n".join(page.extract_text() or "" for page in reader.pages).strip()
    except Exception as error:
        raise DocumentReadError("Não foi possível ler este PDF.") from error

    if not text:
        raise DocumentReadError(
            "Este PDF não possui texto selecionável. O suporte a OCR será adicionado em breve."
        )

    return text
