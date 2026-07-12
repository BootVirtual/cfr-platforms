import requests
from bs4 import BeautifulSoup
import base64
import cv2
import numpy as np
import matplotlib.pyplot as plt

res = requests.get("https://cfr.ro/gari/camereweb/index.php?statie=BucurestiNord")
soup = BeautifulSoup(res.content, "html.parser")
soup = soup.find(id="webcam-img")

img = soup["src"]
img = img.replace("data:image/jpg;base64,", '')
img_data = base64.b64decode(img)

with open("table.png", "wb") as file:
     file.write(img_data)

img = cv2.imread("table.png")

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = img.shape[:2]

arrivals = img[:, :w//2]
departures = img[:, w//2:]

arrivals = arrivals[60:340, :520]
departures = departures[60:330, 40:540]

_, departures = cv2.threshold(
     departures,
     0,
     255,
     cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

projection = np.sum(departures, axis=1)

# DEBUG - to be removed
plt.plot(projection)
plt.show()

FIELDS = [
    "type",
    "number",
    "destination",
    "operator",
    "time",
    "delay",
    "platform"
]

def create_row(row):
    return {
        "row": row,
        "cells": {field: None for field in FIELDS},
        "ocr": {field: None for field in FIELDS}
    }

data = {
    "arrivals": [],
    "departures": []
}

data["departures"].append(create_row(departures[24:41]))
data["departures"].append(create_row(departures[41:57]))
data["departures"].append(create_row(departures[57:74]))
data["departures"].append(create_row(departures[87:103]))
data["departures"].append(create_row(departures[104:120]))
data["departures"].append(create_row(departures[120:137]))
data["departures"].append(create_row(departures[149:166]))
data["departures"].append(create_row(departures[166:183]))
data["departures"].append(create_row(departures[183:200]))
data["departures"].append(create_row(departures[212:228]))
data["departures"].append(create_row(departures[228:245]))
data["departures"].append(create_row(departures[245:261]))

for row in data["departures"]:
    row["cells"]["type"] = row["row"][:, 20:53]
    row["cells"]["number"] = row["row"][:, 53:106]
    row["cells"]["destination"] = row["row"][:, 106:260]
    row["cells"]["operator"] = row["row"][:, 260:377]
    row["cells"]["time"] = row["row"][:, 377:422]
    row["cells"]["delay"] = row["row"][:, 422:462]
    row["cells"]["platform"] = row["row"][:, 462:]


cv2.imwrite("arrivals.png", arrivals)
cv2.imwrite("departures.png", departures)