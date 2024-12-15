import pytest
from fastapi.testclient import TestClient

from repositories.mongo.database import db
from app import app


@pytest.fixture
async def mock_db(monkeypatch):
    async def mock_get_templates():
        return [{
            '_id': '1',
            'name': 'Order Form',
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
def client(mock_db):
    with TestClient(app) as client:
        yield client

