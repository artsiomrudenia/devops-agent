from fastapi import FastAPI

app = FastAPI(title="devops-agent", version="0.1.0")


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok"}


@app.get("/info")
def info() -> dict:
    return {
        "project": "devops-agent",
        "description": "Task-oriented DevOps automation agent",
        "domain": "devops",
    }
