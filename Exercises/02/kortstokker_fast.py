#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    # SKRIV DIN KODE HER
    output = "".join(decks)
    return output.strip()


def main():
    # Read input.
    decks = [""] * 100
    for line in stdin:
        (letter, csv) = line.strip().split(':')
        csv = csv.split(',')
        for index in csv:
            decks[int(index)] = letter
    # Merge the decks and print result.
    print(merge(decks))


if __name__ == "__main__":
    main()
