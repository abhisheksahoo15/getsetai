from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# ✅ Mount static folder for CSS, JS, images, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ HTML Templates Directory
templates = Jinja2Templates(directory="templates")


# ✅ Home Page Route
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": "GetSetAI"
    })


# ✅ Upcoming Events Page
@app.get("/upcoming", response_class=HTMLResponse)
async def show_upcoming_events(request: Request):
    return templates.TemplateResponse("upcoming.html", {
        "request": request,
        "title": "Upcoming Events"
    })


# ✅ Event Detail Page
@app.get("/detail", response_class=HTMLResponse)
async def show_event_detail(request: Request):
    return templates.TemplateResponse("detail.html", {
        "request": request,
        "title": "Event Details"
    })


# ✅ Past Events Gallery Page
@app.get("/gallery", response_class=HTMLResponse)
async def show_event_gallery(request: Request):
    return templates.TemplateResponse("eventgallary.html", {
        "request": request,
        "title": "Past Events"
    })

# ✅ Past Events Gallery Page
@app.get("/ssmv", response_class=HTMLResponse)
async def show_event_gallery(request: Request):
    return templates.TemplateResponse("pastevents/ssmv1.html", {
        "request": request,
        "title": "Past Events"
    })


# ✅ Past Events Gallery Page
@app.get("/details", response_class=HTMLResponse)
async def show_event_gallery(request: Request):
    return templates.TemplateResponse("detail.html", {
        "request": request,
        "title": "detail"
    })


# ✅ Past Events Gallery Page
@app.get("/about", response_class=HTMLResponse)
async def show_event_gallery(request: Request):
    return templates.TemplateResponse("about.html", {
        "request": request,
        "title": "about"
    })


# ✅ Past Events Gallery Page
@app.get("/contact", response_class=HTMLResponse)
async def show_event_gallery(request: Request):
    return templates.TemplateResponse("contact.html", {
        "request": request,
        "title": "about"
    })