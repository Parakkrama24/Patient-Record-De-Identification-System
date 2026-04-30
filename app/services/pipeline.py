from app.services.transformer_detector import detect_pii_with_transformer
from app.services.pii_detector import detect_pii, remove_overlaps  # regex + spacy fallback
from app.services.synthetic_generator import generate_fake


def run_pipeline(text: str):

    # 🔥 1. Get entities from BOTH systems
    transformer_entities = detect_pii_with_transformer(text)
    regex_entities = detect_pii(text)

    # 🔥 2. Merge them
    entities = transformer_entities + regex_entities

    # 🔥 3. Sort by position
    entities = sorted(entities, key=lambda x: x["start"])

    # 🔥 4. Remove overlaps (reuse your old function)
    entities = remove_overlaps(entities)

    # 🔥 5. Replace from RIGHT → LEFT (CRITICAL FIX)
    for entity in reversed(entities):
        clean_type = entity["type"].replace("B-", "").replace("I-", "")
        fake_value = generate_fake(clean_type)

        start = entity["start"]
        end = entity["end"]

        text = text[:start] + fake_value + text[end:]

    return text