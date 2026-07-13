from cfr_platforms import scraper, ocr
from cfr_platforms.parsers import get_parser
from cachetools import TTLCache, cached

cache = TTLCache(maxsize=32, ttl=60)

@cached(cache)
def get_station_data(station):
    img = scraper.get_station_webcam(station)

    parser = get_parser(station)

    data = parser.parse(img)

    data = ocr.ocr(data)

    return data