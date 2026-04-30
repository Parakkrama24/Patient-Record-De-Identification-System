from transformers import pipeline

ner_pipeline = pipeline(
    "token-classification",
    model="training/saved_model",
    tokenizer="training/saved_model",
    aggregation_strategy="simple"
)

def detect_pii_with_transformer(text: str):
    results = ner_pipeline(text)

    entities = []

    for item in results:
        label = item["entity_group"]

        if label == "O":
            continue

        entities.append({
            "type": label,
            "value": item["word"],
            "start": item["start"],
            "end": item["end"],
            "score": float(item["score"])
        })

    return entities