
# SteamGPI API
Сервис для мониторинга цен и доступности игр в Steam по регионам.

## Обзор
Steam GPI API позволяет получать информацию о ценах и доступности игр в Steam в разных регионах. Этот API полезен для сравнения цен и проверки региональной доступности прямо из браузерного расширения.

## 📌 Цели проекта
- Проверка актуальных цен на игры в Steam по регионам.
- Сравнение скидок и цен в разных валютах.
- Хранение информации об играх в PostgreSQL в формате JSONB.
- Расширяемость.

## ⚙️ Технологии
- Python (основной парсер и API-клиент)
- PostgreSQL (база данных)
- JSONB (гибкое хранение данных)
- Docker (контейнеризация)
- Git + Git Hooks + линтеры (code quality)
- Steam Store API

## 🗄 Структура БД

### Таблица: games

| Поле        | Тип         | Описание                                   |
|-------------|-------------|--------------------------------------------|
| appid       | INTEGER     | ID игры в Steam (primary key)              |
| data        | JSONB       | Вся информация об игре и ценах по регионам|
| updated_at  | TIMESTAMP   | Время последнего обновления                |

## Базовый URL
https://store.steampowered.com/api/appdetails

## Эндпоинты

### 1. Получение информации об игре в одном регионе
Возвращает данные о цене и доступности игры в указанном регионе.

**Эндпоинт:**
GET /game/{appid}

**Параметры:**
- `appid` (integer, обязательно) – Уникальный идентификатор игры в Steam.
- `region` (string, опционально) – Код региона (например, ru, us, tr). Если не указан, возвращается глобальная информация.
- `language` (string, опционально) – Язык описания игры (например, en, ru).

**Ответ:**
JSON-объект с информацией о продукте.

#### Пример запроса:
GET /game/570?region=us&language=en

#### Пример ответа:
```json
{
  "appid": 570,
  "region": "us",
  "name": "Dota 2",
  "available": true,
  "initial_price": 0,
  "final_price": 0,
  "currency": "USD",
  "discount_percent": 0
}
```

---

### 2. Получение информации об игре в нескольких регионах
Возвращает данные о цене и доступности игры в нескольких регионах.

**Эндпоинт:**
GET /game/{appid}/regions

**Параметры:**
- `appid` (integer, обязательно) – Уникальный идентификатор игры в Steam.
- `regions` (массив строк, обязательно) – Список кодов регионов (например, ru,us,eu,tr).

**Ответ:**
JSON-массив с информацией по каждому региону.

#### Пример запроса:
GET /game/570/regions?regions=ru,us,eu,tr

#### Пример ответа:
```json
[
  {
    "region": "ru",
    "name": "Dota 2",
    "available": true,
    "initial_price": 0,
    "final_price": 0,
    "currency": "RUB",
    "discount_percent": 0
  },
  {
    "region": "us",
    "name": "Dota 2",
    "available": true,
    "initial_price": 0,
    "final_price": 0,
    "currency": "USD",
    "discount_percent": 0
  }
]
```

## Обработка ошибок
- 400 Bad Request – Неверный запрос (например, отсутствует appid).
- 404 Not Found – Игра не найдена.
- 500 Internal Server Error – Внутренняя ошибка сервера.

## Ограничения
API ограничено 60 запросами в минуту на один IP-адрес.

## Контакты и поддержка
По вопросам и проблемам обращайтесь в службу поддержки: danver6@mail.ru.
