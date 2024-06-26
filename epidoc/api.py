from typing import Optional

from bs4 import BeautifulSoup

from .body import _Edition, _Head
from .header import _History, _ProfileDesc
from .normalize import _normalize, _normalized_get_text


class EpiDoc:

    title = None
    idno: dict[str, str] = {}
    authority: Optional[str] = None
    availability: Optional[str] = None
    material = None
    origin_dates: list[str] = []
    origin_place: dict[str, str] = {}
    provenances: dict[str, str] = {}
    terms: list[str] = []
    languages: dict[str, str] = {}
    commentary = None
    edition_language = None
    edition_foreign_languages: dict[str, int] = {}
    reprint_from: list[str] = []
    reprint_in: list[str] = []

    @classmethod
    def create(
        cls,
        title,
        idno,
        authority=None,
        availability=None,
        material=None,
        origin_dates=None,
        origin_place=None,
        provenances=None,
        terms=None,
        languages=None,
        commentary=None,
        edition_language=None,
        edition_foreign_languages=None,
        reprint_from=None,
        reprint_in=None,
    ):
        h = cls()
        h.title = title
        h.idno = idno
        h.material = material
        if authority is not None:
            h.authority = authority
        if availability is not None:
            h.availability = availability
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
        if reprint_from is not None:
            h.reprint_from = reprint_from
        if reprint_in is not None:
            h.reprint_in = reprint_in
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
    publication_stmt = filedesc.publicationstmt
    for idno in publication_stmt.find_all("idno"):
        typ = _normalize(idno.attrs.get("type"))
        value = _normalize(idno.getText())
        if not value:
            continue
        idnos[typ] = value
    doc.idno = idnos
    authority = publication_stmt.find("authority")
    if authority:
        doc.authority = _normalized_get_text(authority)
    availability = publication_stmt.find("availability")
    if availability:
        availability_text = _normalized_get_text(availability)
        license = availability.find("ref", type="license")
        if license:
            license_target = license.attrs.get("target")
            if license_target:
                availability_text += f" {license_target}"
        doc.availability = availability_text

    msdesc = filedesc.sourcedesc.msdesc
    if msdesc:
        physdesc = msdesc.physdesc
        if physdesc:
            support = physdesc.objectdesc.support
            if hasattr(support, "material"):
                doc.material = _normalize(_normalized_get_text(support.material))
        history = msdesc.history
        if history:
            doc.origin_dates = _History.origin_dates(history)
            doc.origin_place = _History.origin_place(history)
            doc.provenances = _History.provenances(history)

    profile_desc = teiheader.profiledesc
    if profile_desc:
        doc.languages = _ProfileDesc.lang_usage(profile_desc)
        doc.terms = _ProfileDesc.keyword_terms(profile_desc)

    body = soup.body
    commentary = body.find("div", type="commentary", subtype="general")
    if commentary:
        doc.commentary = _normalized_get_text(commentary)
    doc.edition_language = _Edition.language(body)
    doc.edition_foreign_languages = _Edition.foreign_languages(body)

    doc.reprint_from = _Head.reprint_from(body)
    doc.reprint_in = _Head.reprint_in(body)

    return doc
