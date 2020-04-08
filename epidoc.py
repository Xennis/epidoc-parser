from bs4 import BeautifulSoup

from header import History, ProfileDesc
from normalize import normalize


class EpiDoc:

    title = None
    idno = {}
    material = None
    origin_dates = []
    origin_place = []
    provenances = {}
    terms = []
    languages = {}

    @classmethod
    def create(cls, title, idno, material=None, origin_dates=None, origin_place=None, provenances=None, terms=None, languages=None):
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
        return h

    def __eq__(self, other):
        if not isinstance(other, EpiDoc):
            return False
        return (
            self.title == other.title
            and self.idno == other.idno
            and self.material == other.material
            and self.origin_dates == other.origin_dates
            and self.origin_place == other.origin_place
            and self.provenances == other.provenances
            and self.terms == other.terms
            and self.languages == other.languages
        )

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

    return doc
