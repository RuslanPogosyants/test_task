import asyncio
import aiohttp
from typing import Dict, Any, List

from repositories.mongo.database import clear_templates, get_templates, add_template

url = "http://0.0.0.0:8000/get_form"


async def post_data(data: Dict[str, Any]) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            status_code: int = response.status
            response_json: Dict[str, Any] = await response.json()
            print("Status Code:", status_code)
            print("Response JSON:", response_json)


async def delete_all_templates() -> None:
    deleted_count: int = await clear_templates()
    print(f'Удалено документов: {deleted_count}')

    templates: List[Dict[str, Any]] = await get_templates()
    print('Все шаблоны после очистки:', templates)


async def add_mock_template() -> None:
    template_name: str = "Order Form"
    fields: Dict[str, str] = {
        "field_name_1": "email",
        "field_name_2": "phone",
        "field_name_3": "date"
    }

    inserted_id: str = await add_template(template_name, fields)
    print(f'Шаблон добавлен с ID: {inserted_id}')

    templates: List[Dict[str, Any]] = await get_templates()
    print('Все шаблоны:', templates)


async def main() -> None:
    await delete_all_templates()
    await add_mock_template()

    data_not_in_db: Dict[str, Dict[str, str]] = {
        "data": {
            "email": "test@example.com",
            "phone": "+7 123 456 78 90",
        }
    }
    await post_data(data_not_in_db)

    data_in_db: Dict[str, Dict[str, str]] = {
        "data": {
            "field_name_1": "email@mail.ru",
            "field_name_2": "+7 123 456 78 90",
            "field_name_3": "01.01.2021"
        }
    }
    await post_data(data_in_db)

if __name__ == '__main__':
    asyncio.run(main())
