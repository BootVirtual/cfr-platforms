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

def ocr(data):
    def fuzzy_match(value, list, threshold):
        result = process.extractOne(value, list, scorer=fuzz.WRatio)
        match, score, _ = result
        if score >= threshold:
            return match
        return value

    for board_name, rows in data.items():
        for row in rows:
            row["ocr"]["type"] = pytesseract.image_to_string(row["cells"]["type"], config=general_config, lang="ron").strip()
            row["ocr"]["type"] = fuzzy_match(row["ocr"]["type"], train_classes, 90)
            row["ocr"]["number"] = pytesseract.image_to_string(row["cells"]["number"], config=number_config, lang="ron").strip()
            row["ocr"]["destination"] = pytesseract.image_to_string(row["cells"]["destination"], config=general_config, lang="ron").strip()
            row["ocr"]["operator"] = pytesseract.image_to_string(row["cells"]["operator"], config=general_config, lang="ron").strip()
            row["ocr"]["operator"] = fuzzy_match(row["ocr"]["operator"], operators, 75)
            row["ocr"]["time"] = pytesseract.image_to_string(row["cells"]["time"], config=time_config, lang="ron").strip()
            row["ocr"]["delay"] = pytesseract.image_to_string(row["cells"]["delay"], config=number_config, lang="ron").strip()
            row["ocr"]["platform"] = pytesseract.image_to_string(row["cells"]["platform"], config=number_config, lang="ron").strip()

    return data