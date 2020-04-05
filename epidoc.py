from bs4 import BeautifulSoup

from history import ParseHistory
from normalize import normalize


class EpiDocHeader:

    title = None
    idno = {}
    material = None
    dates = []
    places = []

    @classmethod
    def create(cls, title, idno, material=None, dates=None, places=None):
        h = cls()
        h.title = title
        h.idno = idno
        h.material = material
        if dates is not None:
            h.dates = dates
        if places is not None:
            h.places = places
        return h

    def __eq__(self, other):
        if not isinstance(other, EpiDocHeader):
            return False
        return (
            self.title == other.title
            and self.idno == other.idno
            and self.material == other.material
            and self.dates == other.dates
            and self.places == other.places
        )

    def __repr__(self):
        return f"title={self.title},idno={self.idno},material={self.material},date={self.dates},places={self.places}"


class EpiDoc:

    header = None

    @classmethod
    def create(cls, header):
        d = cls()
        d.header = header
        return d

    def __eq__(self, other):
        if not isinstance(other, EpiDoc):
            return False
        return self.header == other.header

    def __repr__(self):
        return f"header={self.header}"


def load(fp):
    return loads(fp.read())


def loads(s):
    soup = BeautifulSoup(s, features="lxml")

    header = EpiDocHeader()

    filedesc = soup.teiheader.filedesc
    header.title = filedesc.titlestmt.title.getText()
    idnos = {}
    for idno in filedesc.publicationstmt.find_all("idno"):
        typ = normalize(idno.attrs.get("type"))
        value = normalize(idno.getText())
        idnos[typ] = value
    header.idno = idnos

    msdesc = filedesc.sourcedesc.msdesc
    if msdesc:
        header.material = normalize(msdesc.physdesc.objectdesc.support.material.getText())
        history = msdesc.history
        header.dates = ParseHistory.dates(history)
        header.places = ParseHistory.places(history)

    doc = EpiDoc()
    doc.header = header
    return doc
