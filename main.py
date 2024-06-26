from typing import Union

from fastapi import FastAPI

from Routers.router import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

