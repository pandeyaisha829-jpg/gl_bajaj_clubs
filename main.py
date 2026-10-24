from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI(title="GL Bajaj Campus Guide - Clubs Module")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Detailed Club Data Engine
CLUBS_DATA = [
    {
        "id": "navrang",
        "name": "Navrang - The Cultural Club",
        "type": "Cultural",
        "department": "Institutional Cultural Wing",
        "faculty_coordinator": {
            "name": "Dr. Shilpa Choudhary",
            "role": "Faculty Coordinator",
            "image": "/static/images/navrang_mentor.jpeg"
        },
        "core_team": {
            "president": "Akul singh katiyar",
            "vice_presidents": ["Aradhya panwar", "Shrey"],
            "secretary": "Aman mishra",
            "treasurer": "Supriya verma"
        },
        "avenues": [
            {
                "name": "Dance Avenue",
                "convenor": "Ananya",
                "co_convenor": "Arya",
                "executives": ["Astitva", "Pushkar", "Atifa", "Palak"]
            },
            {
                "name": "Music Avenue",
                "convenor": "Pragya",
                "co_convenor": "Kushagra",
                "executives": ["Om", "Shubh"]
            },
            {
                "name": "Management Avenue",
                "convenor": "Saksham",
                "co_convenor": "Pranit",
                "executives": ["Kirti", "Deepak"]
            },
            {
                "name": "Technical Avenue",
                "convenor": "Tushar",
                "co_convenor": "Palak",
                "executives": ["Digvijay", "Samman"]
            }
        ],
        "past_events": [
            {"title": "Music Jamming Session", "description": "Open stage acoustic jamming session.", "image": "/static/images/music_jamming.jpeg"},
            {"title": "Flashmob", "description": "Surprise synchronized dance performance.", "image": "/static/images/flashmob.jpeg"},
            {"title": "Dandiya Night 2026", "description": "Grand festive cultural evening.", "image": "/static/images/dandiya_night.jpeg"}
        ]
    },
    {
        "id": "vibeesta",
        "name": "Vibeesta - The Music & Band Society",
        "type": "Cultural/Music",
        "department": "Student Activity Centre",
        "faculty_coordinator": {
            "name": "Amit vista",
            "role": "president",
            "image": "/static/images/amit.jpeg"
        },
        "core_team": {
            "president": "Amit vista",
            "vice_presidents": ["Sanya Arora"],
            "secretary": "Aman Deep",
            "treasurer": "Riya Garg"
        },
        "avenues": [
            {"name": "Vocal Wing", "convenor": "Kavya", "co_convenor": "Rahul", "executives": ["Siddharth"]},
            {"name": "Instrumental Wing", "convenor": "Dev", "co_convenor": "Sameer", "executives": ["Rohan"]}
        ],
        "past_events": [
            {"title": "Unplugged Acoustic Night", "description": "Soulful music under the stars.", "image": "/static/images/music_jamming.jpeg"}
        ]
    },
    {
        "id": "codespace",
        "name": "Codespace - Official IT Club",
        "type": "Technical",
        "department": "Department of Information Technology",
        "faculty_coordinator": {
            "name": "Dr PC vashist",
            "role": "HOD it departement",
            "image": "/static/images/hod.jpeg"
        },
        "core_team": {
            "president": "Yuvraj pratap singh",
            "vice_presidents": ["Shantanu katiyar"],
            "secretary": "Raghavendra shah",
            "treasurer": "Bhavya kansal"
        },
        "avenues": [
            {"name": "Tech Team", "convenor": "Ayush", "co_convenor": "Gatik juneja", "executives": ["Nikhil"]}
        ],
        "past_events": [
            {"title": "Aagaz 3.0", "description": "Annual orientation ceremony.", "image": "/static/images/codespace_orientation.jpeg"}
        ]
    }
]

FEEDBACK_STORE = []
TEAM_STATUS_DATA = [
    {"name": "Ananya Singhal", "club": "Navrang", "avenue": "Dance Avenue", "role": "Convenor", "status": "Active", "event": "Flashmob & Dandiya"},
    {"name": "Pragya Rajput", "club": "Navrang", "avenue": "Dance Avenue", "role": "Member", "status": "Inactive", "event": "Dandiya Night"}
]
CONVENOR_CONFIDENTIAL_REVIEWS = [
    {"convenor": "Ananya Singhal", "club": "Navrang - Dance Avenue", "rating": "⭐⭐⭐⭐⭐", "review": "Exceptional execution during flashmob rehearsals."}
]

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"clubs": CLUBS_DATA})

@app.get("/club/{club_id}")
async def club_detail(request: Request, club_id: str):
    selected_club = next((club for club in CLUBS_DATA if club["id"] == club_id), None)
    if not selected_club:
        return templates.TemplateResponse(request, "index.html", {"clubs": CLUBS_DATA})
    return templates.TemplateResponse(request, "club_detail.html", {"club": selected_club})

@app.post("/submit-feedback")
async def submit_feedback(request: Request, name: str = Form(...), email: str = Form(...), club: str = Form(...), message: str = Form(...)):
    FEEDBACK_STORE.append({"name": name, "email": email, "club": club, "message": message})
    return templates.TemplateResponse(request, "index.html", {"clubs": CLUBS_DATA, "feedback_sent": True})

@app.get("/core-team-portal")
async def core_team_portal(request: Request, passcode: str = ""):
    if passcode != "GLB-Core2026-Navrang#Sec":
        return templates.TemplateResponse(request, "unauthorized.html", {})
    return templates.TemplateResponse(request, "core_team.html", {"team_status": TEAM_STATUS_DATA, "reviews": CONVENOR_CONFIDENTIAL_REVIEWS, "feedbacks": FEEDBACK_STORE})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)