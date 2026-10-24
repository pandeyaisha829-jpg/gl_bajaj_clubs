from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI(title="GL Bajaj Campus Guide - Clubs & Events Module")

# Mount static files and templates
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
            "treasurer": "Supriya verma",
            "banner_image": "/static/images/core_team.jpeg"
        },
        "avenues": [
            {
                "name": "Dance Avenue",
                "convenor": "Ananya",
                "co_convenor": "Arya",
                "executives": ["Astitva", "Pushkar", "Atifa", "Palak"],
                "members": [
                    "Ananya Singhal", "Arya Tomar", "Astitva Agrawal", "Pushkar Singh", 
                    "Palak Aggarwal", "Atifa Zareef", "Saumya Sanu", "Aisha Pandey", 
                    "Aanchal", "Shambhavi Srivastava", "Vivek", "Gaurie N Varshney", 
                    "Vaibhav Saxena", "Brinda Singh", "Shrishti Srivastava", "Riya Jaiswal", 
                    "Vaishnavi Gupta", "Akanksha Gupta", "Tanushka Gaur", "Vyom Khushwaha", 
                    "Janvi Karira", "Puja Kumari", "Amit Kumar", "Tanishka Singh", 
                    "Jiya Kumari", "Vaishnavi Pathak", "Tanya Gautam", "Anoushka Verma", 
                    "Anurag Maurya", "Samriddhi", "Shreya Singh", "Vaishnavi Singh", 
                    "Ashita Vishwakarma", "Aditi Shreya", "Agam Raj", "Nainsi Jaiswal", 
                    "Shrasti Agnihotri", "Mani Rawat", "Adarsh", "Aayushi Sharma", 
                    "Saksham Agarwal", "Aditi Pratap Singh", "Pragya Rajpoot"
                ],
                "image": "/static/images/dance_avenue.jpeg"
            },
            {
                "name": "Music Avenue",
                "convenor": "Pragya",
                "co_convenor": "Kushagra",
                "executives": ["Om", "Shubh"],
                "members": ["Abhinav Kumar Sehgal", "Aditi Shreya", "Akansha Sharma"]
            },
            {
                "name": "Management Avenue",
                "convenor": "Saksham",
                "co_convenor": "Pranit",
                "executives": ["Kirti", "Deepak"],
                "members": ["Kirti Goyal", "Deepak Sharma"]
            },
            {
                "name": "Technical Avenue",
                "convenor": "Tushar",
                "co_convenor": "Palak",
                "executives": ["Digvijay", "Samman"]
            },
            {
                "name": "Poetry Avenue",
                "convenor": "Anuj",
                "co_convenor": "Jyotika",
                "executives": ["Marz", "Pavitra"]
            },
            {
                "name": "Drama Avenue",
                "convenor": "Kabir",
                "co_convenor": "Anshika",
                "executives": ["Sohini", "Adarsh"],
                "members": ["Vyom Kushwaha", "Tripti Dhariwal", "Vivek"]
            },
            {
                "name": "Photography Avenue",
                "convenor": "Parsh",
                "co_convenor": "Anshul",
                "executives": ["Abhishek", "Raj"]
            }
        ],
        "past_events": [
            {
                "title": "Music Jamming Session",
                "description": "An open stage acoustic jamming session in the sports ground.",
                "image": "/static/images/music_jamming.jpeg"
            },
            {
                "title": "Flashmob",
                "description": "A surprise synchronized dance performance by dance avenue at the main ground.",
                "image": "/static/images/flashmob.jpeg"
            },
            {
                "title": "Dandiya Night 2026",
                "description": "Grand festive cultural evening with traditional Garba and Dandiya performances.",
                "image": "/static/images/dandiya_night.jpeg"
            }
        ],
        "upcoming_events": [
            {
                "title": "Freshers Party 2026",
                "date": "2026-11-12",
                "venue": "Main Sports Ground",
                "coordinates": {"lat": 28.472979, "lng": 77.488693}
            }
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
            "image": "/static/images/music_avenue.jpeg"
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
            {"title": "Unplugged Acoustic Night", "description": "Soulful music renditions under the stars.", "image": "/static/images/music_jamming.jpeg"}
        ],
        "upcoming_events": [
            {"title": "Battle of Bands 2026", "date": "2026-11-20", "venue": "Open Air Theatre (OAT)", "coordinates": {"lat": 28.4725, "lng": 77.4892}}
        ]
    },
    {
        "id": "codespace",
        "name": "Codespace - Official IT Department Club",
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
            {"name": "Social Media", "convenor": "Varnika malik", "co_convenor": "Aayush srivastava", "executives": ["Mayank"]},
            {"name": "Tech Team", "convenor": "Ayush", "co_convenor": "Gatik juneja", "executives": ["Nikhil"]},
            {"name": "Photography", "convenor": "Harsh mishra", "co_convenor": "Shiwanshu tiwari", "executives": ["Divyansh"]}
        ],
        "past_events": [
            {"title": "Aagaz 3.0", "description": "Annual orientation ceremony of Codespace club.", "image": "/static/images/codespace_orientation.jpeg"}
        ],
        "upcoming_events": [
            {"title": "Hack-IT 2026", "date": "2026-11-25", "venue": "IT Block Computer Labs", "coordinates": {"lat": 28.4718, "lng": 77.4885}}
        ]
    }
]

# Stores feedback submitted dynamically
FEEDBACK_STORE = []

# Core Team Activity Data & Confidential Feedback
TEAM_STATUS_DATA = [
    {"name": "Ananya Singhal", "club": "Navrang", "avenue": "Dance Avenue", "role": "Convenor", "status": "Active", "event": "Flashmob & Dandiya Night"},
    {"name": "Aisha Pandey", "club": "Navrang", "avenue": "Dance Avenue", "role": "Member", "status": "Active", "event": "Flashmob & Music Jamming"},
    {"name": "Pragya Rajput", "club": "Navrang", "avenue": "Dance Avenue", "role": "Member", "status": "Inactive", "event": "Dandiya Night 2026"},
    {"name": "Vaishnavi Pandey", "club": "Navrang", "avenue": "Music Avenue", "role": "Member", "status": "Inactive", "event": "Music Jamming Session"},
    {"name": "Krish Kumar", "club": "Navrang", "avenue": "Music Avenue", "role": "Member", "status": "Inactive", "event": "Acoustic Night"},
    {"name": "Ajita", "club": "Navrang", "avenue": "Management Avenue", "role": "Member", "status": "Inactive", "event": "Dandiya Night Management"},
    {"name": "Rimjhim Kumari", "club": "Navrang", "avenue": "Technical Avenue", "role": "Member", "status": "Inactive", "event": "Tech Workshop"},
    {"name": "Arya Tomar", "club": "Navrang", "avenue": "Dance Avenue", "role": "Co-Convenor", "status": "Active", "event": "Flashmob Choreography"},
    {"name": "Saksham Agarwal", "club": "Navrang", "avenue": "Dance Avenue", "role": "Member", "status": "Active", "event": "Flashmob"},
    {"name": "Pragya", "club": "Navrang", "avenue": "Music Avenue", "role": "Convenor", "status": "Active", "event": "Unplugged Night"}
]

CONVENOR_CONFIDENTIAL_REVIEWS = [
    {"convenor": "Ananya Singhal", "club": "Navrang - Dance Avenue", "rating": "⭐⭐⭐⭐⭐", "review": "Exceptional execution during flashmob rehearsals and student team management."},
    {"convenor": "Pragya", "club": "Navrang - Music Avenue", "rating": "⭐⭐⭐⭐☆", "review": "Great coordination for acoustics night; recommended to delegate technical sound setup early."},
    {"convenor": "Kavya", "club": "Vibeesta - Vocal Wing", "rating": "⭐⭐⭐⭐⭐", "review": "Highly active during practice sessions and seamless venue booking coordination."},
    {"convenor": "Ayush", "club": "Codespace - Tech Team", "rating": "⭐⭐⭐⭐☆", "review": "Strong technical oversight; ensure all venue portal permissions are submitted prior to event deadlines."}
]

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"clubs": CLUBS_DATA, "feedback_sent": False})

@app.post("/submit-feedback")
async def submit_feedback(request: Request, name: str = Form(...), email: str = Form(...), club: str = Form(...), message: str = Form(...)):
    FEEDBACK_STORE.append({"name": name, "email": email, "club": club, "message": message})
    return templates.TemplateResponse(request, "index.html", {"clubs": CLUBS_DATA, "feedback_sent": True, "sender_name": name})

@app.get("/core-team-portal")
async def core_team_portal(request: Request, passcode: str = ""):
    if passcode != "glbajaj2026":
        return templates.TemplateResponse(request, "unauthorized.html", {})
    
    return templates.TemplateResponse(request, "core_team.html", {
        "team_status": TEAM_STATUS_DATA,
        "reviews": CONVENOR_CONFIDENTIAL_REVIEWS,
        "feedbacks": FEEDBACK_STORE
    })

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)