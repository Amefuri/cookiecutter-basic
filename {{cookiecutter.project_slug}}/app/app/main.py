from core import config
from api.api_v1.api import api_router
from fastapi import FastAPI

app = FastAPI(title=config.PROJECT_NAME)
app.include_router(api_router, prefix=config.API_V1_PATH)