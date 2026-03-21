from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "working"}

@app.post("/smart")
def smart():
    return {"message": "smart works"}