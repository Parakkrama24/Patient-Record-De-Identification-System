from app.services.pii_detector import detect_pii
from app.services.anonymizer import anonymize
from app.services.synthetic_generator import generate_fake

def run_pipeline(text: str):
    entities = detect_pii(text)

    # Replace with synthetic values instead of [TAG]
    offset = 0
    for entity in entities:
        fake_value = generate_fake(entity["type"])

        start = entity["start"] + offset
        end = entity["end"] + offset

        text = text[:start] + fake_value + text[end:]
        offset += len(fake_value) - (end - start)

    return text