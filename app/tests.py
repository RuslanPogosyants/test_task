import pytest
from fastapi.testclient import TestClient
from app.database import db
from app.main import app


@pytest.fixture
async def mock_db(monkeypatch):
    async def mock_get_templates():
        return [{
            '_id': '1',
            'name': 'OrderForm',
            'fields': {
                'user_email': 'email',
                'user_phone': 'phone',
                'order_date': 'date'
            }
        }]

    async def mock_add_template(name, fields):
        return '1'

    monkeypatch.setattr(db, "get_templates", mock_get_templates)
    monkeypatch.setattr(db, "add_template", mock_add_template)

@pytest.fixture
def client():
    return TestClient(app)

@pytest.mark.asyncio
async def test_get_nonexistent_template(mock_db, client, monkeypatch):
    async def mock_get_templates_empty():
        return []

    monkeypatch.setattr(db, "get_templates", mock_get_templates_empty)

    data = {
        "user_email": "test@example.com",
        "user_phone": "+7 123 456 78 90",
        "order_text": "Just some text"
    }

    response = client.post("/get_form", json={"data": data})

    assert response.status_code == 200
    assert response.json() == {'user_email': 'email', 'user_phone': 'phone', 'order_text': 'text'}

@pytest.mark.asyncio
async def test_get_existing_template(mock_db, client):
    data = {
        "user_email": "test@example.com",
        "user_phone": "+7 123 456 78 90",
        "order_date": "01.01.2021"
    }

    response = client.post("/get_form", json={"data": data})

    assert response.status_code == 200
    assert response.json() == {'template_name': 'OrderForm'}

if __name__ == "__main__":
    pytest.main()

