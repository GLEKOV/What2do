from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates



router = APIRouter(
    tags=['Главная страница'],
)



templates = Jinja2Templates(directory="templates")



@router.get('/', response_class=HTMLResponse)
async def name(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get('/a1', response_class=HTMLResponse)
async def name(request: Request):
    return templates.TemplateResponse("a1.html", {"request": request})

@router.get('/a2', response_class=HTMLResponse)
async def name(request: Request):
    return templates.TemplateResponse("a2.html", {"request": request})