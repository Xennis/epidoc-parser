# EpiDoc Parser

[![Python](https://github.com/Xennis/epidoc-parser/actions/workflows/python.yml/badge.svg?branch=master&event=push)](https://github.com/Xennis/epidoc-parser/actions/workflows/python.yml?query=event%3Apush+branch%3Amaster)

Python parser for EpiDoc (epigraphic documents in TEI XML).

## Usage

### Installation 

Install the package
```shell
pip install git+https://github.com/Xennis/epidoc-parser
```

### Load a document

Load a document from a file
```python
import epidoc

with open("my-epidoc.xml") as f:
    doc = epidoc.load(f)
```

Load a document from a string
```python
import epidoc

my_epidoc = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="http://www.stoa.org/epidoc/schema/8.13/tei-epidoc.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0" xml:id="hgv74005">
   [...]
</TEI>
"""

doc = epidoc.loads(my_epidoc)
```

### Get data from a document

Call the attributes, for example
```python
>>> doc.title
"Ordre de paiement"
>>> doc.material
"ostrakon"
>>> doc.languages
{"en": "Englisch", "la": "Latein", "el": "Griechisch"}
>>> [t.get("text") for t in doc.terms]
["Anweisung", "Zahlung", "Getreide"]
>>> doc.origin_place.get("text")
"Kysis (Oasis Magna)"
>>> doc.origin_dates[0]
{"notbefore": "0301", "notafter": "0425", "precision": "low", "text": "IV - Anfang V"}
```

## Documentation

| Field                     | EpiDoc source element (XPath)                                                  |
|---------------------------|--------------------------------------------------------------------------------|
| commentary                | `//body/div[@type='commentary' and @subtype='general']`                        |
| edition_foreign_languages | `//body/div[@type='edition']//foreign/@xml:lang`                               |
| edition_language          | `//body/div[@type='edition']/@xml:lang`                                        |
| idno                      | `//teiHeader/fileDesc/publicationStmt/idno`                                    |
| authority                 | `//teiHeader/fileDesc/publicationStmt/authority`                               |
| availability              | `//teiHeader/fileDesc/publicationStmt/availability`                            |
| languages                 | `//teiHeader/profileDesc/langUsage/language`                                   |
| material                  | `//teiHeader/fileDesc/sourceDesc/msDesc/physDesc/objectDesc//support/material` |
| origin_dates              | `//teiHeader/fileDesc/sourceDesc/msDesc/history/origin/origDate`               |
| origin_place              | `//teiHeader/fileDesc/sourceDesc/msDesc/history/origin/origPlace`              |
| provenances               | `//teiHeader/fileDesc/sourceDesc/msDesc/history/provenance`                    |
| reprint_from              | `//body/ref[@type='reprint-from']`                                             |
| reprint_in                | `//body/ref[@type='reprint-in']`                                               |
| terms                     | `//teiHeader/profileDesc/textClass//term`                                      |
| title                     | `//teiHeader/fileDesc/titleStmt/title`                                         |

## Development

Create a virtual environment, enable it and install the dependencies
```shell
python3 -m venv venv
. venv/bin/activate
pip install --requirement requirements.txt
```

Run the test
```shell
make unittest
```

## LICENSE

### Code

see [LICENSE](LICENSE)

### Test data

The test data in this project is from the project [idp.data](https://github.com/papyri/idp.data) by [Papyri.info](http://papyri.info). This data is made available under a [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/), with copyright and attribution to the respective projects.
