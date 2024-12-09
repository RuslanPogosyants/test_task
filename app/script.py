import requests

url = "http://localhost:8000/get_form"

data = {
    "data": {
        "email": "test@example.com",
        "phone": "+7 123 456 78 90",
    }
}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

data = {
    "data": {
        "field_name_1": "email@mail.ru",
        "field_name_2": "+7 123 456 78 90",
        "field_name_3": "01.01.2021"
    }
}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

