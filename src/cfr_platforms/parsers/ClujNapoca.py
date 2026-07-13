import cv2

def parse(img):
    arrivals = img[1]
    departures = img[0]

    arrivals = cv2.cvtColor(arrivals, cv2.COLOR_BGR2GRAY)
    departures = cv2.cvtColor(departures, cv2.COLOR_BGR2GRAY)

    arrivals = cv2.divide(arrivals, cv2.GaussianBlur(arrivals, (51, 51), 0), scale=255)

    #arrivals = cv2.adaptiveThreshold(
    #    arrivals,
    #    255,
    #    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #    cv2.THRESH_BINARY,
    #    31,
    #    11
    #)

    _, arrivals = cv2.threshold(
        arrivals,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    cv2.imwrite("arrivals.png", arrivals)
    cv2.imwrite("departures.png", departures)

    exit()