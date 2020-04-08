from .normalize import _normalize, _normalized_get_text, _normalized_attrs


class _History:
    @staticmethod
    def origin_dates(history):
        result = []
        for elem in history.origin.findAll("origdate"):
            date = _normalized_attrs(elem)
            date["text"] = _normalized_get_text(elem)
            result.append(date)
        return result

    @staticmethod
    def origin_place(history):
        origin_place = history.origin.origplace
        if not origin_place:
            return {}
        result = _normalized_attrs(origin_place)
        result["text"] = origin_place.getText().strip()
        return result

    @staticmethod
    def provenances(history):
        result = {}
        for elem in history.findAll("provenance"):
            typ = elem.attrs.get("type")
            assert typ not in result
            result[typ] = _History._provenance(elem)
        return result

    @staticmethod
    def _provenance(provenance):
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
    def keyword_terms(profile_desc):
        result = []
        textclass = profile_desc.textclass
        if textclass is None:
            return result
        for elem in textclass.keywords.findAll("term"):
            term = _normalized_attrs(elem)
            term["text"] = _normalized_get_text(elem)
            result.append(term)
        return result

    @staticmethod
    def lang_usage(profile_desc):
        result = {}
        lang_usage = profile_desc.langusage
        if lang_usage is None:
            return result
        for elem in lang_usage.findAll("language"):
            ident = _normalize(elem.attrs.get("ident"))
            result[ident] = _normalized_get_text(elem)
        return result
