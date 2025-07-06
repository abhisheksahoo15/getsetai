from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# ✅ Mount static folder for CSS, JS, images, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ HTML Templates Directory
templates = Jinja2Templates(directory="templates")



# 🧠 Employee Master Data
employees = [
    {
        "name": "Shri Jagannath",
        "image": "/static/images/employee/jagga.jpg",
        "designation": "Chief Executive Officer",
        "branch": "GetSetAI, India",
        "community_id": "1GSAI001"
    },
    {
        "name": "Shri Sawariya Seth",
        "image": "/static/images/employee/sawariya.jpg",
        "designation": "Managing Director",
        "branch": "GetSetAI, India",
        "community_id": "1GSAI002"
    },
    {
        "name": "Abhishek Sahoo",
        "image": "/static/images/employee/abhishek.jpg",
        "designation": "Chief Technical Officer",
        "branch": "GetSetAI, Bangalore",
        "community_id": "1GSAI003"
    },
    {
        "name": "Nageshwar Yadav",
        "image": "/static/images/employee/Nageshwar.png",
        "designation": "Head Of Finance",
        "branch": "GetSetAI, Bhilai",
        "community_id": "1GSAI004"
    },
    {
        "name": "Harsh Vaishnav",
        "image": "/static/images/employee/harsh.jpg",
        "designation": "Chief Operating Officer",
        "branch": "GetSetAI, Bhilai",
        "community_id": "1GSAI005"
    },
    {
        "name": "Harnish Chhabra",
        "image": "/static/images/employee/harnish.jpg",
        "designation": "Social Media & Content Head",
        "branch": "GetSetAI, Bhilai",
        "community_id": "1GSAI006"
    },
    {
        "name": "Sanidhya Mishra",
        "image": "/static/images/employee/sanidhya.jpg",
        "designation": "Administrative Head",
        "branch": "GetSetAI, Bhilai",
        "community_id": "1GSAI007"
    },
    {
        "name": "Abhineet Singh",
        "image": "/static/images/employee/Abhineet.png",
        "designation": "Strategy and Operations Head",
        "branch": "GetSetAI, Bhilai",
        "community_id": "1GSAI008"
    },
    {
        "name": "Shivesh Singh Rajput",
        "image": "/static/images/employee/shivesh.png",
        "designation": "Principal Consultant",
        "branch": "GetSetAI, Bhilai",
        "community_id": "1GSAI009"
    },
    {
        "name": "Piyush Rane",
        "image": "/static/images/employee/piyush.png",
        "designation": "Visual Content Manager",
        "branch": "GetSetAI, Bhilai",
        "community_id": "1GSAI012"
    },

]

# ✅ Employee Listing Page
@app.get("/employees", response_class=HTMLResponse)
async def get_employees(request: Request):
    return templates.TemplateResponse("employee/employee.html", {
        "request": request,
        "employees": employees,
        "title": "Meet Our Team"
    })

# ✅ Single Employee Detail Page (Dynamic)
@app.get("/employee/{emp_id}", response_class=HTMLResponse)
async def employee_detail(request: Request, emp_id: str):
    employee = next((emp for emp in employees if emp["community_id"] == emp_id), None)
    if not employee:
        return templates.TemplateResponse("employee/404.html", {"request": request, "title": "Not Found"})
    
    return templates.TemplateResponse("employee/detail.html", {
        "request": request,
        "employee": employee,
        "title": employee["name"]
    })






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
@app.get("/innovate", response_class=HTMLResponse)
async def show_event_gallery(request: Request):
    return templates.TemplateResponse("pastevents/innovatex.html", {
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



# ✅ Past Events Gallery Page
@app.get("/shivam-institute", response_class=HTMLResponse)
async def show_event_gallery(request: Request):
    return templates.TemplateResponse("pastevents/shivaminst.html", {
        "request": request,
        "title": "Past Events"
    })






