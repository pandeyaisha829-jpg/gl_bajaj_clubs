from fastapi import FastAPI, Request
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
                "title": "Freshers Party",
                "date": "2026-11-12",
                "venue": "Sports Ground",
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
            {"name": "Vocal Wing", "convenor": "Kavya", "co_convenor": "Rahul"},
            {"name": "Instrumental Wing", "convenor": "Dev", "co_convenor": "Sameer"}
        ],
        "past_events": [
            {"title": "Unplugged Acoustic Night", "description": "Soulful music renditions under the star.", "image": "/static/images/music_jamming.jpeg"}
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
            "name": "Prof. Dr PC vashist",
            "role": "Chief Mentor",
            "image": "/static/images/hod.jpeg"
        },
        "core_team": {
            "president": "Yuvraj pratap singh",
            "vice_presidents": ["Shantanu katiyar"],
            "secretary": "Raghavendra shah",
            "treasurer": "Bhavya kansal"
        },
        "avenues": [
            {"name": "Social Media", "convenor": "Varnika malik", "co_convenor": "Aayush srivastava"},
            {"name": "Tech Team", "convenor": "Ayush", "co_convenor": "Gatik juneja"},
            {"name": "Photography", "convenor": "Harsh mishra", "co_convenor": "Shiwanshu tiwari"}
        ],
        "past_events": [
            {"title": "Aagaz 3.0", "description": "Orientation ceremony of codespace.", "image": "/static/images/codespace_orientation.jpeg"}
        ],
        "upcoming_events": [
            {"title": "Hack-IT 2026", "date": "2026-11-25", "venue": "IT Block Computer Labs", "coordinates": {"lat": 28.4718, "lng": 77.4885}}
        ]
    }
]

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"clubs": CLUBS_DATA})

@app.get("/api/clubs")
def get_clubs_api():
    return {"status": "success", "data": CLUBS_DATA}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)