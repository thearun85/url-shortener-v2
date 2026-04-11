# url-shortener-v2
A URL shortener built with Flask, Postgres and Docker

## Stack
- Python 3.12, Flask, SQLAlchemy
- Postgres (storage), Redis (cache - phase 2)
- Docker + docker-compose for local dev
- Deployed on Fly.io

## Commands

```bash
make run		# start the app with docker-compose
make fmt		# ruff format
make lint		# ruff lint check
make typecheck	# mypy type check
make test		# run the test suite
```
## Setup

```bash
cp .env.example .env
make run
```

## Status
Work in progress.
