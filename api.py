import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from UnleashClient import UnleashClient

#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)

unleash_client = UnleashClient(
    url="http://localhost:4242/api/",
    app_name="unleash-onboarding-python",
    custom_headers={'Authorization': 'default:development.unleash-insecure-api-token'}) 


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup here - load models, singletons, etc.    
    unleash_client.initialize_client()
    
    # Test Unleash Client is connected and working
    print(f"Feature flags working - {unleash_client.is_enabled('experiment-1')}")
    # //end of startup

    yield
    
    # shutdown here - release locks, del temps, etc.
    unleash_client.destroy()
    # //end of shutdown


app = FastAPI(lifespan=lifespan)


@app.get("/ping")
async def pong():
    return {"msg": "pong"}


@app.get("/feature1")
async def feature_available():
    return {"msg": "This feature is available."}


@app.get("/experiment")
async def experiment_feature():
    if(unleash_client.is_enabled('experiment-1')):
        return {"msg": "This feature is experimental and not generally available"}
    else:
        raise HTTPException(status_code=404, detail="Resource not found!")