import spacy
from app.utils.regex_patterns import PHONE_PATTERN, EMAIL_PATTERN, NAME_PATTERN

# Load model once
nlp = spacy.load("en_core_web_sm")


def remove_overlaps(entities):
    # Sort by start position
    entities = sorted(entities, key=lambda x: x["start"])

    filtered = []
    last_end = -1

    for ent in entities:
        if ent["start"] >= last_end:
            filtered.append(ent)
            last_end = ent["end"]

    return filtered


def detect_pii(text: str):
    entities = []

    # -------------------------
    # REGEX DETECTION
    # -------------------------
    for match in PHONE_PATTERN.finditer(text):
        entities.append({
            "type": "PHONE",
            "value": match.group(),
            "start": match.start(),
            "end": match.end()
        })

    for match in EMAIL_PATTERN.finditer(text):
        entities.append({
            "type": "EMAIL",
            "value": match.group(),
            "start": match.start(),
            "end": match.end()
        })

    # -------------------------
    # NLP DETECTION
    # -------------------------
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities.append({
                "type": "NAME",
                "value": ent.text,
                "start": ent.start_char,
                "end": ent.end_char
            })

        elif ent.label_ == "GPE":
            entities.append({
                "type": "LOCATION",
                "value": ent.text,
                "start": ent.start_char,
                "end": ent.end_char
            })

        elif ent.label_ == "DATE":
            entities.append({
                "type": "DATE",
                "value": ent.text,
                "start": ent.start_char,
                "end": ent.end_char
            })

    # 🔥 THIS IS THE IMPORTANT LINE
    return remove_overlaps(entities)