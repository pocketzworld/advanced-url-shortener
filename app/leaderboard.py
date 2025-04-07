import redis
import os
from datetime import datetime, timedelta

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

VISIT_WINDOW_SECONDS = 24 * 60 * 60  # 24 hours

def track_visit(short_id: str):
    now = datetime.utcnow().timestamp()
    r.zadd("leaderboard", {short_id: now})
    r.zincrby("leaderboard-counts", 1, short_id)

def get_leaderboard():
    cutoff = datetime.utcnow().timestamp() - VISIT_WINDOW_SECONDS
    r.zremrangebyscore("leaderboard", 0, cutoff)
    top_urls = r.zrevrange("leaderboard-counts", 0, 9, withscores=True)
    return [{"url": url, "visits": int(score)} for url, score in top_urls]
