import re


def validate_field(field_name, value):
    match value:
        case _ if re.match(r'^\d{2}\.\d{2}\.\d{4}$', value) or re.match(r'^\d{4}-\d{2}-\d{2}$', value):
            return "date"
        case _ if re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value):
            return "phone"
        case _ if isinstance(value, str) and re.match(r'^[^@]+@[^@]+\.[^@]+$', value):
            return "email"
        case _:
            return "text"
