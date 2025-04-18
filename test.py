import requests
import json

def get_game_info (appid: int, region: str = "ru", language: str = "en"):
    """
    Gets information about a game from the Steam Store API.
    :param appid: game ID in Steam
    :param region: Region to get prices from (for example: 'ru', 'us', 'tr')
    :param language: Description language (for example: 'en', 'ru')
    :return: Dictionary with information about the game
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
        json_str = json.dumps(data, indent = 4)

        

        with open('app_info.json', 'a', encoding="utf-8") as f:
            f.write(json_str)
        f.close()

        flag = not data[str(appid)].get("success")

        if not data[str(appid)].get("success") :
            return {
                "appid": appid,
                "region": region,
                "break": True,
                "message": "Game not found"
            }

        game_data = data[str(appid)].get("data")
        try:    
            price_info = game_data.get("price_overview")
            result = {
            "appid": appid,
            "region": region,
            "name": game_data.get("name", "Неизвестно"),
            "available": True,
            "is_free": game_data.get("is_free", False),
            "currency": price_info.get("currency"),
            "initial_price": price_info.get("initial") / 100,
            "final_price": price_info.get("final") / 100 ,
            "discount_percent": price_info.get("discount_percent"),
            "platforms": game_data.get("platforms", {}),
            "release_date": game_data.get("release_date", {}).get("date")
            }
        except Exception as e:
            result = {
            "appid": appid,
            "region": region,
            "name": game_data.get("name", "Неизвестно"),
            "available": False,
            "is_free": game_data.get("is_free", False),
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


def get_info_across_regions(appid: int, regions: list) -> list:
    """
    Получает информацию об игре по нескольким регионам.
    :param appid: ID игры в Steam
    :param regions: Список регионов для сравнения
    :return: Список словарей с информацией по каждому региону
    """
    all_data = []
    i = 0
    for region in regions:
        info = get_game_info(appid, region)
        if info.get("break"):
            all_data.append(info)
        all_data.append(info)
        i += 1
        print(f"{i} из {len(regions)}")
    return all_data

def out_res():
    appid = 632360  #int(input("Введите AppID игры: "))

    # Список популярных регионов
    popular_regions = ["ru", "us", "eu", "tr", "kz"]

    with open('app_info.json', 'w', encoding="utf-8") as f:
        f.write("")
    f.close()
    
    results = get_info_across_regions(appid, popular_regions)

    for region_info in results:
        if region_info.get("available"):
            print(f"\nРегион: {region_info['region']}")
            print(f"Игра: {region_info['name']}")
            print(f"Цена без скидки: {region_info['initial_price']} {region_info['currency']}")
            print(f"Цена со скидкой: {region_info['final_price']} {region_info['currency']}")
            print(f"Скидка: {region_info['discount_percent']}%")
        elif region_info.get("break"):
            print(f"Товар не найден.")

        
        elif not region_info.get("available"):
            print(f"\nРегион: {region_info['region']}")
            print(f"Игра: {region_info['name']}")
            print(f"Товар недоступен в данном регионе.")
        
        
            

out_res()



    
    

    
