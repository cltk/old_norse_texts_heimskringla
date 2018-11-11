"""Some useful pre-processing functions"""

import re

import os

from nltk.corpus import PlaintextCorpusReader

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]
__license__ = "MIT License"


def remove_punctuations(text):
    res = text
    if re.match(r"[0-9]+\.", text) is None:
        res = re.sub("[\-:?;.,]", "", res)
    res = re.sub("z", "s", res)
    res = re.sub("x", "ks", res)
    res = re.sub(r" +", " ", res)
    return res


if __name__ == "__main__":
    # pos_annotated_text = PoeticEddaPOSTaggedReader("Völuspá")
    text = PlaintextCorpusReader(os.path.join(poetic_edda, "Völuspá", "txt_files", "pos"),
                                    "pos_tagged.txt")
    # print(pos_annotated_text.tagged_words()[:50])
    print(text.raw()[:50])
