def normalize(v):
    if isinstance(v, str):
        return v.lower().strip()


def normalized_get_text(raw):
    parsed = raw.getText().strip()
    return parsed if parsed else None


def normalized_attrs(raw):
    parsed = {}
    for name, value in raw.attrs.items():
        parsed[normalize(name)] = normalize(value)
    return parsed
