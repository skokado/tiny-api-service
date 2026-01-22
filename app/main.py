from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel


class HelloResponse(BaseModel):
    message: Literal["Hello from tiny-api"]


app = FastAPI(title="Tiny API", version="1.0.0")


@app.get("/", response_model=HelloResponse)
async def root():
    return HelloResponse(message="Hello from tiny-api")
