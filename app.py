from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from main import run_pipeline

app = FastAPI(title="DraftPilot", version="1.0.0")


class DraftRequest(BaseModel):
    intent: str
    context: str | None = None


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/draft")
def draft(req: DraftRequest):
    return run_pipeline(intent=req.intent, context=req.context)
