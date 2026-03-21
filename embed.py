from sentence_transformers import SentenceTransformer
from data_loader import movies
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = []
titles = []

for movie in movies[:500]:
    text = movie["title"] + " " + str(movie["overview"])
    vec = model.encode(text)

    embeddings.append(vec)
    titles.append(movie["title"])

embeddings = np.array(embeddings)

print("Embeddings created ✅")