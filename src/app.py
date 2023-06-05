from fastapi import FastAPI

from src.apps.properties.controller import router as PropertiesRouter

app = FastAPI()
app.include_router(PropertiesRouter)


@app.get("/")
def hellow_world():
    return {"data": "hellow world"}
