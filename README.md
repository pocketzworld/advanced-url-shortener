# 🏗️ Pocket Worlds - Backend Assignment

Welcome! This is your starting template for building the distributed URL shortener and leaderboard backend.

## ✅ Goals

- Build a production-adjacent backend service that handles:
  - URL shortening
  - Redirect tracking
  - A leaderboard of top 10 most-visited URLs in the last 24 hours

## 🏃‍♀️ Getting Started

```bash
# Clone and run locally
docker-compose up --build
```

App runs on [http://localhost:8000](http://localhost:8000)

## 🧱 Project Structure

- `app/main.py` — entrypoint with route setup
- `app/shortener.py` — logic for shortening URLs
- `app/storage.py` — abstract interface for persistence
- `app/leaderboard.py` — logic for leaderboard tracking
- `tests/` — unit tests

## ✍️ Assumptions & Architecture

Please fill in this section as part of your submission:
- Assumptions made
- Architecture decisions
- Tradeoffs between consistency/performance
- Fault tolerance considerations
- Scaling plan (for 10M redirects/day)

## ✅ To Do

- [ ] Implement `POST /shorten`
- [ ] Implement `GET /<short_id>`
- [ ] Implement `GET /url-leaderboard`
- [ ] Add tests for core logic
