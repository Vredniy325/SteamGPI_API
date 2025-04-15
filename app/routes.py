from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from typing import List, Optional

from app.steam import get_game_info, get_info_across_regions

router = APIRouter()

@router.get("/game/{appid}")
async def get_game(appid: int, region: Optional[str] = "ru", language: Optional[str] = "en"):
    """
    Получение информации об игре в одном регионе.
    """
    data = get_game_info(appid=appid, region=region, language=language)
    if data.get("break"):
        return JSONResponse(status_code=404, content={"error": "Game not found"})
    return data

@router.get("/game/{appid}/regions")
async def get_game_multiple_regions(
    appid: int,
    regions: List[str] = Query(..., description="Список регионов, например: ru,us,tr")
):
    """
    Получение информации об игре в нескольких регионах.
    """
    result = get_info_across_regions(appid=appid, regions=regions)
    return result
