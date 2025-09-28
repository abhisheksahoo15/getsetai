from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
from google.oauth2 import service_account
from googleapiclient.discovery import build

import os

app = FastAPI()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")




# ------------------ Routes ------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "GetSetAI"})


@app.post("/chat", response_class=JSONResponse)
async def chat(user_input: str = Form(...)):
    prompt = f"User: {user_input}\nAI:"
    output = chatbot(prompt, max_new_tokens=100, do_sample=True, temperature=0.7)[0]['generated_text']
    response = output.split("AI:")[-1].strip() if "AI:" in output else output.strip()
    return JSONResponse(content={"response": response})

@app.get("/upcoming", response_class=HTMLResponse)
async def show_upcoming_events(request: Request):
    return templates.TemplateResponse("upcoming.html", {"request": request, "title": "Upcoming Events"})

@app.get("/detail", response_class=HTMLResponse)
async def show_event_detail(request: Request):
    return templates.TemplateResponse("detail.html", {"request": request, "title": "Event Details"})

@app.get("/gallery", response_class=HTMLResponse)
async def show_event_gallery(request: Request):
    return templates.TemplateResponse("eventgallary.html", {"request": request, "title": "Past Events"})

@app.get("/ssmv", response_class=HTMLResponse)
async def show_ssmv(request: Request):
    return templates.TemplateResponse("pastevents/ssmv1.html", {"request": request, "title": "Past Events"})

@app.get("/innovate", response_class=HTMLResponse)
async def show_innovate(request: Request):
    return templates.TemplateResponse("pastevents/innovatex.html", {"request": request, "title": "Past Events"})

@app.get("/details", response_class=HTMLResponse)
async def show_details(request: Request):
    return templates.TemplateResponse("detail.html", {"request": request, "title": "Detail"})

@app.get("/about", response_class=HTMLResponse)
async def show_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "title": "About"})

@app.get("/contact", response_class=HTMLResponse)
async def show_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "title": "Contact"})

@app.get("/shivam-institute", response_class=HTMLResponse)
async def show_shivam_institute(request: Request):
    return templates.TemplateResponse("pastevents/shivaminst.html", {"request": request, "title": "Past Events"})

# ------------------ Employees ------------------

employees = [
    # {"name": "Shri Jagannath", "image": "/static/images/employee/jagga.jpg", "designation": "Chief Executive Officer", "branch": "GetSetAI, India", "community_id": "1GSAI001"},
    # {"name": "Shri Sawariya Seth", "image": "/static/images/employee/sawariya.jpg", "designation": "Managing Director", "branch": "GetSetAI, India", "community_id": "1GSAI002"},
    {"name": "Abhishek Sahoo", "image": "/static/images/employee/abhishek.jpg", "designation": "Chief Technical Officer", "branch": "GetSetAI, Bangalore", "community_id": "1GSAI003"},
    # {"name": "Nageshwar Yadav", "image": "/static/images/employee/Nageshwar.png", "designation": "Head Of Finance", "branch": "GetSetAI, Bhilai", "community_id": "1GSAI004"},
    {"name": "Harsh Vaishnav", "image": "/static/images/employee/harsh.jpg", "designation": "Chief Operating Officer", "branch": "GetSetAI, Bhilai", "community_id": "1GSAI005"},
    {"name": "Harnish Chhabra", "image": "/static/images/employee/harnish.jpg", "designation": "Social Media & Content Head", "branch": "GetSetAI, Bhilai", "community_id": "1GSAI006"},
    {"name": "Sanidhya Mishra", "image": "/static/images/employee/sanidhya.jpg", "designation": "Administrative Head", "branch": "GetSetAI, Bhilai", "community_id": "1GSAI007"},
    # {"name": "Abhineet Singh", "image": "/static/images/employee/Abhineet.png", "designation": "Strategy and Operations Head", "branch": "GetSetAI, Bhilai", "community_id": "1GSAI008"},
    # {"name": "Shivesh Singh Rajput", "image": "/static/images/employee/shivesh.png", "designation": "Principal Consultant", "branch": "GetSetAI, Bhilai", "community_id": "1GSAI009"},
    # {"name": "Piyush Rane", "image": "/static/images/employee/piyush.png", "designation": "Visual Content Manager", "branch": "GetSetAI, Bhilai", "community_id": "1GSAI012"},
    {"name": "B. Bharadwaj", "image": "/static/images/employee/bharadwaj.jpg", "designation": "Desigining Head ", "branch": "GetSetAI, Bhilai", "community_id": "1GSAI007"},
]

@app.get("/employees", response_class=HTMLResponse)
async def get_employees(request: Request):
    return templates.TemplateResponse("employee/employee.html", {
        "request": request,
        "employees": employees,
        "title": "Meet Our Team"
    })

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

# ------------------ Custom 404 Handler ------------------


# ------------------ Custom 404 Handler ------------------

@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse("404.html", {"request": request, "title": "Page Not Found"}, status_code=404)
    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)



SERVICE_ACCOUNT_FILE = os.path.join(".gitignore", "credentials", "service_account.json")
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "14DBCsBam8PmM6YLBXRrz7UOuJEkGxH46LdT4G9nMSCU"  # <-- Replace with your Google Sheet ID

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build("sheets", "v4", credentials=credentials)
sheet = service.spreadsheets()

# ---------------- Routes ----------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "GetSetAI"})


@app.get("/sheet-data")
async def get_sheet_data():
    """
    Reads all rows from Google Sheet (first sheet by default).
    """
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range="Sheet1").execute()
    values = result.get("values", [])
    return {"data": values}


@app.post("/sheet-add")
async def add_sheet_data(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):
    """
    Append a row to Google Sheet.
    """
    values = [[name, email, message]]
    body = {"values": values}

    result = sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range="Sheet1",
        valueInputOption="RAW",
        body=body
    ).execute()

    return {"status": "success", "updated": result.get("updates")}