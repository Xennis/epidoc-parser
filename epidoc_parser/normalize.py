from typing import TypeVar, Any, Optional

from bs4 import Tag

T = TypeVar("T")


def _normalize(v: T) -> T:
    if isinstance(v, str):
        return v.lower().strip()  # type: ignore
    return v


def _normalized_get_text(raw: Optional[Tag]) -> Optional[str]:
    if not raw:
        return None
    parsed = raw.getText().strip().replace("\n", "")
    return parsed if parsed else None


def _normalized_attrs(raw: Tag) -> dict[str, str]:
    parsed = {}
    for name, value in raw.attrs.items():
        parsed[_normalize(name)] = _normalize(value)
    return parsed


def _must_find_sub_tag(tag: Tag, *keys: str) -> Tag:
    current_tag = tag
    for key in keys:
        sub_tag = current_tag.find(key)
        assert isinstance(sub_tag, Tag), f"${key} is not None"
        current_tag = sub_tag

    return current_tag
