from fastapi import FastAPI

from services.from_handlers import get_form

app = FastAPI()

app.add_api_route("/get_form", get_form, methods=["POST"])
