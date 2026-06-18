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

def search_songs(query,offset=0,limit=20):

    search_results = yt.search(
        query,
        filter="songs"
    )

    if not search_results:
        return []

    primary_song = search_results[0]

    songs = []

    seen = set()

    # Exact match first

    video_id = primary_song["videoId"]

    songs.append({

        "videoId": video_id,

        "title":
            primary_song["title"],

        "artist":
            ",".join(
                artist["name"]
                for artist in primary_song["artists"]
            ),

        "thumbnail":
            f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg",

        "fallbackThumbnail":
            f"https://i.ytimg.com/vi/{video_id}/mqdefault.jpg"
    })

    seen.add(video_id)

    try:

        recommendations = yt.get_watch_playlist(
            videoId=video_id
        )

        for track in recommendations["tracks"]:

            track_id = track.get("videoId")

            if not track_id:
                continue

            if track_id in seen:
                continue

            songs.append({

                "videoId": track_id,

                "title":
                    track["title"],

                "artist":
                    ",".join(
                        artist["name"]
                        for artist in track["artists"]
                    ),

                "thumbnail":
                    f"https://i.ytimg.com/vi/{track_id}/hqdefault.jpg",

                "fallbackThumbnail":
                    f"https://i.ytimg.com/vi/{track_id}/mqdefault.jpg"
            })

            seen.add(track_id)

    except Exception as e:

        print(
            "Recommendation Error:",
            e
        )

    return songs[
        offset:
        offset + limit
    ]

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
    