from fastapi.testclient import TestClient

from document_analyzer.api import app

client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_analyze_document_text() -> None:
    response = client.post(
        "/api/v1/analyze",
        json={
            "text": "Nota Fiscal emitida em 26/09/2026. "
            "CNPJ 12.345.678/0001-95. Total R$ 99,90."
        },
    )

    assert response.status_code == 200
    assert response.json()["document_type"] == "nota_fiscal"
    assert response.json()["cnpj"] == ["12.345.678/0001-95"]
    assert response.json()["amounts_brl"] == ["99.90"]


def test_rejects_short_text() -> None:
    response = client.post("/api/v1/analyze", json={"text": "curto"})

    assert response.status_code == 422
