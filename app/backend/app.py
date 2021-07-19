from fastapi import FastAPI
from app.backend.api.routers.api import router
def generate_app():
    app = FastAPI()
    app.include_router(router)
    return app

app = generate_app()