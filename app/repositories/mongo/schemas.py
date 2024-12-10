from pydantic import BaseModel
from typing import Dict, Any


class FormRequest(BaseModel):
    data: Dict[str, Any]
