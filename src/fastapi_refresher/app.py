from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts : list[dict] = [
    {
        "id" : 1,
        "author": "Tendo Calvin",
        "title" : "FastAPI is awesome",
        "content": "This framework is used in Machine Learning systems",
        "date_posted": "April, 20 2025"
    } , 
    
    {
        "id" : 1,
        "author": "David Beckham",
        "title" : "Software Engineer",
        "content": "he works remotely and has a YouTube channel for showcasing his skills",
        "date_posted": "April, 20 2025"
    }
]

@app.get("/home", include_in_schema=False)
async def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})