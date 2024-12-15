from typing import Dict, Any, Optional, List

from repositories.mongo.database import get_templates
from repositories.mongo.schemas import FormRequest
from services.validators import validate_field


async def get_form(request: FormRequest) -> Dict[str, Any]:
    data: Dict[str, Any] = request.data
    templates: List[Dict[str, Any]] = await get_templates()

    matched_template: Optional[str] = None

    validated_fields: Dict[str, str] = {field: validate_field(field, value) for field, value in data.items()}

    for template in templates:
        fields: Dict[str, str] = template['fields']

        if all(field in data and validated_fields[field] == fields[field] for field in fields):
            matched_template = template['name']
            break

    if matched_template:
        return {"template_name": matched_template}

    return validated_fields
