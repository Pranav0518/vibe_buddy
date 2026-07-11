from ytmusicapi import YTMusic
from services.recommendation_engine import smart_search
yt = YTMusic()

#Function to retrieve thes
def audio_metadata(song_name):
    results = yt.search( 
        song_name,
        filter = "songs"
    )

    song = results[0]
    video_Id = song["videoId"]

    #print(song["title"])
    #print(song["videoId"])
    return {
       
        "videoId": video_Id,
        "title": song["title"],
        "artist":  ",".join(
            artist["name"]
            for artist in song["artists"]),
        "thumbnail": f"https://i.ytimg.com/vi/{video_Id}/maxresdefault.jpg",
        "fallbackThumbnail": f"https://i.ytimg.com/vi/{video_Id}/hqdefault.jpg"

    }

def search_songs(query,offset=0,limit=20):

    result = smart_search(query)
    return result[offset: offset + limit]

def get_song_details(video_id):

    results = yt.search(
        video_id,
        filter="songs"
    )

    if not results:
        return None

    song = results[0]

    return {
        "title": song["title"],
        "artist": ",".join(
            artist["name"]
            for artist in song["artists"]
        ),
        "thumbnail":
            f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
    }

def get_recommendations(video_id):

    playlist = yt.get_watch_playlist(
        videoId=video_id
    )

    recommendations = []

    for track in playlist["tracks"][:20]:

        recommendations.append({

            "videoId":
                track["videoId"],

            "title":
                track["title"],

            "artist":
                ",".join(
                    artist["name"]
                    for artist in track["artists"]
                ),

            "thumbnail":
                f"https://i.ytimg.com/vi/{track['videoId']}/hqdefault.jpg"
        })

    return recommendations
def search_song_v2(query):
    yt.search(
        query,
        filter="albums"
    )
    yt.get_album(
        browseID
    )
    