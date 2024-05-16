import unittest
from french_number_converter.main import convert_to_french


class TestNumberToFrenchConversion(unittest.TestCase):
    def setUp(self):
        self.test_cases = {
            -1: "moins un",
            0: "zéro",
            1: "un",
            5: "cinq",
            10: "dix",
            11: "onze",
            15: "quinze",
            20: "vingt",
            21: "vingt-et-un",
            30: "trente",
            35: "trente-cinq",
            50: "cinquante",
            51: "cinquante-et-un",
            68: "soixante-huit",
            70: "soixante-dix",
            75: "soixante-quinze",
            99: "quatre-vingt-dix-neuf",
            100: "cent",
            101: "cent-un",
            105: "cent-cinq",
            111: "cent-onze",
            123: "cent-vingt-trois",
            168: "cent-soixante-huit",
            171: "cent-soixante-et-onze",
            175: "cent-soixante-quinze",
            199: "cent-quatre-vingt-dix-neuf",
            200: "deux-cents",
            201: "deux-cent-un",
            555: "cinq-cent-cinquante-cinq",
            999: "neuf-cent-quatre-vingt-dix-neuf",
            1000: "mille",
            1001: "mille-un",
            1111: "mille-cent-onze",
            1199: "mille-cent-quatre-vingt-dix-neuf",
            1234: "mille-deux-cent-trente-quatre",
            1999: "mille-neuf-cent-quatre-vingt-dix-neuf",
            2000: "deux-mille",
            2001: "deux-mille-un",
            2020: "deux-mille-vingt",
            2021: "deux-mille-vingt-et-un",
            2345: "deux-mille-trois-cent-quarante-cinq",
            9999: "neuf-mille-neuf-cent-quatre-vingt-dix-neuf",
            10000: "dix-mille",
            11111: "onze-mille-cent-onze",
            12345: "douze-mille-trois-cent-quarante-cinq",
            123456: "cent-vingt-trois-mille-quatre-cent-cinquante-six",
            654321: "six-cent-cinquante-quatre-mille-trois-cent-vingt-et-un",
            999999: "neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf",
        }

        self.invalid_numbers = [1000000, 1000001, 1234567, 9999999, 10000000, 1000000000]

    def test_valid_numbers(self):
        for number, expected in self.test_cases.items():
            with self.subTest(number=number):
                self.assertEqual(convert_to_french(number), expected)

    def test_invalid_numbers(self):
        for number in self.invalid_numbers:
            with self.subTest(number=number):
                with self.assertRaises(ValueError):
                    convert_to_french(number)


if __name__ == "__main__":
    unittest.main()
