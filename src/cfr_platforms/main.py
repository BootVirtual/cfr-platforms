import requests
from bs4 import BeautifulSoup
import base64


res = requests.get("https://cfr.ro/gari/camereweb/index.php?statie=BucurestiNord")

soup = BeautifulSoup(res.content, "html.parser")

soup = soup.find(id="webcam-img")

img = soup["src"]

img = img.replace("data:image/jpg;base64,", '')

imgdata = base64.b64decode(img)

with open("table.png", "wb") as file:
    file.write(imgdata)


