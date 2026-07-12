from fastapi import FastAPI
from cfr_platforms.logic import get_station_data

app = FastAPI(
    title = "CFR Departures/Arrivals API",
    version = "0.1"
)

@app.get("/stations/{station}")
def station(station):
    return get_station_data(station)

@app.get("/health")
def health():
    return {"status": "ok"}