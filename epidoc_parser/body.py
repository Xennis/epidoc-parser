from typing import Optional, Any

from bs4 import Tag

from .normalize import _normalize


class _Edition:
    @staticmethod
    def _edition(body: Tag) -> Optional[Any]:
        return body.find("div", type="edition")  # Note: limit to xml:space="preserve"?

    @staticmethod
    def language(body: Tag) -> Optional[str]:
        edition = _Edition._edition(body)
        if edition:
            return _normalize(edition.attrs.get("xml:lang"))

        return None

    @staticmethod
    def foreign_languages(body: Tag) -> dict[str, int]:
        edition = _Edition._edition(body)
        if not edition:
            return {}
        result: dict[str, int] = {}
        for elem in edition.find_all("foreign"):
            lang = _normalize(elem.attrs.get("xml:lang"))
            if not lang:
                continue
            result[lang] = result.get(lang, 0) + 1
        return result


class _Head:

    @staticmethod
    def reprint_from(body: Tag) -> list[str]:
        result: list[str] = []
        for elem in body.find_all("ref", type="reprint-from"):
            n = _normalize(elem.attrs.get("n"))
            if n:
                result.append(n)
        return result

    @staticmethod
    def reprint_in(body: Tag) -> list[str]:
        result: list[str] = []
        for elem in body.find_all("ref", type="reprint-in"):
            n = _normalize(elem.attrs.get("n"))
            if n:
                result.append(n)
        return result
