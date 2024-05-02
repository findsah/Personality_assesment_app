from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_transcripts():
    response = client.get("/transcripts/")
    assert response.status_code == 200
    assert response.json() is not None
    data = response.json()
    assert "index" in data[0]
    assert "speaker_label" in data[0]
    assert "paragraph" in data[0]

def test_read_summaries():
    response = client.get("/summaries/")
    assert response.status_code == 200
    assert response.json() is not None
    data = response.json()
    assert "sentence" in data[0]
    assert "is_inferable" in data[0]
    assert "explanation" in data[0]

def test_read_assessments():
    response = client.get("/assessments/")
    assert response.status_code == 200
    assert response.json() is not None
    data = response.json()
    assert "question" in data[0]
    assert "answer" in data[0]
    assert "evidence" in data[0]

def test_read_evaluations():
    response = client.get("/evaluations/")
    assert response.status_code == 200
    assert response.json() is not None
    data = response.json()
    assert "question" in data[0]
    assert "answer" in data[0]
    assert "inferability_score_1" in data[0]
    assert "inferability_score_2" in data[0]
