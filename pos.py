

from enum import Enum, auto

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]
__license__ = "MIT License"


class POSClass(Enum):
    noun = auto()  # noun
    adjective = auto()  # adjective
    pronoun = auto()  # pronoun
    verb = auto()  # verb
    past_participle = auto()  # past_participle
    adverb_and_preposition = auto()  # adverb_and_preposition
    conjunction = auto()  # conjunction
    article = auto()  # article
    number = auto()  # number
    punctuation = auto()  # punctuation
    unknown = auto()  # unknown


class POSGender(Enum):
    k = auto()  # masculine
    v = auto()  # feminine
    h = auto()  # neuter
    x = auto()  # unknown


class POSNumber(Enum):
    e = auto()  # singular
    f = auto()  # plural



class POSTense(Enum):
    n = auto()  # present
    þ = auto()  # past


class POSCase(Enum):
    n = auto()  # nominative
    o = auto()  # accusative
    þ = auto()  # dative
    e = auto()  # genitive


class POSNounKind(Enum):
    m = auto()
    oe = auto()
    s = auto()


class POSPronounKind(Enum):
    a = auto()  # demonstrative
    b = auto()  # reflexive
    e = auto()  # possessive
    o = auto()  # indefinite
    p = auto()  # personal
    s = auto()  # interrogative
    t = auto()  # relative


class POSAdjectiveKind(Enum):
    s = auto()  # strong
    v = auto()  # weak
    o = auto()  # no-declension


class POSAdjectiveGradation(Enum):
    f = auto()  # normal
    m = auto()  # comparative
    e = auto()  # superlative


class POSVerbMode(Enum):
    n = auto()  # infinitive
    b = auto()  # imperative
    f = auto()  # indicative
    v = auto()  # subjunctive
    s = auto()  # supine
    l = auto()  # present_participle


class POSVerbAction(Enum):
    g = auto()  # active
    m = auto()  # middle


class POSTagReader:
    def __init__(self, tag):
        self.tag = tag

    def get_meaning(self):
        pass

    def analyze(self):
        context = None
        for i, c in enumerate(self.tag):
            if c == "n":
                self.read_noun_tag()

    def read_noun_tag(self):
        chain = [POSGender, POSNumber, POSCase, POSNounKind]
        pass

    def read_adjective_tag(self):
        chain = [POSGender, POSNumber, POSCase, POSAdjectiveKind]
        pass

    def read_pronoun_tag(self):
        chain = [POSPronounKind, POSGender, lambda x: str(x), POSNumber]
        pass

    def read_verb_tag(self):
        chain = [POSVerbMode, POSVerbMode, lambda x: str(x), POSNumber, POSTense]
        pass

    def read_past_participle_tag(self):
        chani = [POSGender, POSNumber, POSCase]
        pass

    def read_adverb_preposition_tag(self):
        pass

    def read_article_tag(self):
        pass

    def read_number_tag(self):
        pass

    def read_conjunction(self):
        pass