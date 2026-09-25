from decimal import Decimal

from document_analyzer import analyze_document
from document_analyzer import reader
from document_analyzer.reader import DocumentReadError, read_document_text


def test_analyzes_invoice_text() -> None:
    result = analyze_document(
        "Nota Fiscal DANFE emitida em 24/09/2026. "
        "CNPJ 12.345.678/0001-95. Total R$ 1.250,00."
    )

    assert result.document_type == "nota_fiscal"
    assert result.confidence == 90
    assert result.cnpj == ("12.345.678/0001-95",)
    assert result.dates == ("24/09/2026",)
    assert result.amounts_brl == (Decimal("1250.00"),)


def test_marks_unknown_text_with_low_confidence() -> None:
    result = analyze_document("Mensagem simples sem campos conhecidos.")

    assert result.document_type == "desconhecido"
    assert result.confidence == 25


def test_reads_text_file(tmp_path) -> None:
    document = tmp_path / "nota.txt"
    document.write_text("Nota Fiscal. CNPJ 12.345.678/0001-95.", encoding="utf-8")

    assert read_document_text(str(document)) == "Nota Fiscal. CNPJ 12.345.678/0001-95."


def test_rejects_file_without_supported_extension(tmp_path) -> None:
    document = tmp_path / "nota.csv"
    document.write_text("conteúdo", encoding="utf-8")

    try:
        read_document_text(str(document))
    except DocumentReadError as error:
        assert "Formato não suportado" in str(error)
    else:
        raise AssertionError("Era esperado um erro para extensão não suportada.")


def test_reads_text_from_pdf(tmp_path, monkeypatch) -> None:
    document = tmp_path / "nota.pdf"
    document.write_bytes(b"arquivo de teste")

    class FakePage:
        def extract_text(self) -> str:
            return "Nota Fiscal. Total R$ 50,00."

    class FakeReader:
        pages = [FakePage()]

    monkeypatch.setattr(reader, "PdfReader", lambda path: FakeReader())

    assert read_document_text(str(document)) == "Nota Fiscal. Total R$ 50,00."
