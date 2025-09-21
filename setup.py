import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

requires = [
    "beautifulsoup4>=4.12,<5",
    "lxml>=5.2,<7",
]

setuptools.setup(
    author="Xennis",
    author_email="code@xennis.org",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    description="Parser for EpiDoc (epigraphic documents in TEI XML)",
    install_requires=requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="epidoc-parser",
    packages=["epidoc_parser"],
    python_requires=">=3.9",
    url="https://github.com/Xennis/epidoc-parser",
    version="0.0.1",
)
