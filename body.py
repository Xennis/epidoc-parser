from normalize import normalize


class Edition:
    @staticmethod
    def _edition(body):
        return body.find("div", type="edition")  # Note: limit to xml:space="preserve"?

    @staticmethod
    def language(body):
        edition = Edition._edition(body)
        if edition:
            return normalize(edition.attrs.get("xml:lang"))

    @staticmethod
    def foreign_languages(body):
        edition = Edition._edition(body)
        if not edition:
            return {}
        result = {}
        for elem in edition.find_all("foreign"):
            lang = normalize(elem.attrs.get("xml:lang"))
            if not lang:
                continue
            result[lang] = result.get(lang, 0) + 1
        return result
