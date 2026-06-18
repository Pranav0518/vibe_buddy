from fastapi import FastAPI
from audio_extract import retrived_audio
from metadata import search_songs,audio_id, get_song_details,get_recommendations
from audio_extract import get_audio_by_video_id
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
app = FastAPI()

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
async def home():
    return FileResponse("template/index.html")

@app.get("/search")
def search(query:str, offset:int = 0, limit: int = 20):
    return search_songs(query,offset,limit)

@app.get("/player")
async def player_page():
    return FileResponse(
        "template/player.html"
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

