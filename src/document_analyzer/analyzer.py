from dataclasses import dataclass
from decimal import Decimal
import re


DOCUMENT_KEYWORDS = {
    "nota_fiscal": ("nota fiscal", "danfe", "nf-e"),
    "comprovante": ("comprovante", "pix", "transferência", "transferencia"),
    "documento_cadastral": ("cpf", "rg", "endereço", "endereco"),
}


@dataclass(frozen=True)
class AnalysisResult:
    document_type: str
    confidence: int
    cpf: tuple[str, ...]
    cnpj: tuple[str, ...]
    dates: tuple[str, ...]
    amounts_brl: tuple[Decimal, ...]


def analyze_document(text: str) -> AnalysisResult:
    normalized = text.casefold()
    matches = {
        document_type: sum(keyword in normalized for keyword in keywords)
        for document_type, keywords in DOCUMENT_KEYWORDS.items()
    }
    document_type, matched_keywords = max(matches.items(), key=lambda item: item[1])

    if matched_keywords == 0:
        document_type, confidence = "desconhecido", 25
    else:
        confidence = min(50 + matched_keywords * 20, 95)

    amounts = re.findall(r"R\$\s*([\d.]+,\d{2})", text)
    return AnalysisResult(
        document_type=document_type,
        confidence=confidence,
        cpf=tuple(re.findall(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b", text)),
        cnpj=tuple(re.findall(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b", text)),
        dates=tuple(re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)),
        amounts_brl=tuple(
            Decimal(amount.replace(".", "").replace(",", ".")) for amount in amounts
        ),
    )
