"""Module to read different kinds of annotated texts
- syllabified texts
- POS tagged texts
"""


__author__ = ["Clément Besnier <clemsciences@aol.com>", ]
__license__ = "MIT License"


class Reader:
    def __init__(self):
        pass

    def read_raw(self):
        pass

    def preprocess(self):
        pass

    def read_annotations(self):
        pass


class POSTaggedReader(Reader):
    def __init__(self):
        Reader.__init__(self)

    def read_raw(self):
        Reader.read_raw(self)

    def preprocess(self):
        Reader.preprocess(self)

    def read_annotations(self):
        Reader.read_annotations(self)


class SyllabifiedReader(Reader):
    def __init__(self):
        Reader.__init__(self)

    def read_raw(self):
        Reader.read_raw(self)

    def preprocess(self):
        Reader.preprocess(self)

    def read_annotations(self):
        Reader.read_annotations(self)
