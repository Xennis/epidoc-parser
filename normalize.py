def normalize(v):
    if isinstance(v, str):
        return v.lower().strip()


def normalized_get_text(raw):
    parsed = raw.getText().strip()
    return parsed if parsed else None
