from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/home", include_in_schema=False)
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html")