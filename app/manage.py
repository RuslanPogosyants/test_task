import asyncio
import aiohttp

from repositories.mongo.database import db

url = "http://localhost:8000/get_form"


async def post_data(data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            status_code = response.status
            response_json = await response.json()
            print("Status Code:", status_code)
            print("Response JSON:", response_json)


async def delete_templates():
    deleted_count = await db.clear_templates()
    print(f'Удалено документов: {deleted_count}')

    templates = await db.get_templates()
    print('Все шаблоны после очистки:', templates)


async def add_template():
    template_name = "Form #1"
    fields = {
        "field_name_1": "email",
        "field_name_2": "phone",
        "field_name_3": "date"
    }

    inserted_id = await db.add_template(template_name, fields)
    print(f'Шаблон добавлен с ID: {inserted_id}')

    templates = await db.get_templates()
    print('Все шаблоны:', templates)


async def main():
    await delete_templates()
    await add_template()

    data_not_in_db = {
        "data": {
            "email": "test@example.com",
            "phone": "+7 123 456 78 90",
        }
    }
    await post_data(data_not_in_db)

    data_in_db = {
        "data": {
            "field_name_1": "email@mail.ru",
            "field_name_2": "+7 123 456 78 90",
            "field_name_3": "01.01.2021"
        }
    }
    await post_data(data_in_db)


if __name__ == '__main__':
    asyncio.run(main())
