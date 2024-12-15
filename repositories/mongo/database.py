from motor.motor_asyncio import AsyncIOMotorClient
from typing import Dict, Any, List

uri = "mongodb://mongo:27017"
db_name = "template_form_db"
client = AsyncIOMotorClient(uri)
db = client[db_name]


async def get_templates() -> List[Dict[str, Any]]:
    """Получить все шаблоны из базы данных."""
    templates = await db.templates.find().to_list(length=None)
    return templates


async def add_template(name: str, fields: Dict[str, Any]) -> str:
    """Добавить новый шаблон в базу данных."""
    template = {
        "name": name,
        "fields": fields
    }
    result = await db.templates.insert_one(template)
    return str(result.inserted_id)


async def clear_templates() -> int:
    """Очистить все шаблоны из базы данных."""
    result = await db.templates.delete_many({})
    return result.deleted_count
