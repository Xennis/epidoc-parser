from bs4 import BeautifulSoup

from body import Edition
from header import History, ProfileDesc
from normalize import normalize, normalized_get_text


class EpiDoc:

    title = None
    idno = {}
    material = None
    origin_dates = []
    origin_place = []
    provenances = {}
    terms = []
    languages = {}
    commentary = None
    edition_language = None
    edition_foreign_languages = {}

    @classmethod
    def create(
        cls,
        title,
        idno,
        material=None,
        origin_dates=None,
        origin_place=None,
        provenances=None,
        terms=None,
        languages=None,
        commentary=None,
        edition_language=None,
        edition_foreign_languages=None,
    ):
        h = cls()
        h.title = title
        h.idno = idno
        h.material = material
        if origin_dates is not None:
            h.origin_dates = origin_dates
        if origin_place is not None:
            h.origin_place = origin_place
        if provenances is not None:
            h.provenances = provenances
        if terms is not None:
            h.terms = terms
        if languages is not None:
            h.languages = languages
        h.commentary = commentary
        h.edition_language = edition_language
        if edition_foreign_languages is not None:
            h.edition_foreign_languages = edition_foreign_languages
        return h

    def __repr__(self):
        return f'<EpiDoc "{self.title}">'


def load(fp):
    return loads(fp.read())


def loads(s):
    soup = BeautifulSoup(s, features="lxml")

    doc = EpiDoc()

    teiheader = soup.teiheader
    filedesc = teiheader.filedesc
    doc.title = filedesc.titlestmt.title.getText()
    idnos = {}
    for idno in filedesc.publicationstmt.find_all("idno"):
        typ = normalize(idno.attrs.get("type"))
        value = normalize(idno.getText())
        idnos[typ] = value
    doc.idno = idnos

    msdesc = filedesc.sourcedesc.msdesc
    if msdesc:
        doc.material = normalize(msdesc.physdesc.objectdesc.support.material.getText())
        history = msdesc.history
        doc.origin_dates = History.origin_dates(history)
        doc.origin_place = History.origin_place(history)
        doc.provenances = History.provenances(history)

    profile_desc = teiheader.profiledesc
    doc.languages = ProfileDesc.lang_usage(profile_desc)
    doc.terms = ProfileDesc.keyword_terms(profile_desc)

    body = soup.body
    commentary = body.find("div", type="commentary", subtype="general")
    if commentary:
        doc.commentary = normalized_get_text(commentary)
    doc.edition_language = Edition.language(body)
    doc.edition_foreign_languages = Edition.foreign_languages(body)

    return doc
