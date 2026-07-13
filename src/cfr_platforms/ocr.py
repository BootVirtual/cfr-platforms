import pytesseract
from rapidfuzz import process, fuzz

general_config = (
    "--psm 7 "
)

time_config = (
    "--psm 7 "
    "-c tessedit_char_whitelist=1234567890:"
)

number_config = (
    "--psm 7 "
    "-c tessedit_char_whitelist=1234567890"
)

platform_config = (
    "--psm 7 "
    "-c tessedit_char_whitelist=1234567890A"
)

class_config = (
    "--psm 7 "
    "-c tessedit_char_whitelist=IRMCNE"
)

operators = [
    "CFR Călători",
    "Regio Călători",
    "Transferoviar",
    "InterRegional",
    "Astra Trans Carpatic",
    "Softrans Călători"
]

train_classes = [
    "R",
    "RE",
    "RM",
    "IR",
    "IRN",
    "IC"
]

stations = [
    "ADJUD",
    "AEROPORT H COANDĂ",
    "ARAD",
    "BAIA MARE",
    "BISTRIȚA N.",
    "BONTIDA",
    "BRAȘOV",
    "BUCUREȘTI N.",
    "BUCUREȘTI OBOR",
    "BUDAPESTA KELETI",
    "BUZĂU",
    "CÂMPIA TURZII",
    "CLUJ NAPOCA",
    "CONSTANȚA",
    "CRAIOVA",
    "CURTICI",
    "DEJ",
    "DEVA",
    "FETEȘTI",
    "GALAȚI",
    "IAȘI",
    "MANGALIA",
    "PITEȘTI",
    "PLOIEȘTI SUD",
    "ROȘIORI NORD",
    "RUSE",
    "SIBIU",
    "SIMERIA",
    "SLOBOZIA VECHE",
    "SUCEAVA",
    "SUCEAVA NORD",
    "TIMIȘOARA NORD",
    "TÂRGOVIȘTE",
    "TÂRGU JIU",
    "TEIUȘ",
    "TG. MUREȘ",
    "URZICENI",
    "VIENA"
]

def ocr(data):
    def fuzzy_match(value, list, threshold):
        result = process.extractOne(value, list, scorer=fuzz.WRatio)
        match, score, _ = result
        if score >= threshold:
            return match
        return value

    for board_name, rows in data.items():
        for row in rows:
            row["ocr"]["type"] = pytesseract.image_to_string(row["cells"]["type"], config=class_config, lang="ron").strip()
            row["ocr"]["type"] = fuzzy_match(row["ocr"]["type"], train_classes, 90)
            row["ocr"]["number"] = pytesseract.image_to_string(row["cells"]["number"], config=number_config, lang="ron").strip()
            row["ocr"]["destination"] = pytesseract.image_to_string(row["cells"]["destination"], config=general_config, lang="ron").strip().upper()
            row["ocr"]["destination"] = fuzzy_match(row["ocr"]["destination"], stations, 80)
            row["ocr"]["operator"] = pytesseract.image_to_string(row["cells"]["operator"], config=general_config, lang="ron").strip()
            row["ocr"]["operator"] = fuzzy_match(row["ocr"]["operator"], operators, 75)
            row["ocr"]["time"] = pytesseract.image_to_string(row["cells"]["time"], config=time_config, lang="ron").strip()
            row["ocr"]["delay"] = pytesseract.image_to_string(row["cells"]["delay"], config=number_config, lang="ron").strip()
            row["ocr"]["platform"] = pytesseract.image_to_string(row["cells"]["platform"], config=platform_config, lang="ron").strip()

    return {
        board: [
            row["ocr"]
            for row in rows
        ]
        for board, rows in data.items()
    }