from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from embed import embeddings, titles

model = SentenceTransformer('all-MiniLM-L6-v2')

def recommend_movies(query):
    query_vec = model.encode(query)

    scores = cosine_similarity([query_vec], embeddings)[0]

    top_indices = scores.argsort()[-5:][::-1]

    results = []

    for i in top_indices:
        results.append({
            "name": titles[i],
            "score": float(scores[i])
        })

    return results