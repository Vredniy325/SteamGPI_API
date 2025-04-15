import requests
import json

def fetch_game_info(appid: int, region: str = "ru", language: str = "en") -> dict:
    url = "https://store.steampowered.com/api/appdetails"
    params = {
        "appids": appid,
        "cc": region,
        "l": language
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if not data.get(str(appid), {}).get("success"):
            return {
                "appid": appid,
                "region": region,
                "available": False,
                "message": "Game not found"
            }

        game_data = data[str(appid)]["data"]
        price_info = game_data.get("price_overview")

        return {
            "appid": appid,
            "region": region,
            "name": game_data.get("name", "Unknown"),
            "available": True,
            "is_free": game_data.get("is_free", False),
            "currency": price_info.get("currency") if price_info else None,
            "initial_price": price_info.get("initial") / 100 if price_info else None,
            "final_price": price_info.get("final") / 100 if price_info else None,
            "discount_percent": price_info.get("discount_percent") if price_info else 0,
            "platforms": game_data.get("platforms", {}),
            "release_date": game_data.get("release_date", {}).get("date")
        }

    except Exception as e:
        return {
            "appid": appid,
            "region": region,
            "available": False,
            "error": str(e)
        }

def fetch_game_info_multiple_regions(appid: int, regions: list[str]) -> list[dict]:
    return [fetch_game_info(appid, region) for region in regions]
