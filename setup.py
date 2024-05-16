from setuptools import setup

setup(
    name="french_number_converter",
    description="Converts numbers to French full letters.",
    version="1.0.0",
    packages=["french_number_converter"],
    url="https://github.com/Anko59/french-number-converter.git",
    author="Anko59",
    author_email="jeancollette138@gmail.com",
    keywords=["french", "numbers", "converter"],
    entry_points={
        "console_scripts": [
            "number_to_french=french_number_converter.main:main",
        ],
    },
    python_requires=">=3.6",
)
