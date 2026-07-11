from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request, FastAPI
from services.metadata import (
    search_songs,
    audio_metadata, 
    get_song_details,
    get_recommendations
)
from services.audio_extract import(
     retrived_audio,
     get_audio_by_video_id
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

templates = Jinja2Templates(
    directory="template"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/favicon.ico")
async def favicon():
    return FileResponse("favicon.ico")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
       request=request,
       name="index.html",
       context={}
    )

@app.get("/search")
def search(query:str, offset:int = 0, limit: int = 20):
    return search_songs(query,offset,limit)

@app.get("/player")
async def player_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="player.html",
        context={}
    )

@app.get("/song/{video_id}")
def get_song(video_id:str):
    details = get_song_details(video_id)
    audio_url = get_audio_by_video_id(video_id)

    return {

        "videoId": video_id,
        "title": details["title"],
        "artist": details['artist'],
        "thumbnail": f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg",
        "audioUrl": audio_url

    }

@app.get("/recommend/{video_id}")
def recommend(video_id: str):

    return get_recommendations(video_id)

@app.get("/play")
def play(song: str):
  return retrived_audio(song)

