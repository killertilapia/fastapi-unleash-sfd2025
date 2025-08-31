from contextlib import asynccontextmanager
from fastapi import FastAPI

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup here - load models, singletons, etc.

    # //end of startup
    yield
    # shutdown here - release locks, del temps, etc.

    # //end of shutdown


@app.get("/ping")
async def pong():
    return {"msg": "pong"}


@app.get("/feature1")
async def feature_available():
    return {"msg": "This feature is available."}


@app.get("/experiment")
async def experiment_feature():
    return {"msg": "This feature is experimental and not generally available"}