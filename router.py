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
