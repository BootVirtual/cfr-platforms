import cv2

def parse(img):
    img = img[0]

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    h, w = img.shape[:2]

    arrivals = img[:, :w//2]
    departures = img[:, w//2:]

    arrivals = arrivals[60:340, :520]
    departures = departures[60:330, 40:540]

    _, arrivals = cv2.threshold(
        arrivals,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    _, departures = cv2.threshold(
        departures,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

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

    data["arrivals"].append(create_row(arrivals[26:44]))
    data["arrivals"].append(create_row(arrivals[44:61]))
    data["arrivals"].append(create_row(arrivals[61:78]))
    data["arrivals"].append(create_row(arrivals[90:107]))
    data["arrivals"].append(create_row(arrivals[107:124]))
    data["arrivals"].append(create_row(arrivals[124:141]))
    data["arrivals"].append(create_row(arrivals[151:170]))
    data["arrivals"].append(create_row(arrivals[170:187]))
    data["arrivals"].append(create_row(arrivals[187:204]))
    data["arrivals"].append(create_row(arrivals[216:232]))
    data["arrivals"].append(create_row(arrivals[232:249]))
    data["arrivals"].append(create_row(arrivals[249:266]))

    for row in data["arrivals"]:
        row["cells"]["type"] = row["row"][:, 23:58]
        row["cells"]["number"] = row["row"][:, 58:109]
        row["cells"]["destination"] = row["row"][:, 109:264]
        row["cells"]["operator"] = row["row"][:, 264:386]
        row["cells"]["time"] = row["row"][:, 386:433]
        row["cells"]["delay"] = row["row"][:, 433:473]
        row["cells"]["platform"] = row["row"][:, 473:]

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
        row["cells"]["destination"] = row["row"][:, 106:258]
        row["cells"]["operator"] = row["row"][:, 258:375]
        row["cells"]["time"] = row["row"][:, 375:422]
        row["cells"]["delay"] = row["row"][:, 422:462]
        row["cells"]["platform"] = row["row"][:, 462:]

    return data