from typing import Union

from bs4 import Tag

from .normalize import _normalize, _normalized_get_text, _normalized_attrs


class _History:
    @staticmethod
    def origin_dates(history: Tag) -> list[dict[str, str]]:
        origin = history.origin
        if origin is None:
            return []

        result: list[dict[str, str]] = []
        for elem in origin.find_all("origdate"):
            date = _normalized_attrs(elem)
            text = _normalized_get_text(elem)
            if text is not None:
                date["text"] = text
            result.append(date)
        return result

    @staticmethod
    def origin_place(history: Tag) -> dict[str, str]:
        origin = history.origin
        if origin is None:
            return {}

        origin_place = origin.origplace
        if not origin_place:
            return {}

        result = _normalized_attrs(origin_place)
        result["text"] = origin_place.getText().strip()
        return result

    @staticmethod
    def provenances(history: Tag) -> dict[str, list[dict[str, Union[str, list]]]]:
        result: dict[str, list[dict[str, Union[str, list]]]] = {}
        for elem in history.find_all("provenance"):
            typ = _normalize(elem.attrs.get("type"))
            if typ is None:
                continue
            result[typ] = result.get(typ, []) + _History._provenance(elem)
        return result

    @staticmethod
    def _provenance(provenance: Tag) -> list[dict[str, Union[str, list[str]]]]:
        result = []
        # Note: For some it's provenance.p.placename
        for elem in provenance.find_all("placename"):
            place = _normalized_attrs(elem)
            elem_res: dict[str, Union[str, list[str]]] = {}
            text = _normalized_get_text(elem)
            if text is not None:
                elem_res["text"] = text

            for key, value in place.items():
                if key == "ref":
                    elem_res["ref"] = [_normalize(value) for value in value.split(" ")]
                    continue

                elem_res[key] = value

            result.append(elem_res)
        return result


class _ProfileDesc:
    @staticmethod
    def keyword_terms(profile_desc: Tag) -> list[dict[str, str]]:
        textclass = profile_desc.textclass
        if textclass is None:
            return []

        keywords = textclass.keywords
        if keywords is None:
            return []

        result: list[dict[str, str]] = []
        for elem in keywords.find_all("term"):
            term = _normalized_attrs(elem)
            text = _normalized_get_text(elem)
            if text is not None:
                term["text"] = text

            if term:
                result.append(term)
        return result

    @staticmethod
    def lang_usage(profile_desc: Tag) -> dict[str, str]:
        result: dict[str, str] = {}
        lang_usage = profile_desc.langusage
        if lang_usage is None:
            return result
        for elem in lang_usage.find_all("language"):
            ident = _normalize(elem.attrs.get("ident"))
            text = _normalized_get_text(elem)
            if text is not None:
                result[ident] = text
        return result
