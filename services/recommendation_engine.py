from ytmusicapi import YTMusic
yt = YTMusic()

def search_exact_songs(query):
    results = yt.search(
        query,
        filter = "songs"
    )

    songs = []
    for song in results[:10]:
        songs.append({
            "sources": ["song"],
            "videoId": song["videoId"],
            "title": song["title"],
            "artist":", ".join(
                artist["name"] 
                for artist in song["artists"]
            ),
            "thumbnail": f"https://i.ytimg.com/vi/{song['videoId']}/hqdefault.jpg"
        })
    #print(songs)
    return songs

def search_album(query):
    albums = yt.search(
        query,
        filter = "albums"
    )
    songs =[]

    if not albums:
        return songs
    
    album = yt.get_album(
        albums[0]["browseId"]
    )

    for track in album["tracks"]:
        songs.append({

            "sources": ["album"],

            "videoId":
                track["videoId"],

            "title":
                track["title"],

            "artist":
                ", ".join(
                    artist["name"]
                    for artist in track["artists"]
                ),

            "thumbnail":
                f"https://i.ytimg.com/vi/{track['videoId']}/hqdefault.jpg"

        })
    #print(songs)
    return songs

def search_artist(query):
    artists = yt.search(
        query,
        filter="artists"
    )

    songs = []

    if not artists:
        return songs

    artist = yt.get_artist(
        artists[0]["browseId"]
    )

    for track in artist.get("songs", {}).get("results",[] ):

        songs.append({

            "sources": ["artist"],

            "videoId":
                track["videoId"],

            "title":
                track["title"],

            "artist":
                ", ".join(
                    artist["name"]
                    for artist in track["artists"]
                ),

            "thumbnail":
                f"https://i.ytimg.com/vi/{track['videoId']}/hqdefault.jpg"

        })
   # print(songs)
    return songs

def watch_playlist_graph(video_id):

    recommendations = []
    try:
        playlist = yt.get_watch_playlist(
            videoId=video_id
        )

        for track in playlist.get("tracks",[]):
            if "videoId" not in track:
                continue
                
            recommendations.append({
                "sources": ["watch_graph"],

                "videoId":
                    track["videoId"],

                "title":
                    track["title"],

                "artist":
                    ", ".join(
                        artist["name"]
                        for artist in track.get("artists", [])
                    ),

                "thumbnail":
                    f"https://i.ytimg.com/vi/{track['videoId']}/hqdefault.jpg"
            })

    except Exception as e:
        print(
            "Watch Graph Error:",e
        )
    
    return recommendations


def remove_duplicates(results):
        unique = {}

        for song in results:

            video_id = song["videoId"]

            if video_id not in unique:
                unique[video_id] = song

            else:
                unique[video_id]["sources"].extend(song["sources"])

        return list(unique.values())

def calculate_score(song):
    score = 0
    for source in song["sources"]:
        if source == "song":
            score += 100

        elif source == "album":
            score += 90

        elif source == "artist":
            score += 80

        elif source == "watch_graph":
            score += 70

    return score

def sort_results(results):
    for song in results:
        song["score"] = calculate_score(song)

    results.sort(
        key = lambda song: song["score"],
        reverse = True
    )

    return results

def smart_search(query):
    exact = search_exact_songs(query)
    artist = search_artist(query)
    album = search_album(query)

    watch_graph = []
    if exact:
        watch_graph = watch_playlist_graph(
            exact[0]["videoId"]
        )

    combined = remove_duplicates((exact + album + artist + watch_graph ))
    ranked_combined = sort_results(combined)
    return ranked_combined