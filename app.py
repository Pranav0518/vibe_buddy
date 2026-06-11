from fastapi import FastAPI
from audio_extract import retrived_audio
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

@app.get("/play")
def play(song: str):
  return retrived_audio(song)

