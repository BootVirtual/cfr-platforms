import requests
from bs4 import BeautifulSoup
import base64
import cv2

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

cv2.imwrite("arrivals.png", arrivals)
cv2.imwrite("departures.png", departures)