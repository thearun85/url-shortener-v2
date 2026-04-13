[![CI](https://github.com/thearun85/url-shortener-v2/actions/workflows/ci.yml/badge.svg)](https://github.com/thearun85/url-shortener-v2/actions/workflows/ci.yml)

# url-shortener-v2

A URL shortener built with Flask, Postgres and Docker.

## Live API

Base URL: `https://url-shortener-v2-mihl.onrender.com`

### Shorten a URL
```bash
curl -X POST https://url-shortener-v2-mihl.onrender.com/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com"}'
```

### Redirect
```bash
curl -L https://url-shortener-v2-mihl.onrender.com/
```

### Health check
```bash
curl https://url-shortener-v2-mihl.onrender.com/health
```

## Stack
- Python 3.12, Flask, SQLAlchemy
- Postgres (storage), Redis (cache - phase 2)
- Docker + docker-compose for local dev
- Deployed on Render

## Local setup
```bash
cp .env.example .env
make run
```

## Commands
```bash
make run        # start the app with docker-compose
make test       # run the test suite
make lint       # ruff lint check
make typecheck  # mypy type check
make create-db  # create database tables
```
