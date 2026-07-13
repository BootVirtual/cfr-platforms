import asyncio
from cfr_platforms.logic import get_station_data
from cfr_platforms.cache import latest

async def worker(station):
    while True:
        latest[station] = await asyncio.to_thread(get_station_data, station)
        await asyncio.sleep(60)