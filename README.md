# Number to French Converter

This project converts integer numbers into their French word equivalents.

## Installation

Clone the repository and install the requirements:

```sh
git clone https://github.com/Anko59/french-number-converter
cd french-number-converter
pip install -e .
```

## Usage

Once installed using pip, you can use the script `number_to_french` as follows:

```sh
number_to_french 12345
>> The number 12345 in French is: douze-mille-trois-cent-quarante-cinq
```

Or, you can import the module `french_number_converter`'s `convert_to_french` function and use it as follows:

```python
from french_number_converter import convert_to_french
convert_to_french(12345)
>> "douze-mille-trois-cent-quarante-cinq"
```

## Running Tests

To run the tests, use:

```sh
pip install pytest
pytest tests.py
```

## Contributing

To contribute, please fork the repository and submit a pull request.

`pre-commit` is needed to commit on this repository

```sh
pip install pre-commit
pre-commit install
```
