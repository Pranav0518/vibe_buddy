from sentence_transformer import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("ALL-MiniLM-L6-v2")

embedding_cache = {}
def get_embedding(key: str, text: str):
    if key in embedding_cache:
        return embedding_cache[key]
    
    embedding = model.encode(text)
    embedding_cache[key] = embedding
    return embedding

def get_query_embedding(query:str):
    return model.encode(query)

def calculate_similarity(query_embedding, song_embedding):
    similarity = cosine_similarity(
        [query_embedding],
        [song_embedding]
    )[0][0]

    return float(similarity)

