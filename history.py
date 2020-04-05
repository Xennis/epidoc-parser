from normalize import normalize, normalized_get_text


class ParseHistory:
    @staticmethod
    def dates(history):
        result = []
        for elem in history.origin.findAll("origdate"):
            date = {"text": normalized_get_text(elem)}
            for name, value in elem.attrs.items():
                date[normalize(name)] = normalize(value)
            result.append(date)
        return result

    @staticmethod
    def places(history):
        result = {}
        origin_place = history.origin.origplace
        result["text"] = origin_place.getText().strip()
        for name, value in origin_place.attrs.items():
            result[normalize(name)] = normalize(value)

        for elem in history.findAll("provenance"):
            typ = elem.attrs.get("type")
            assert typ not in result
            result[typ] = ParseHistory.provenance(elem)

        return result

    @staticmethod
    def provenance(provenance):
        result = []
        # Note: For some it's provenance.p.placename
        for elem in provenance.findAll("placename"):
            place = {"text": normalized_get_text(elem)}
            for name, value in elem.attrs.items():
                place[normalize(name)] = normalize(value)

            if "ref" in place:
                place["ref"] = [normalize(ref) for ref in place["ref"].split(" ")]
            result.append(place)
        return result
