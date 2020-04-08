def _normalize(v):
    if isinstance(v, str):
        return v.lower().strip()
    return v


def _normalized_get_text(raw):
    parsed = raw.getText().strip()
    return parsed if parsed else None


def _normalized_attrs(raw):
    parsed = {}
    for name, value in raw.attrs.items():
        parsed[_normalize(name)] = _normalize(value)
    return parsed
