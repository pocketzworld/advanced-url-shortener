import redis
import os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def store_url(short_id: str, long_url: str):
    r.set(f"url:{short_id}", long_url)

def get_url(short_id: str) -> str:
    return r.get(f"url:{short_id}")
