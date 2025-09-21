import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

requires = [
    "beautifulsoup4>=4.13,<5",
    "lxml>=6,<7",
]

setuptools.setup(
    author="Xennis",
    author_email="code@xennis.org",
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Markup :: XML",
    ],
    description="Parser for EpiDoc (epigraphic documents in TEI XML)",
    install_requires=requires,
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="epidoc-parser",
    packages=["epidoc_parser"],
    python_requires=">=3.9",
    url="https://github.com/Xennis/epidoc-parser",
    version="0.0.1",
)
