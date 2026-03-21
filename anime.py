import pandas as pd

anime = pd.read_csv("animedata.csv", engine='python')

anime.columns = anime.columns.str.strip().str.lower()

anime = anime.rename(columns={
    "name": "title",
    "sypnopsis": "overview"
})

print(anime.head())