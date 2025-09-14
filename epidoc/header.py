from typing import Any

from bs4 import Tag

from .normalize import _normalize, _normalized_get_text, _normalized_attrs


class _History:
    @staticmethod
    def origin_dates(history: Tag) -> list[Any]:
        origin = history.origin
        if origin is None:
            return []

        result = []
        for elem in origin.findAll("origdate"):  # type: ignore
            date = _normalized_attrs(elem)
            date["text"] = _normalized_get_text(elem)
            result.append(date)
        return result

    @staticmethod
    def origin_place(history: Tag) -> dict[str, Any]:
        origin = history.origin
        if origin is None:
            return {}

        origin_place = origin.origplace  # type: ignore
        if not origin_place:
            return {}

        result = _normalized_attrs(origin_place)
        result["text"] = origin_place.getText().strip()
        return result

    @staticmethod
    def provenances(history: Tag) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for elem in history.findAll("provenance"):
            typ = _normalize(elem.attrs.get("type"))
            if typ is None:
                continue
            result[typ] = result.get(typ, []) + _History._provenance(elem)
        return result

    @staticmethod
    def _provenance(provenance: Tag):
        result = []
        # Note: For some it's provenance.p.placename
        for elem in provenance.findAll("placename"):
            place = _normalized_attrs(elem)
            place["text"] = _normalized_get_text(elem)
            if "ref" in place:
                place["ref"] = [_normalize(ref) for ref in place["ref"].split(" ")]
            result.append(place)
        return result


class _ProfileDesc:
    @staticmethod
    def keyword_terms(profile_desc: Tag) -> list[dict[str, Any]]:
        textclass = profile_desc.textclass
        if textclass is None:
            return []

        keywords = textclass.keywords
        if keywords is None:
            return []

        result: list[dict[str, Any]] = []
        for elem in keywords.findAll("term"):  # type: ignore
            term = _normalized_attrs(elem)
            term["text"] = _normalized_get_text(elem)
            result.append(term)
        return result

    @staticmethod
    def lang_usage(profile_desc: Tag) -> dict[str, str]:
        result: dict[str, str] = {}
        lang_usage = profile_desc.langusage
        if lang_usage is None:
            return result
        for elem in lang_usage.findAll("language"):
            ident = _normalize(elem.attrs.get("ident"))
            result[ident] = _normalized_get_text(elem)
        return result
