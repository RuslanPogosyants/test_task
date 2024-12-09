from pydantic import BaseModel, Field
from typing import Dict


class FormTemplate(BaseModel):
    id: str = Field(default_factory=str)
    name: str
    fields: Dict[str, str]
