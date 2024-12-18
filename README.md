
# FastAPI Project

Этот проект является веб-приложением, разработанным с использованием FastAPI. Он предоставляет API для работы с формами и шаблонами.

## Установка

### Установка через Docker

Для запуска приложения с использованием Docker выполните следующие шаги:

1. **Соберите образ**:
   ```bash
   docker build -t fastapi-project .
   ```

2. **Запустите контейнер**:
   ```bash
   docker run -d -p 8000:8000 fastapi-project
   ```
   
### Установка без Docker

Если вы предпочитаете запускать приложение локально, установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

## Запуск приложения

Чтобы запустить приложение, используйте команду:

```bash
uvicorn app:app --reload
```

- `app` — это имя вашего основного файла.
- `--reload` позволяет автоматически перезагружать сервер при изменении кода.

## Использование API

### Получение формы

**POST** `/get_form`

**Тело запроса:**
```json
{
  "data": {
    "user_email": "test@example.com",
    "user_phone": "+7 123 456 78 90",
    "order_text": "Just some text"
  }
}
```

**Ответ:**
- Если шаблон найден:
  ```json
  {
    "template_name": "Order Form"
  }
  ```
- Если шаблон не найден:
  ```json
  {
    "user_email": "email",
    "user_phone": "phone",
    "order_text": "text"
  }
  ```

## Структура проекта

- `app.py` — основной файл приложения.
- `repositories/` — папка с доступом к базе данных и схемами.
- `services/` — папка с логикой валидации и другими сервисами.
- `services/manage.py` — файл со скриптом для наката данных в базу
- 
## Лицензия

Этот проект лицензирован под MIT License. См. файл [LICENSE](LICENSE) для получения подробной информации.


