from bs4 import Tag

from .normalize import _normalize


class _Edition:
    @staticmethod
    def _edition(body: Tag):
        return body.find("div", type="edition")  # Note: limit to xml:space="preserve"?

    @staticmethod
    def language(body: Tag):
        edition = _Edition._edition(body)
        if edition:
            return _normalize(edition.attrs.get("xml:lang"))

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
