from fastapi import FastAPI
from app.database import db
from app.schemas import FormRequest
from app.validators import validate_field

app = FastAPI()


@app.post("/get_form")
async def get_form(request: FormRequest):
    data = request.data
    templates = await db.get_templates()

    matched_template = None

    for template in templates:
        fields = template['fields']

        if all(field in data and validate_field(field, data[field]) == fields[field] for field, field_type in fields.items()):
            matched_template = template['name']
            break

    if matched_template:
        return {"template_name": matched_template}

    field_types = {field: validate_field(field, value) for field, value in data.items()}
    return field_types
