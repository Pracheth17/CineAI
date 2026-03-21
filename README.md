CineAI – AI Movie & Anime Recommender

An AI-powered recommendation system that understands natural language queries like:

"dark anime like Attack on Titan"
"feel-good movies for a weekend"

and returns highly relevant suggestions using semantic similarity instead of traditional filters.


Features

Natural language search without filters
AI-based semantic recommendations
Supports both movies and anime
Fast backend using FastAPI
Clean and responsive UI built with React

How it works

User enters a natural language query
Query is converted into an embedding using Sentence Transformers (MiniLM)
Movie and anime descriptions are pre-encoded into vector embeddings
Cosine similarity is used to find the closest matches
Top results are returned and displayed with posters via TMDB API
Tech Stack

Frontend

React.js
HTML, CSS

Backend

FastAPI (Python)

AI / ML

Sentence Transformers (MiniLM)
Hugging Face
Scikit-learn

Data

Pandas
TMDB API

Deployment

Render
Project Structure

Cine/
│── frontend/
│── app.py
│── requirements.txt
│── render.yaml
│── runtime.txt
│── dataset files

Running locally

Clone the repository:

git clone https://github.com/Pracheth17/CineAI.git
cd CineAI

Run backend:

pip install -r requirements.txt
uvicorn app --reload

Run frontend:

cd frontend
npm install
npm start

API

POST /chat

Example input:

{ "text": "emotional anime or sad movies" }

Why I built this

Unlike traditional recommendation systems that rely on filters or predefined categories, this application allows users to describe what they want in plain English, making the experience more intuitive and user-friendly.

Future improvements

Improve UI and user experience
Add a dedicated anime dataset
Add user accounts and personalization
Save watch history and favorites
Improve poster availability

Key Learnings

Applied NLP embeddings in a real-world application
Built an end-to-end AI system from model to deployment
Improved understanding of vector search and similarity algorithms
Author

Pracheth Pasala

GitHub: https://github.com/Pracheth17
LinkedIn:www.linkedin.com/in/pracheth-pasala-b0419432b
