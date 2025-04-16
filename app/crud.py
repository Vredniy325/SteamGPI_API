from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime, timedelta
from typing import List
from app.models import Game
def get_game_by_appid(db: Session, appid: int):
    return db.query(models.Game).filter(models.Game.appid == appid).first()


#Проверка на наличие игры в базе данных  по все регионам

def get_game_by_appid_and_region( 
        db: Session, 
        appid: int, 
        regions: List[str] = ["ru"] 
        ): 
        game = db.query(Game).filter(Game.appid == appid).first()
        if not game:
            return []  

        data_row = game.data  # это jsonb словарь
        data = data_row if isinstance(data_row, list) else [data_row]
        e_flag = "False"
        print("DATA VAR = ", data, "\n\n\n")
        for region in regions:
            flag = False
            for i in data:
                if i['region'] == region:
                    e_flag = "True"
                    flag = True
                    break
            

            if not flag:
                if e_flag == "True":
                    print("Нашел  хоть ОДИН регион для игры с id: ", appid)
                    return e_flag  # если игры нет в базе данных по региону
                print("Не нашел всех регионов для игры с id: ", appid)
                return []  # если игры нет в базе данных по региону
        print("Нашел все регионы для игры с id: ", appid)    
        return game


def update_game(db: Session, appid: int, game_data: dict):
    db_game = get_game_by_appid(db, appid)
    if db_game:
        db_game.data = game_data
        db_game.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_game)
        return db_game
    return None

# Updated create_or_update_game function
def create_game(db: Session, appid: int, game_data: list, regions: list[str]):#dict?

    #Для множества регионов
    created_games = []

    for region in regions:
        new_game = models.Game(
            appid=appid,
            data=game_data,
            updated_at=datetime.utcnow(),
            #region=region
        )
    db.add(new_game)
    created_games.append(new_game)

    db.commit()

    for game in created_games:
        db.refresh(game)

    return created_games