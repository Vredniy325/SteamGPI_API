from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app import routes

app = FastAPI(
    title="SteamGPI API",
    description="API для мониторинга цен и доступности игр в Steam по регионам",
    version="1.0.0"
)

app.include_router(routes.router)

@app.get("/", response_class=JSONResponse)
async def root():
    return {"message": "Добро пожаловать в SteamGPI API!"}
