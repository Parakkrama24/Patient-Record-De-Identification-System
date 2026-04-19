def anonymize(text: str, entities: list):
    offset = 0

    for entity in entities:
        replacement = f"[{entity['type']}]"

        start = entity["start"] + offset
        end = entity["end"] + offset

        text = text[:start] + replacement + text[end:]

        offset += len(replacement) - (end - start)

    return text