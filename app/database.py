from motor.motor_asyncio import AsyncIOMotorClient


class Database:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]

    async def get_templates(self):
        templates = await self.db.templates.find().to_list(length=None)
        return templates

    async def add_template(self, name: str, fields: dict):
        template = {
            "name": name,
            "fields": fields
        }
        result = await self.db.templates.insert_one(template)
        return str(result.inserted_id)

    async def clear_templates(self):
        result = await self.db.templates.delete_many({})
        return result.deleted_count


db = Database("mongodb://localhost:27017", "template_fomr_db")
