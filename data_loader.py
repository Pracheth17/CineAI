import pandas as pd

print("Loading data...")

# Just use ONE dataset for now
df = pd.read_csv("tmdb_5000_movies.csv")

df = df[["title", "overview"]]
df = df.dropna()

print("Done!")
print(df.head())

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Creating model...")

tfidf = TfidfVectorizer(stop_words='english')
vectors = tfidf.fit_transform(df['overview'])

similarity = cosine_similarity(vectors)

print("Model ready!")

def recommend(title):
    idx = df[df['title'] == title].index[0]
    distances = similarity[idx]

    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    return [df.iloc[i[0]].title for i in movies_list]

print(recommend("Avatar"))