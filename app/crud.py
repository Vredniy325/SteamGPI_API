from sqlalchemy.orm import Session
from app import models, schemas

def create_game(db: Session, game: schemas.GameCreate) -> models.Game:
    db_game = models.Game(**game.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game
