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

    cv2.imwrite("arrivals.png", arrivals)
    cv2.imwrite("departures.png", departures)

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

    cv2.imwrite("test.png", data["arrivals"][9]["cells"]["number"])

    return data