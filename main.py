from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles  # ✅ Needed to serve static files

app = FastAPI()

# ✅ Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "GetSetAI"})

@app.get("/upcoming", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("upcoming.html", {"request": request})


@app.get("/detail", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("detail.html", {"request": request})