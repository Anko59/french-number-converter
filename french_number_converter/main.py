import argparse

number_to_french = {
    0: "zéro",
    1: "un",
    2: "deux",
    3: "trois",
    4: "quatre",
    5: "cinq",
    6: "six",
    7: "sept",
    8: "huit",
    9: "neuf",
    10: "dix",
    11: "onze",
    12: "douze",
    13: "treize",
    14: "quatorze",
    15: "quinze",
    16: "seize",
    20: "vingt",
    30: "trente",
    40: "quarante",
    50: "cinquante",
    60: "soixante",
    70: "soixante-dix",
    80: "quatre-vingt",
    90: "quatre-vingt-dix",
    100: "cent",
    1000: "mille",
}


def convert_to_french(n):
    n = _convert_to_french(n)
    if n.endswith("quatre-vingt") or (n.endswith("cent") and n != "cent"):
        return n + "s"
    return n


def _convert_to_french(n):
    if n in number_to_french:
        return number_to_french[n]
    elif n < 0:
        return f"moins {convert_to_french(-n)}"
    elif n < 20:
        return f"dix-{number_to_french[n - 10]}"
    elif n < 100:
        return convert_tens_to_french(n)
    elif n < 1000:
        return convert_hundreds_to_french(n)
    elif n < 1000000:
        return convert_thousands_to_french(n)
    else:
        raise ValueError("This script only supports numbers up to 999,999")


def convert_tens_to_french(n):
    tens, below_ten = divmod(n, 10)
    if tens in [7, 9]:
        if tens == 7 and below_ten == 1:
            return "soixante-et-onze"
        return "-".join([number_to_french[tens * 10 - 10], convert_to_french(below_ten + 10)])
    elif below_ten == 1 and tens != 8:
        return f"{number_to_french[tens * 10]}-et-{number_to_french[below_ten]}"
    return "-".join([number_to_french[tens * 10], number_to_french[below_ten]])


def convert_hundreds_to_french(n):
    hundreds, remainder = divmod(n, 100)
    base = "cent" if hundreds == 1 else f"{number_to_french[hundreds]}-cent"
    return base if remainder == 0 else f"{base}-{convert_to_french(remainder)}"


def convert_thousands_to_french(n):
    thousands, remainder = divmod(n, 1000)
    base = "mille" if thousands == 1 else f"{convert_to_french(thousands)}-mille"
    return base if remainder == 0 else f"{base}-{convert_to_french(remainder)}"


def main():
    parser = argparse.ArgumentParser(description="Convert integer numbers to French full letters.")
    parser.add_argument("number", type=int, help="The integer number to convert")
    args = parser.parse_args()

    try:
        french_number = convert_to_french(args.number)
        print(f"The number {args.number} in French is: {french_number}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
