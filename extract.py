import sys
from audio_extract import retrived_audio

song_name =  " ".join(sys.argv[1:])

try:
    audio_url = retrived_audio(song_name)
    print(audio_url)
except Exception as e:
    print(f"Error: {str(e)}")
    print(1)