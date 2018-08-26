

from enum import Enum, auto

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]
__license__ = "MIT License"


class POSClass(Enum):
    noun = auto()
    adjective = auto()
    pronoun = auto()
    verb = auto()
    past_participle = auto()
    adverb_and_preposition = auto()
    conjunction = auto()
    article = auto()
    number = auto()
    punctuation = auto()
    unknown = auto()


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
