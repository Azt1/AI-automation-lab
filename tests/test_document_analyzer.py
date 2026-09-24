from decimal import Decimal

from document_analyzer import analyze_document


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
