from services.embedding_engine import get_embedding

def build_semantic_document(song):
    
    title = song.get("title","")
    artist = song.get("artist","")
    album = song.get("album","")

    semantic_document = f"""
    Title : {title}
    Artist: {artist}
    Album: {album}
    """

    return semantic_document

def build_feature(song):
    semantic_document = build_semantic_document(song)

    embedding = get_embedding(
        key = song["videoId"], 
        text = semantic_document
    )

    feature = {
        "videoId": song["videoId"],
        "title": song["title"],
        "artist": song["artist"],
        "album": song.get("album",""),
        "thumbnail": song["thumbnail"],
        "sources": song["sources"],
        "semantic_document": semantic_document,
        "embedding": embedding
    }

    return feature