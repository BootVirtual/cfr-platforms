# cfr-platforms

Web scraper and parser for CFR (romanian railways) platform and delay information.

## Motivation

Digitalisation is hard. The CFR offer no realtime information for train departures, but instead offer [webcams pointed to the departures board](https://cfr.ro/gari/camereweb/index.php?statie=BucurestiNord) of a couple of railway stations. This project aims to convert the images provided by the respective webcams into something more usable online.

The first station to be implemented is Bucharest North, as that's Romania's biggest/busiest station.

## Note

While this script will return something, there is absolutely no guarantee that it is accurate (it's OCR based after all...)
The script is provided as-is, I assume no responsability for the accuracy of this script.

## Usage

I used poetry for dependency management. After cloning the repo make sure you run:

`poetry install`

You might also need to install the Tesseract OCR binaries for your system. Refer to their [docs](https://tesseract-ocr.github.io/tessdoc/Installation.html) for how to do that.

To run the script, run the module using poetry:

`poetry run python -m cfr_platforms.main`

This will return the current arrivals and departures tables at Bucharest North in the CLI.

The output should resemble the following (as you can maybe see, text might not get recognised properly all of the time. This is due to a mixture of the OCR software and the (somewhat bad) quality image CFR provides (thinking about it, quality also probably varies by time of day, as that affects lighting conditions of the physical board. if CFR would actually publish their data in a proper way, we wouldn't be in this rabbithole right now)):

```text
ARRIVALS:
+-------+--------+--------------------+----------------------+-------+--------------+----------+
| Train |  No.   |        From        |       Operator       |  Time | Delay (min.) | Platform |
+-------+--------+--------------------+----------------------+-------+--------------+----------+
|   R   | 16594  |      BRAŞOYv       |    InterRegional     | 18:42 |     300      |          |
|   R   | 11536  |       BRAȘOV       | Astra Trans Carpatic | 19:43 |     200      |          |
|   R   |  1838  |       BRASOV       |     CFR Călători     | 20:04 |     145      |          |
|   R   | 41538  |       BRASOV       | Astra Trans Carpatic | 21:04 |     200      |          |
|   IR  | 18023  |   TIMISOARA NORD   |     CFR Călători     | 21:11 |      8       |          |
|   IR  | 15574  |       BRAȘOV       |    InterRegional     | 21:31 |     160      |          |
|       |  4382  |     CONSTANŢA      |     CFR Călători     | 21:23 |      69      |          |
|   IR  | 10084  |      MANGALIA      |    Transferoviar     | 22:00 |      40      |          |
|   R   | 41836  |    CLUJ NAPOCA     |     CFR Călători     | 22:04 |      30      |          |
|   RE  | 10120  | AEROPORI îi COANDA |    Transferoviar     | 22:17 |              |    10    |
|   RE  | 410588 |       ADJUD        |    Regio Călători    | 22:31 |      25      |          |
|   IR  |  1522  |       SIBIU        |     CFR Călători     | 22:35 |      85      |          |
+-------+--------+--------------------+----------------------+-------+--------------+----------+
DEPARTURES:
+-------+--------+-------------------+----------------+-------+--------------+----------+
| Train |  No.   |    Destination    |    Operator    |  Time | Delay (min.) | Platform |
+-------+--------+-------------------+----------------+-------+--------------+----------+
|   IR  |  4389  |     CONSTANŢA     |  CFR Călători  | 20:33 |     120      |          |
|   R   | 16577  |      BRASOYV      | InterRegional  | 21:50 |     120      |          |
|   R   | 16537  |    CLUJ NAPOCA    | InterRegional  | 22:00 |      60      |          |
|   R   |  1653  |  VATRA DORNEI BAI |  CFR Călători  | 22:20 |              |    9     |
|   R   |  5935  |   PLOIESTI! SUD   |  CFR Călători  |  :27  |              |          |
|   RE  | 40423  | AEROPORT H COANDĂ | Transferoviar  | 22:30 |              |    10    |
|  IRN  |  4569  |        IASI       |  CFR Călători  | 22:38 |              |          |
|   RE  | 410693 |       ADJUD       | Regio Călători | 23:01 |              |          |
|   RM  |  7345  | AEROPORT H COANDĂ |  CFR Călători  | 23:10 |              |          |
|   IR  |  4914  |       SIBIU       |  CFR Călători  | 23:14 |              |          |
|   RM  |  7947  | AEROPORT H COANDĂ |  CFR Călători  | 23:30 |              |          |
|   RM  |  7904  | AEROPORT H COANDĂ |  CFR Călători  |  0:30 |              |          |
+-------+--------+-------------------+----------------+-------+--------------+----------+
```

## Roadmap(-ish)

I should probably expand a little more upon this project. Cool things would be (in no particular order):

- some sort of an API or something to be able to interface with the script
- more stations
- station fuzzy matching (although I would need a proper list of stations for that)
- ???

## Endnote

This project is being developed as a submission to [HackClub](https://hackclub.com/). It is still very much a WIP.
