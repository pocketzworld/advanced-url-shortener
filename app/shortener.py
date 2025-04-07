import hashlib

def shorten_url(long_url: str) -> str:
    return hashlib.sha256(long_url.encode()).hexdigest()[:6]
