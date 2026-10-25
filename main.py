from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI(title="GL Bajaj Campus Guide - Clubs Module")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

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
                "executives": ["Astitva", "Pushkar", "Atifa", "Palak"],
                "members": ["Ananya Singhal", "Arya Tomar", "Astitva Agrawal", "Pushkar Singh", "Palak Aggarwal", "Atifa Zareef", "Aisha Pandey", "Pragya Rajput"]
            },
            {
                "name": "Music Avenue",
                "convenor": "Pragya",
                "co_convenor": "Kushagra",
                "executives": ["Om", "Shubh"],
                "members": ["Pragya", "Kushagra", "Om", "Shubh", "Vaishnavi Pandey", "Krish Kumar", "akash gupta"]
            },
            {
                "name": "Management Avenue",
                "convenor": "Saksham",
                "co_convenor": "Pranit",
                "executives": ["Kirti", "Deepak"],
                "members": ["Saksham", "Pranit", "Kirti", "Deepak", "Ajita"]
            },
            {
                "name": "Technical Avenue",
                "convenor": "Tushar",
                "co_convenor": "Palak",
                "executives": ["Digvijay", "Samman"],
                "members": ["Tushar", "Palak", "Digvijay", "Samman", "Rimjhim Kumari"]
            }
        ],
        "past_events": [
            {"title": "Music Jamming Session", "description": "Open stage acoustic jamming session.", "image": "/static/images/music_jamming.jpeg"},
            {"title": "Flashmob", "description": "Surprise synchronized dance performance.", "image": "/static/images/flashmob.jpeg"},
            {"title": "Dandiya Night 2026", "description": "Grand festive cultural evening.", "image": "/static/images/dandiya_night.jpeg"}
        ],
        "upcoming_events": [
            {"title": "Annual Fest - Pratibha 2026", "date": "15th Nov 2026", "venue": "SHD hall"},
            {"title": "Inter-College Dance Battle", "date": "28th Nov 2026", "venue": "SBG hall"}
        ]
    },
    {
        "id": "vibeesta",
        "name": "Vibeesta - The Music & Band Society",
        "type": "Cultural/Music",
        "department": "Student Activity Centre",
        "faculty_coordinator": {
            "name": "Amit vista",
            "role": "President",
            "image": "/static/images/amit.jpeg"
        },
        "core_team": {
            "president": "Amit vista",
            "vice_presidents": ["Sanya Arora"],
            "secretary": "Aman Deep",
            "treasurer": "Riya Garg"
        },
        "avenues": [
            {"name": "Music", "convenor": "Kavya", "co_convenor": "Rahul", "executives": ["Siddharth"], "members": ["Kavya", "Rahul", "Siddharth"]}
        ],
        "past_events": [
            {"title": "Vibrant-2026", "description": "an intercollege event.", "image": "/static/images/vibrant.jpeg"}
        ],
        "upcoming_events": [
            {"title": "Battle of Bands", "date": "10th Dec 2026", "venue": "Sports Ground"}
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
  {"name": "Social Media", "convenor": "Varnika malik", "co_convenor": "Aayush srivastava", "executives": ["Mayank"], "members": ["kavya", "aditya", "siddharth"]},
  {"name": "Tech Team", "convenor": "Ayush", "co_convenor": "Gatik juneja", "executives": ["Nikhil"], "members": ["akansha", "amit", "aditya"]},
  {"name": "Photography", "convenor": "Harsh mishra", "co_convenor": "Shiwanshu tiwari", "executives": ["Divyansh"], "members": ["anjali", "Rahul", "shreya"]},
  

        ],
        "past_events": [
            {"title": "Aagaz 3.0", "description": "Annual orientation ceremony.", "image": "/static/images/codespace_orientation.jpeg"}
        ],
        "upcoming_events": [
            {"title": "Hack-IT 2026", "date": "5th Dec 2026", "venue": "IT Computer Labs"}
        ]
    }
]

FEEDBACK_STORE = []
TEAM_STATUS_DATA = [
    {"name": "Ananya Singhal", "club": "Navrang", "avenue": "Dance Avenue", "role": "Convenor", "status": "Active", "event": "Flashmob & Dandiya"},
    {"name": "Pragya Rajput", "club": "Navrang", "avenue": "Dance Avenue", "role": "Member", "status": "Inactive", "event": "Dandiya Night"},
]
CONVENOR_CONFIDENTIAL_REVIEWS = [
    {"convenor": "Ananya Singhal", "club": "Navrang - Dance Avenue", "rating": "⭐⭐⭐⭐⭐", "review": "Exceptional execution during flashmob rehearsals."}
]

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"clubs": CLUBS_DATA, "feedback_sent": False})

@app.post("/submit-feedback")
async def submit_feedback(request: Request, name: str = Form(...), email: str = Form(...), club: str = Form(...), message: str = Form(...)):
    FEEDBACK_STORE.append({"name": name, "email": email, "club": club, "message": message})
    return templates.TemplateResponse(request, "index.html", {"clubs": CLUBS_DATA, "feedback_sent": True})

@app.get("/core-team-portal")
async def core_team_portal(request: Request, passcode: str = ""):
    if passcode != "GLB-2026":
        return templates.TemplateResponse(request, "unauthorized.html", {})
    return templates.TemplateResponse(request, "core_team.html", {"team_status": TEAM_STATUS_DATA, "reviews": CONVENOR_CONFIDENTIAL_REVIEWS, "feedbacks": FEEDBACK_STORE})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)