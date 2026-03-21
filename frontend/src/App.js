import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [chatInput, setChatInput] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [liked, setLiked] = useState([]);
  const [watchlist, setWatchlist] = useState([]);

  useEffect(() => {
    setLiked(JSON.parse(localStorage.getItem("liked")) || []);
    setWatchlist(JSON.parse(localStorage.getItem("watchlist")) || []);
  }, []);

  const saveLiked = (data) => {
    localStorage.setItem("liked", JSON.stringify(data));
    setLiked(data);
  };

  const saveWatchlist = (data) => {
    localStorage.setItem("watchlist", JSON.stringify(data));
    setWatchlist(data);
  };

  const likeMovie = (title) => {
    if (!liked.includes(title)) saveLiked([...liked, title]);
  };

  const addWatchlist = (title) => {
    if (!watchlist.includes(title)) saveWatchlist([...watchlist, title]);
  };

  const chatRecommend = async () => {
    if (!chatInput.trim()) return;

    setLoading(true);
    setResults([]);

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: chatInput }),
      });

      const data = await res.json();
      setResults(data.results || []);
    } catch (err) {
      alert("Backend not responding");
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <div className="hero">
        <h1>CineAI</h1>
        <p>AI-powered movie & anime recommendations</p>
      </div>

      <div className="chat-container">
        <input
          type="text"
          placeholder="Try: dark anime, action movies, emotional drama..."
          value={chatInput}
          onChange={(e) => setChatInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && chatRecommend()}
        />
        <button onClick={chatRecommend}>Search</button>
      </div>

      {loading && <div className="loader"></div>}

      {!loading && results.length === 0 && chatInput && (
        <p className="empty">No results found</p>
      )}

      <div className="grid">
        {results.map((item, index) => (
          <div key={index} className="card">
            {item.poster ? (
              <img
                src={`https://image.tmdb.org/t/p/w300${item.poster}`}
                alt={item.title}
              />
            ) : (
              <div className="no-image">No Image</div>
            )}

            <div className="card-content">
              <h3>{item.title}</h3>
              <p className="reason">{item.reason}</p>

              <div className="actions">
                <button onClick={() => likeMovie(item.title)}>
                  ❤️ {liked.includes(item.title) && "Liked"}
                </button>
                <button onClick={() => addWatchlist(item.title)}>
                  ⭐ {watchlist.includes(item.title) && "Added"}
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;