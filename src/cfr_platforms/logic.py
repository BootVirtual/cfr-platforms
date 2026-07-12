from cfr_platforms import scraper, ocr
from cfr_platforms.parsers import BucurestiNord

def get_station_data(station):
    img = scraper.get_station_webcam("BucurestiNord")

    data = BucurestiNord.parse(img)

    data = ocr.ocr(data)

    return data