from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from UnleashClient import UnleashClient
from pydantic_settings import BaseSettings


unleash_client = UnleashClient(
    url="http://localhost:4242/api/",
    app_name="unleash-onboarding-python",
    custom_headers={'Authorization': 'default:development.unleash-insecure-api-token'}) 

class AppSettings(BaseSettings):
    """
    This is how FastAPI handles external settings; We'll also use it for
    creating an Unleash context

    Context can be obtain via a file(JSON), Database or other ways
    """
    userId: str = "jginete@innovuze.com"
    #userId: str = "no_chance@gmail.com"
    otherFields: str = "some-value"

app_context = AppSettings().model_dump() # dump obj to dict

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup here - load models, singletons, etc.    
    unleash_client.initialize_client()
    
    # Test Unleash Client is connected and working
    print(f"Feature flags working - {unleash_client.is_enabled('experiment-1')}")
    
    # //end of startup

    yield   # App starts serving requests

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
    if(unleash_client.is_enabled('experiment-1', context=app_context)):
        return {"msg": "This feature is experimental and not generally available"}
    else:
        raise HTTPException(status_code=404, detail="Resource not found!")
    
@app.get("/prod-feature")
async def prod_feature_only():
    if(unleash_client.is_enabled('prod-feature-1', context=app_context)):
        return {"msg": "This Production Feature is available!"}
    else:
        raise HTTPException(status_code=403, detail="ACCESS DENIED. Naughty naughty!")
