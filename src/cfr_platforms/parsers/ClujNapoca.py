import cv2
import numpy as np

def parse(img):
    arrivals = img[1]
    departures = img[0]

    arrivals = cv2.cvtColor(arrivals, cv2.COLOR_BGR2GRAY)
    departures = cv2.cvtColor(departures, cv2.COLOR_BGR2GRAY)

    arrivals = cv2.GaussianBlur(arrivals, (3, 3), 0)
    departures = cv2.GaussianBlur(departures, (3, 3), 0)

    arrivals_source = np.float32([
        [96, 138],
        [985, 150],
        [990, 518],
        [97, 523]
    ])

    w = 880
    h = 380

    arrivals_dest = np.float32([
        [0, 0],
        [w, 0],
        [w, h],
        [0, h]
    ])

    arrivals = cv2.warpPerspective(arrivals, cv2.getPerspectiveTransform(arrivals_source, arrivals_dest), (w, h))

    departures_source = np.float32([
        [116, 121],
        [1010, 127],
        [1004, 512],
        [99, 490]
    ])

    w = 920
    h = 400

    departures_dest = np.float32([
        [0, 0],
        [w, 0],
        [w, h],
        [0, h]
    ])

    departures = cv2.warpPerspective(departures, cv2.getPerspectiveTransform(departures_source, departures_dest), (w, h))

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

    data["arrivals"].append(create_row(arrivals[0:41]))
    data["arrivals"].append(create_row(arrivals[41:76]))
    data["arrivals"].append(create_row(arrivals[76:116]))
    data["arrivals"].append(create_row(arrivals[116:152]))
    data["arrivals"].append(create_row(arrivals[152:190]))
    data["arrivals"].append(create_row(arrivals[190:228]))
    data["arrivals"].append(create_row(arrivals[228:265]))
    data["arrivals"].append(create_row(arrivals[265:303]))
    data["arrivals"].append(create_row(arrivals[303:341]))
    data["arrivals"].append(create_row(arrivals[341:379]))

    for row in data["arrivals"]:
        row["cells"]["type"] = row["row"][:, :90]
        row["cells"]["number"] = row["row"][:, 90:214]
        row["cells"]["destination"] = row["row"][:, 214:404]
        row["cells"]["operator"] = row["row"][:, 404:595]
        row["cells"]["time"] = row["row"][:, 595:717]
        row["cells"]["delay"] = row["row"][:, 717:817]
        row["cells"]["platform"] = row["row"][:, 817:]

    data["departures"].append(create_row(departures[0:41]))
    data["departures"].append(create_row(departures[41:81]))
    data["departures"].append(create_row(departures[81:122]))
    data["departures"].append(create_row(departures[122:160]))
    data["departures"].append(create_row(departures[160:200]))
    data["departures"].append(create_row(departures[200:241]))
    data["departures"].append(create_row(departures[241:280]))
    data["departures"].append(create_row(departures[280:320]))
    data["departures"].append(create_row(departures[320:358]))
    data["departures"].append(create_row(departures[358:399]))

    for row in data["departures"]:
        row["cells"]["type"] = row["row"][:, :94]
        row["cells"]["number"] = row["row"][:, 94:219]
        row["cells"]["destination"] = row["row"][:, 219:422]
        row["cells"]["operator"] = row["row"][:, 422:626]
        row["cells"]["time"] = row["row"][:, 626:747]
        row["cells"]["delay"] = row["row"][:, 747:859]
        row["cells"]["platform"] = row["row"][:, 859:]

    return data