from fastapi import FastAPI
import asyncio
from contextlib import asynccontextmanager
from cfr_platforms.worker import worker
from cfr_platforms.cache import latest

stations = [
    "BucurestiNord",
    "ClujNapoca"
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    tasks = [
        asyncio.create_task(worker(station))
        for station in stations
    ]
    yield
    for task in tasks:
        task.cancel()

app = FastAPI(
    title = "CFR Departures/Arrivals API",
    version = "0.1",
    lifespan=lifespan
)

@app.get("/stations/{station}")
def station(station):
    return latest[station]

@app.get("/health")
def health():
    return {"status": "ok"}