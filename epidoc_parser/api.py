import warnings
from typing import Optional, Self, TextIO, Union

from bs4 import BeautifulSoup, Tag, XMLParsedAsHTMLWarning

from .body import _Edition, _Head
from .header import _History, _ProfileDesc
from .normalize import _normalize, _normalized_get_text, _must_find_sub_tag


class EpiDoc:

    title = None
    idno: dict[str, str] = {}
    authority: Optional[str] = None
    availability: Optional[str] = None
    material = None
    origin_dates: list[dict[str, str]] = []
    origin_place: dict[str, str] = {}
    provenances: dict[str, list[dict[str, Union[str, list]]]] = {}
    terms: list[dict[str, str]] = []
    languages: dict[str, str] = {}
    commentary = None
    edition_language = None
    edition_foreign_languages: dict[str, int] = {}
    reprint_from: list[str] = []
    reprint_in: list[str] = []

    @classmethod
    def create(
        cls,
        title: str,
        idno: dict[str, str],
        authority: Optional[str] = None,
        availability: Optional[str] = None,
        material: Optional[str] = None,
        origin_dates: Optional[list[dict[str, str]]] = None,
        origin_place: Optional[dict[str, str]] = None,
        provenances: Optional[dict[str, list[dict[str, Union[str, list]]]]] = None,
        terms: Optional[list[dict[str, str]]] = None,
        languages: Optional[dict[str, str]] = None,
        commentary: Optional[str] = None,
        edition_language: Optional[str] = None,
        edition_foreign_languages: Optional[dict[str, int]] = None,
        reprint_from: Optional[list[str]] = None,
        reprint_in: Optional[list[str]] = None,
    ) -> Self:
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

    def __repr__(self) -> str:
        return f'<EpiDoc "{self.title}">'


def load(fp: TextIO) -> EpiDoc:
    return loads(fp.read())


def loads(s: str) -> EpiDoc:
    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
    soup = BeautifulSoup(s, features="lxml")
    doc = EpiDoc()

    teiheader = _must_find_sub_tag(soup, "teiheader")
    filedesc = _must_find_sub_tag(teiheader, "filedesc")
    title = _must_find_sub_tag(filedesc, "titlestmt", "title")
    doc.title = title.getText()
    idnos = {}
    publication_stmt = _must_find_sub_tag(filedesc, "publicationstmt")
    for idno in publication_stmt.find_all("idno"):
        typ = _normalize(idno.attrs.get("type"))
        value = _normalize(idno.getText())
        if not value:
            continue
        idnos[typ] = value
    doc.idno = idnos
    authority = publication_stmt.find("authority")
    if isinstance(authority, Tag):
        doc.authority = _normalized_get_text(authority)
    availability = publication_stmt.availability
    if availability:
        availability_text = _normalized_get_text(availability)
        license = availability.find("ref", type="license")
        if availability_text and isinstance(license, Tag):
            license_target = license.attrs.get("target")
            if license_target:
                availability_text += f" {license_target}"
        doc.availability = availability_text

    sourcedesc = filedesc.sourcedesc
    if sourcedesc:
        msdesc = sourcedesc.msdesc
        if msdesc:
            msidentifier = msdesc.msidentifier
            if msidentifier:
                idno = msidentifier.idno
                if idno and hasattr(idno, "type"):
                    if idno.get("type") == "invNo":
                        doc.idno["invno"] = idno.text
            physdesc = msdesc.physdesc
            if physdesc:
                objectdesc = physdesc.objectdesc
                if objectdesc:
                    support = objectdesc.support
                    if support and hasattr(support, "material"):
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

    body = _must_find_sub_tag(soup, "body")
    commentary = body.find("div", type="commentary", subtype="general")
    if isinstance(commentary, Tag):
        doc.commentary = _normalized_get_text(commentary)
    doc.edition_language = _Edition.language(body)
    doc.edition_foreign_languages = _Edition.foreign_languages(body)

    doc.reprint_from = _Head.reprint_from(body)
    doc.reprint_in = _Head.reprint_in(body)

    return doc
