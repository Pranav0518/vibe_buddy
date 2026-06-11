from ytmusicapi import YTMusic

yt = YTMusic()

def audio_id(song_name):
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


#print('/n',song)
#print(results)