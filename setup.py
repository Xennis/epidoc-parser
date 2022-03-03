import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

requires = [
    "beautifulsoup4>=4.9.0,<5",
    "lxml>=4.5,<5",
]

setuptools.setup(
    author="Xennis",
    author_email="code@xennis.org",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    description="A small example package",
    install_requires=requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="epidoc",
    packages=["epidoc"],
    python_requires=">=3.6",
    url="https://github.com/Xennis/epidoc-parser",
    version="0.0.1",
)
