from utils import *
from fastapi import FastAPI
import os
from typing import Optional

app = FastAPI()

@app.get("/")
def home_page():
    return out_res()
