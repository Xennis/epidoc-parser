from typing import TypeVar, Any

from bs4 import Tag

T = TypeVar("T")


def _normalize(v: T) -> T:
    if isinstance(v, str):
        return v.lower().strip()  # type: ignore
    return v


def _normalized_get_text(raw):
    if not raw:
        return None
    parsed = raw.getText().strip()
    return parsed if parsed else None


def _normalized_attrs(raw: Tag) -> dict[str, Any]:
    parsed = {}
    for name, value in raw.attrs.items():
        parsed[_normalize(name)] = _normalize(value)
    return parsed
