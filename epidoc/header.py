from .normalize import normalize, normalized_get_text, normalized_attrs


class History:
    @staticmethod
    def origin_dates(history):
        result = []
        for elem in history.origin.findAll("origdate"):
            date = normalized_attrs(elem)
            date["text"] = normalized_get_text(elem)
            result.append(date)
        return result

    @staticmethod
    def origin_place(history):
        origin_place = history.origin.origplace
        result = normalized_attrs(origin_place)
        result["text"] = origin_place.getText().strip()
        return result

    @staticmethod
    def provenances(history):
        result = {}
        for elem in history.findAll("provenance"):
            typ = elem.attrs.get("type")
            assert typ not in result
            result[typ] = History._provenance(elem)
        return result

    @staticmethod
    def _provenance(provenance):
        result = []
        # Note: For some it's provenance.p.placename
        for elem in provenance.findAll("placename"):
            place = normalized_attrs(elem)
            place["text"] = normalized_get_text(elem)
            if "ref" in place:
                place["ref"] = [normalize(ref) for ref in place["ref"].split(" ")]
            result.append(place)
        return result


class ProfileDesc:
    @staticmethod
    def keyword_terms(profile_desc):
        result = []
        textclass = profile_desc.textclass
        if textclass is None:
            return result
        for elem in textclass.keywords.findAll("term"):
            term = normalized_attrs(elem)
            term["text"] = normalized_get_text(elem)
            result.append(term)
        return result

    @staticmethod
    def lang_usage(profile_desc):
        result = {}
        lang_usage = profile_desc.langusage
        if lang_usage is None:
            return result
        for elem in lang_usage.findAll("language"):
            ident = normalize(elem.attrs.get("ident"))
            result[ident] = normalized_get_text(elem)
        return result
