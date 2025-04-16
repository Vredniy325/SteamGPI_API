from pydantic import BaseModel
from typing import Optional, List


class PriceOverview(BaseModel):
    currency: Optional[str]
    initial: Optional[float]
    final: Optional[float]
    discount_percent: Optional[int]


class GameData(BaseModel):
    name: str
    is_free: bool
    platforms: dict
    release_date: dict
    price_overview: Optional[PriceOverview]


class GameResponse(BaseModel):
    appid: int
    region: str
    name: str
    available: bool
    is_free: bool
    currency: Optional[str]
    initial_price: Optional[float]
    final_price: Optional[float]
    discount_percent: Optional[int]
    platforms: dict
    release_date: Optional[str]
    error: Optional[str] = None


class AlertCreate(BaseModel):
    appid: int
    price: str


class AlertResponse(AlertCreate):
    alertid: int
    userid: int


class UserCreate(BaseModel):
    login: str
    password: str


class UserResponse(UserCreate):
    userid: int
