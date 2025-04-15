from fastapi import APIRouter, Query
from app.steam import fetch_game_info, fetch_game_info_multiple_regions

router = APIRouter()

@router.get("/game/{appid}")
async def get_game(appid: int, region: str = "ru", language: str = "en"):
    return fetch_game_info(appid, region, language)

@router.get("/game/{appid}/regions")
async def get_game_regions(
    appid: int,
    regions: list[str] = Query(default=["ru", "us", "eu", "tr", "kz"])
):
    return fetch_game_info_multiple_regions(appid, regions)
