from fastapi import FastAPI, HTTPException
import asyncio
from contextlib import asynccontextmanager
from cfr_platforms.worker import worker
from cfr_platforms.cache import latest
from pydantic import BaseModel, Field

class Station(BaseModel):
    id: str = Field(example="BucurestiNord")
    name: str = Field(example="București Nord")

class Train(BaseModel):
    type: str = Field(example="IR")
    number: str = Field(example="1234")
    destination: str = Field(example="Craiova")
    operator: str = Field(example="Transferoviar")
    time: str = Field(example="07:23")
    delay: str = Field(example="15")
    platform: str = Field(example="12")

class StationData(BaseModel):
    arrivals: list[Train]
    departures: list[Train]

STATIONS = {
    "BucurestiNord": {
        "name": "București Nord"
    },
    "ClujNapoca": {
        "name": "Cluj-Napoca"
    },
}

@asynccontextmanager
async def lifespan(app: FastAPI):
    tasks = [
        asyncio.create_task(worker(station_id))
        for station_id in STATIONS
    ]
    yield
    for task in tasks:
        task.cancel()

app = FastAPI(
    title = "CFR Departures/Arrivals API",
    version = "0.1",
    lifespan=lifespan,
    description="""
Realtime departures and arrivals from CFR stations.

Data is extracted using OCR from the webcams provided by CFR, it may (will) contain inacuracies.
""",
    contact={
        "name": "marctg",
        "url": "https://github.com/BootVirtual/cfr-platforms"
    }
)

@app.get(
    "/stations/{station}",
    summary="Fetch arrivals and departures",
    description="Returns the latest arrivals and departures for a station.",
    response_model=StationData,
    responses={
        404: {
            "description": "Unsupported station" 
        },
        503: {
            "description:": "Station data not yet available."
        }
    },
    tags=["Stations"]
)
def station(station):
    if station not in STATIONS:
        raise HTTPException(
            status_code=404,
            detail="Unsupported station"
        )
    
    if station not in latest:
        raise HTTPException(
            status_code=503,
            detail="Station data not yet available."
        )
    
    return latest[station]

@app.get(
    "/stations",
    summary="List all supported stations",
    description="Returns a list of all stations currently supported by the API and their coresponding IDs.",
    response_model=list[Station],
    tags=["Stations"]
)
def stations():
    return [
        {
            "id": station_id,
            **content,
        }
        for station_id, content in STATIONS.items()
    ]

@app.get(
    "/health",
    summary="Health check",
    description="Returns the status of the API.",
    tags=["Health"]
)
def health():
    return {"status": "ok"}