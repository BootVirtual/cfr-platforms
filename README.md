# cfr-platforms

Web scraper and parser for CFR (romanian railways) platform and delay information.

## Motivation

Digitalisation is hard. The CFR offer no realtime information for train departures, but instead offer [webcams pointed to the departures board](https://cfr.ro/gari/camereweb/index.php?statie=BucurestiNord) of a couple of railway stations. This project aims to convert the images provided by the respective webcams into something more usable online.

The first station to be implemented is Bucharest North, as that's Romania's biggest/busiest station.
Also implemented is Cluj Napoca (although it is quite inaccurate. who would've though that tesseract ocr doesn't particularly like webcam images pointed at split flap displays??)

## Note

While this script will return something, there is absolutely no guarantee that it is accurate (it's OCR based after all...)
The script is provided as-is, I assume no responsability for the accuracy of this script.

While the script/API will always fetch the latest departure board, text might not get recognised properly all of the time. This is due to a mixture of the OCR software and the (somewhat bad) quality image CFR provides (thinking about it, quality also probably varies by time of day, as that affects lighting conditions of the physical board. If CFR would actually publish their data in a proper way, we wouldn't be in this rabbithole right now).

There is a fuzzy matching mechanism implemented for train classes, operators and stations. The stations list might not be (is definitely not) complete. I'll have to add upon it as time passes, but it should right now already catch a lot of the most common mistakes/inaccuracies.

## Usage

### CLI

I used poetry for dependency management. After cloning the repo make sure you run:

`poetry install`

You might also need to install the Tesseract OCR binaries for your system. Refer to their [docs](https://tesseract-ocr.github.io/tessdoc/Installation.html) for how to do that.

To run the script, run the module using poetry:

`poetry run python -m cfr_platforms.main <STATION>`

Where `<STATION>` is either `BucurestiNord` or `ClujNapoca`.

This will return the current arrivals and departures tables at the desired station in the CLI.

The output should resemble the following:

```text
ARRIVALS:
+-------+---------+-------------------+----------------+-------+--------------+----------+
| Train |   No.   |        From       |    Operator    |  Time | Delay (min.) | Platform |
+-------+---------+-------------------+----------------+-------+--------------+----------+
|   R   |  129073 |      CRAIOVA      |  CFR Călători  |  9:34 |      89      |    3     |
|   R   |  10262  |     TARSOVIŞTE    | Transferoviar  | 19:27 |      25      |    4     |
|   RE  |   3910  |      CRAIOVA      |  CFR Călători  | 10:39 |      25      |    1     |
|  IRN  |   473   |  BUDAPESTA KELETI |  CFR Călători  | 10:37 |      20      |    14    |
|   RE  |  11066  |       ADJUD       | Regio Călători | 10:52 |      15      |          |
|   RM  |   7922  | AEROPORT H COANDA |  CFR Călători  | 10:37 |              |          |
|   RE  | 4100671 |    PLOIEȘTI SUD   | Transferoviar  | 41:03 |      15      |          |
|   IR  |  10072  |       GALAŢI      | Triaiwiaroviar | 11:10 |      15      |          |
|   CC  |   582   |     CONSTANȚA     |  CFR Călători  | 11:27 |              |          |
|   IR  |   1826  |      TARGU Ji     |  GR Căâlatari  | 14:28 |              |          |
|   RE  |  44032  |       BRAȘOV      | Regio Călători | 11:34 |      13      |          |
|   RE  |  40142  | AEROPORT H COANDA | Transferoviar  |   47  |              |          |
+-------+---------+-------------------+----------------+-------+--------------+----------+
DEPARTURES:
+-------+-------+-------------------+---------------+-------+--------------+----------+
| Train |  No.  |    Destination    |    Operator   |  Time | Delay (min.) | Platform |
+-------+-------+-------------------+---------------+-------+--------------+----------+
|   R   | 10283 |     TÂRGOVIȘTE    | Transferoviar | 10:45 |      10      |    4     |
|       |  1553 |      SUCEAVA      |  CFR Călători | 11:10 |              |    6     |
|   RM  |  7921 | AEROPORT H COANDA |  CFR Călători | 11:10 |              |          |
|   IR  | 16021 |   TIMIȘOARA NORD  |  CFR Călători | 11:20 |              |          |
|   RE  |  9208 |      PITEȘTI      |  CFR Călători | 11:25 |              |          |
|   IR  | 16085 |     CONSTANȚA     |  CFR Călători | 11:30 |              |          |
|   RE  | 40113 | AEROPORT H COANDA | Transferoviar | 11:50 |              |          |
|   IR  |  466  |        AŞ:        |  CFR Călători | 11:38 |              |          |
|   IR  | 18568 |       RRASOV      | InterRegional | 12:00 |              |          |
|   RE  | 10052 |       BUZĂU       | Transferoviar | 12:12 |              |          |
|   IC  |  534  |    CLUJ NAPOCA    |  CFR Călători | 12:21 |              |          |
|   CI  | 23293 | AEROPORT H COANDA |  CFR Călători |  1:30 |              |          |
+-------+-------+-------------------+---------------+-------+--------------+----------+
```

### API

The API was built using FastAPI. Available endpoints are `/stations` to list supported stations, `/stations/<STATION>` to fetch arrivals and departures for a particular station and `/health` for a basic health check of the service. More in-depth docs are available at `/docs`.

Deploying can be done via the included Dockerfile (don't forget to edit your host/port bindings!)

To run the API I've used `uvicorn` (`poetry run uvicorn cfr_platforms.api:app`).

I have tried hosting the API with a free provider, but the OCR would consistently time out/exhaust the available resources (who would've though OCR is no easy task?)

## Roadmap(-ish)

I should probably expand a little more upon this project. Cool things would be (in no particular order):

- ~~some sort of an API or something to be able to interface with the script~~ done
- more stations
- ~~station fuzzy matching (although I would need a proper list of stations for that)~~ done, kind of
- ???

## Endnote

A demo of this CLI tool and API as well as the iOS client I've build can be found at https://youtu.be/gvR8AaXw0cc.

This project is being developed as a submission to [HackClub](https://hackclub.com/). It is still very much a WIP.
