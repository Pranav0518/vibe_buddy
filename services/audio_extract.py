from yt_dlp import YoutubeDL 
from services.metadata import audio_metadata

def retrived_audio(song_name):
    info = audio_metadata(song_name)
    video_id = info["videoId"]
    #print(video_id)

    url = f"https://www.youtube.com/watch?v={video_id}"
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "no_warnings": True,

    }

    with YoutubeDL(ydl_opts) as ydl:
        yt_info = ydl.extract_info(url, download = False)
        audio_url = yt_info["url"]

    return {
    "title": info["title"],
    "artist": info["artist"],
    "thumbnail": info["thumbnail"],
    "audioUrl": audio_url
    }
def get_audio_by_video_id(video_id):

    url = (
        f"https://www.youtube.com/watch?v={video_id}"
    )

    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "no_warnings": True
    }

    with YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(
            url,
            download=False
        )

        audio_url = info["url"]

    return audio_url