import requests
from bs4 import BeautifulSoup
import base64
import cv2
import numpy as np

def get_station_webcam(station):
    res = requests.get(f"https://cfr.ro/gari/camereweb/index.php?statie={station}")

    soup = BeautifulSoup(res.content, "html.parser")
    soup = soup.find_all(id="webcam-img")
    
    images = []

    for element in soup:
        img = element["src"]
        img = img.replace("data:image/jpg;base64,", '')
        img_data = base64.b64decode(img)

        img = cv2.imdecode(np.frombuffer(img_data, np.uint8), cv2.IMREAD_COLOR)

        images.append(img)

    return images