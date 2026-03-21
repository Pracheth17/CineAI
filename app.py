from fastapi import FastAPI
import pandas as pd
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TMDB_API_KEY = "a7f9a24f11437be406ddaec75b965121"

def get_poster(title):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}"
        data = requests.get(url, timeout=3).json()
        if data.get("results"):
            return data["results"][0].get("poster_path")
        return None
    except:
        return None

df = pd.read_csv("tmdb_5000_movies.csv")[["title","overview"]].dropna()
df["title"] = df["title"].str.lower()
df = df.drop_duplicates(subset="title")
df = df[df["overview"].str.len() > 50].reset_index(drop=True)

model = SentenceTransformer("all-MiniLM-L6-v2")
vectors = model.encode(df["overview"].tolist(), batch_size=64, show_progress_bar=False)

class ChatInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/chat")
def chat(input: ChatInput):
    query = input.text.lower()
    if not query.strip():
        return {"results": []}
    query_vec = model.encode([query])
    scores = cosine_similarity(query_vec, vectors).flatten()
    top_idx = scores.argsort()[-10:][::-1]
    results = []
    for i in top_idx:
        row = df.iloc[i]
        results.append({
            "title": row["title"],
            "poster": get_poster(row["title"]),
            "reason": f"matched with {query}"
        })
    return {"results": results}