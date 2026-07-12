from cfr_platforms import scraper
from cfr_platforms.parsers import BucurestiNord
from cfr_platforms import ocr
from prettytable import PrettyTable

img = scraper.get_station_webcam("BucurestiNord")

data = BucurestiNord.parse(img)

data = ocr.ocr(data)

arrivals_table = PrettyTable()

arrivals_table.field_names = ["Train", "No.", "From", "Operator", "Time", "Delay (min.)", "Platform"]
for row in data["arrivals"]:
    arrivals_table.add_row([row["ocr"]["type"], row["ocr"]["number"], row["ocr"]["destination"], row["ocr"]["operator"], row["ocr"]["time"], row["ocr"]["delay"], row["ocr"]["platform"]])

print("ARRIVALS:")
print(arrivals_table)


departures_table = PrettyTable()

departures_table.field_names = ["Train", "No.", "Destination", "Operator", "Time", "Delay (min.)", "Platform"]
for row in data["departures"]:
    departures_table.add_row([row["ocr"]["type"], row["ocr"]["number"], row["ocr"]["destination"], row["ocr"]["operator"], row["ocr"]["time"], row["ocr"]["delay"], row["ocr"]["platform"]])

print("DEPARTURES:")
print(departures_table)