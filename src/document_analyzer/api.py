from fastapi import FastAPI
from pydantic import BaseModel, Field

from .analyzer import analyze_document

app = FastAPI(
    title="AI Document Processor",
    version="0.1.0",
    description="Analisa texto de documentos e extrai campos básicos.",
)


class AnalyzeRequest(BaseModel):
    text: str = Field(min_length=10, description="Texto extraído de um documento.")


class AnalyzeResponse(BaseModel):
    document_type: str
    confidence: int
    cpf: list[str]
    cnpj: list[str]
    dates: list[str]
    amounts_brl: list[str]


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/v1/analyze", response_model=AnalyzeResponse)
def analyze(payload: AnalyzeRequest) -> AnalyzeResponse:
    result = analyze_document(payload.text)
    return AnalyzeResponse(
        document_type=result.document_type,
        confidence=result.confidence,
        cpf=list(result.cpf),
        cnpj=list(result.cnpj),
        dates=list(result.dates),
        amounts_brl=[str(amount) for amount in result.amounts_brl],
    )
