from pydantic import BaseModel
from typing import Dict, Any


class FormRequest(BaseModel):
    """Модель запроса для получения формы."""
    data: Dict[str, Any]
    """Данные формы, содержащие ключи и значения"""
