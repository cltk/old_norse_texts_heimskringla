"""Some useful pre-processing functions"""

import re

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
