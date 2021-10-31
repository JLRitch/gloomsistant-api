# standard modules
import pathlib as pl
import sqlite3

# external modules
from fastapi import FastAPI

# project modules
from routes.api import router as api_router

def get_application() -> FastAPI:
    application = FastAPI(title="Gloomsistant_API", debug=True, version="0.1.0")
    application.include_router(api_router)
    return application

app = get_application()