"""Module to read syllable-annotated text"""

import codecs
import re
from utils import remove_punctuations


__author__ = ["Clément Besnier <clemsciences@aol.com>", ]
__license__ = "MIT License"


def read_annotated_text(filename):
    """
    >>> paragraphs = read_annotated_text("Sæmundar-Edda/Völuspá/txt_files/syllabified_text_complete.txt")
    >>> paragraph = paragraphs[0]
    >>> paragraph
    [[['Hljóðs'], ['bið'], ['ek'], ['al', 'lar']], [['hel', 'gar'], ['kin', 'dir']], [['mei', 'ri'], ['ok'], ['min', 'ni']], [['mö', 'gu'], ['Heim', 'dal', 'lar']], [['vi', 'ltu'], ['at'], ['ek'], ['Val', 'föðr']], [['vel'], ['fyr'], ['tel', 'ja']], [['forn'], ['spjöll'], ['fi', 'ra']], [['þau'], ['er'], ['fremst'], ['of'], ['man']]]
    >>> short_line = paragraph[0]
    >>> short_line
    [['Hljóðs'], ['bið'], ['ek'], ['al', 'lar']]
    >>> syllabified_word1 = short_line[0]
    >>> syllabified_word1
    ['Hljóðs']
    >>> syllabified_word4 = short_line[3]
    >>> syllabified_word4
    ['al', 'lar']

    """
    with codecs.open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    text = re.sub(r"\+\r\n-\r\n[0-9]+\r\n\+\r\n-", "*", text)
    paragraphs = [line for line in text.split("*") if len(line) >= 1 and line[0] != "#"]
    paragraphs = [
        [
            [
                [
                    syllable.strip() for syllable in remove_punctuations(word).strip().split("\n") if syllable.strip() != ""
                ]
                for word in verse.strip().split("-") if len(word) != 0
            ]
            for verse in paragraph.split("+") if verse.strip() != "" and verse != "\xa0"
        ]
        for paragraph in paragraphs if len(paragraph.strip()) != 0
    ]
    return paragraphs


if __name__ == "__main__":
    paragraphs = read_annotated_text("Sæmundar-Edda/Völuspá/txt_files/syllabified_text_complete.txt")
    print(paragraphs)
