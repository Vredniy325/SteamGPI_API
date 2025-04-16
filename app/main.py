from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import routes

app = FastAPI(
    title="Steam GeoPricing Inspector API",
    description="Сервис для мониторинга цен и доступности игр в Steam по регионам.",
    version="1.0.0"
)

# Разрешённые источники (можно ограничить для фронта)
origins = [
    "*",  # В продакшене заменить на URL расширения или фронта
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем маршруты
app.include_router(routes.router)
