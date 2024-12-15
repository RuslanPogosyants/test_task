from pydantic import BaseModel, Field
from typing import Dict


class FormTemplate(BaseModel):
    """Модель шаблона формы."""
    id: str = Field(default_factory=str)
    """ID шаблона."""
    name: str
    """Имя шаблона."""
    fields: Dict[str, str]
    """Словарь, содержащий поля шаблона и их типы."""
