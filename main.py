from utils import *
from fastapi import FastAPI
import os
from typing import Optional

app = FastAPI()

@app.get("/")
def get_game_info():
    return out_res()
