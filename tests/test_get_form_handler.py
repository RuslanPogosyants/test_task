import pytest



@pytest.mark.asyncio
@pytest.mark.parametrize("data, expected_status, expected_response", [
    (
        {
            "data": {
                "field_name_1": "email@mail.ru",
                "field_name_2": "+7 123 456 78 90",
                "field_name_3": "01.01.2021"
            }
        },
        200,
        {'template_name': 'Order Form'}
    )
])
async def test_get_existing_template(mock_db, client, data, expected_status, expected_response):
    response = client.post("/get_form", json=data)
    assert response.status_code == expected_status
    assert response.json() == expected_response


if __name__ == "__main__":
    pytest.main()
