# utils.py

import requests
import json
from typing import List, Dict, Union


def get_game_info(appid: int, region: str = "ru", language: str = "en") -> Dict[str, Union[int, str, float, bool, None]]:
    """
    Получает информацию об игре из Steam Store API.
    :param appid: ID игры в Steam
    :param region: Регион (например: 'ru', 'us', 'tr')
    :param language: Язык описания (например: 'en', 'ru')
    :return: Словарь с информацией об игре
    """
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
        price_info = game_data.get("price_overview", {})

        result = {
            "appid": appid,
            "region": region,
            "name": game_data.get("name", "Неизвестно"),
            "available": True,
            "is_free": game_data.get("is_free", False),
            "currency": price_info.get("currency"),
            "initial_price": price_info.get("initial", 0) / 100 if price_info else None,
            "final_price": price_info.get("final", 0) / 100 if price_info else None,
            "discount_percent": price_info.get("discount_percent", 0),
            "platforms": game_data.get("platforms", {}),
            "release_date": game_data.get("release_date", {}).get("date")
        }

        return result

    except Exception as e:
        return {
            "appid": appid,
            "region": region,
            "available": False,
            "error": str(e)
        }


def get_info_across_regions(appid: int, regions: List[str]) -> List[Dict]:
    """
    Получает информацию об игре по нескольким регионам.
    :param appid: ID игры в Steam
    :param regions: Список регионов для сравнения
    :return: Список словарей с информацией по каждому региону
    """
    all_data = []
    for i, region in enumerate(regions, start=1):
        print(f"{i} из {len(regions)}: {region}")
        info = get_game_info(appid, region)
        all_data.append(info)
    return all_data


def out_res():
    """
    Получает AppID от пользователя и выводит сравнение цен по регионам.
    """
    appid = int(input("Введите AppID игры: "))
    popular_regions = ["ru", "us", "eu", "tr", "kz"]

    results = get_info_across_regions(appid, popular_regions)

    # Логируем в app_info.json (полный лог)
    with open('app_info.json', 'w', encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    print("\nСравнение по регионам:")
    for region_info in results:
        if region_info.get("available"):
            print(f"\nРегион: {region_info['region']}")
            print(f"Игра: {region_info['name']}")
            print(f"Цена без скидки: {region_info['initial_price']} {region_info['currency']}")
            print(f"Цена со скидкой: {region_info['final_price']} {region_info['currency']}")
            print(f"Скидка: {region_info['discount_percent']}%")
        elif region_info.get("message"):
            print(f"\n{region_info['region']} ➜ {region_info['message']}")
        else:
            print(f"\n{region_info['region']} ➜ Ошибка: {region_info.get('error')}")


