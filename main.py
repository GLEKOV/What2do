import uvicorn
from typing import Union
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from fastapi import FastAPI
from router import router as index_router


app = FastAPI(title="What2do")

app.mount("/static", StaticFiles(directory="./static"), name="static")

app.include_router(index_router)

