from fastapi import FastAPI, HTTPException
from .shortener import shorten_url
from .storage import store_url, get_url
from .leaderboard import track_visit, get_leaderboard

app = FastAPI()

@app.post("/shorten")
def create_short_url(long_url: str):
    short_id = shorten_url(long_url)
    store_url(short_id, long_url)
    return {"short_url": f"http://localhost:8000/{short_id}"}

@app.get("/{short_id}")
def redirect(short_id: str):
    long_url = get_url(short_id)
    if not long_url:
        raise HTTPException(status_code=404, detail="URL not found")
    track_visit(short_id)
    return {"redirect_to": long_url}

@app.get("/url-leaderboard")
def leaderboard():
    return get_leaderboard()
