
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import google.generativeai as genai



load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)
app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TravelPlanRequest(BaseModel):
    style: str
    place: str
    duration: str
    demand: str

@app.post('/travel-story')
async def travel_story(req: TravelPlanRequest):
    style_map = {
        'alone': 'a solo traveler',
        'family': 'a family',
        'couple': 'a couple',
    }
    style_text = style_map.get(req.style, 'a traveler')
    prompt = (
        f"Write a short, fun travel story for {style_text} going to {req.place} for {req.duration}. "
        f"They have this special wish: {req.demand}. "
        f"Make it vivid, positive, and inspiring."
        f"make three paragraphs using <p> elements"
    )
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    story = response.text.strip()
    return {"story": story}
