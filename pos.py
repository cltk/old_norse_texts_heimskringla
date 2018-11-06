"""

"""

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]
__license__ = "MIT License"


class Gender:
    masculine = "k"
    feminine = "v"
    neuter = "h"

    @staticmethod
    def parse(tag, value):
        """
        >>> Gender.parse("k", "")
        " masculine"

        >>> Gender.parse("v", "")
        " feminine"
        >>> Gender.parse("h", "")
        " neuter"
        :param tag:
        :param value:
        :return:
        """
        if Gender.masculine == tag[0]:
            value += " masculine"
        elif Gender.feminine == tag[0]:
            value += " feminine"
        elif Gender.neuter == tag[0]:
            value += " neuter"
        return value


class Number:
    singular = "e"
    plural = "f"

    @staticmethod
    def parse(tag, value):
        if Number.singular == tag[0]:
            value += " singular"
        elif Number.plural == tag[0]:
            value += " plural"
        return value


class Case:
    nominative = "n"
    accusative = "o"
    dative = "þ"
    genitive = "e"

    @staticmethod
    def parse(tag, value):
        if Case.nominative == tag[0]:
            value += " nominative"
        elif Case.accusative == tag[0]:
            value += " accusative"
        elif Case.dative == tag[0]:
            value += " dative"
        elif Case.genitive == tag[0]:
            value += " genitive"
        return value


class Declension:
    strong = "s"
    weak = "v"
    indeclinable = "o"

    @staticmethod
    def parse(tag, value):
        if Declension.strong == tag[0]:
            value += " strong"
        elif Declension.weak == tag[0]:
            value += " weak"
        elif Declension.indeclinable == tag[0]:
            value += " indeclinable"
        return value


class Degree:
    positive = "f"
    comparative = "m"
    superlative = "e"

    @staticmethod
    def parse(tag, value):
        if Degree.positive == tag[0]:
            value += " positive"
        elif Degree.comparative == tag[0]:
            value += " comparative"
        elif Degree.superlative == tag[0]:
            value += " superlative"
        return value


class ProperNoun:
    person = "m"
    place = "ö"
    other = "s"

    @staticmethod
    def parse(tag, value):
        if ProperNoun.person == tag[0]:
            value += " person"
        elif ProperNoun.place == tag[0]:
            value += " place"
        elif ProperNoun.other == tag[0]:
            value += " other"
        return value


class Pronoun:
    demontrative = "a"
    indefinite_demonstrative = "b"
    prossessive = "e"
    indefinite = "o"
    personal = "p"
    interrogative = "s"
    relative = "t"

    @staticmethod
    def parse(tag, value):
        if Pronoun.demontrative == tag[0]:
            value += " demontrative"
        elif Pronoun.indefinite_demonstrative == tag[0]:
            value += " indefinite_demonstrative"
        elif Pronoun.prossessive == tag[0]:
            value += " prossessive"
        elif Pronoun.indefinite == tag[0]:
            value += " indefinite"
        elif Pronoun.personal == tag[0]:
            value += " personal"
        elif Pronoun.interrogative == tag[0]:
            value += " interrogative"
        elif Pronoun.relative == tag[0]:
            value += " relative"
        return value


class Person:
    first = "1"
    second = "2"
    third = "3"

    @staticmethod
    def parse(tag, value):
        if Person.first == tag[0]:
            value += " first"
        elif Person.second == tag[0]:
            value += " second"
        elif Person.third == tag[0]:
            value += " third"
        return value


class NumberCategory:
    cardinal = "f"
    ordinal = "o"

    @staticmethod
    def parse(tag, value):
        """
        >>> NumberCategory.parse("f", "")
        " cardinal"
        >>> NumberCategory.parse("o", "")

        " ordinal"
        :param tag:
        :param value:
        :return:
        """
        if NumberCategory.cardinal == tag[0]:
            value += " cardinal"
        elif NumberCategory.ordinal == tag[0]:
            value += " ordinal"
        return value


class Mood:
    infinitive = "n"
    imperative = "b"
    indicative = "f"
    subjunctive = "v"
    supine = "s"
    present_participe = "l"

    @staticmethod
    def parse(tag, value):
        if tag[0] == "n":
            value += " infinitive"
        elif tag[0] == "b":
            value += " imperative"
        elif tag[0] == "f":
            value += " indicative"
        elif tag[0] == "v":
            value += " subjunctive"
        elif tag[0] == "s":
            value += " supine"
        elif tag[0] == "l":
            value += " participe present"
        return value


class Voice:
    active = "g"
    middle = "m"

    @staticmethod
    def parse(tag, value):
        if Voice.active == tag[0]:
            value += " active"
        elif Voice.middle == tag[0]:
            value += " middle"
        return value


class Tense:
    present = "n"
    past = "þ"

    @staticmethod
    def parse(tag, value):
        if Tense.present == tag[0]:
            value += " present"
        elif Tense.past == tag[0]:
            value += " past"
        return value


class MainPOS:
    noun = "n"
    adjective = "l"
    pronoun = "f"
    article = "g"
    numeral = "t"
    verb = "s"
    adverb = "a"
    conjunction = "c"
    foreign = "e"
    unanalysed = "x"
    punctuation = "p"

    @staticmethod
    def parse(tag):
        """
        >>> MainPOS.parse('fakeþ')

        >>> MainPOS.parse('sfg3eþ')

        >>> MainPOS.parse('lvensf')

        >>> MainPOS.parse('fp1en')

        >>> MainPOS.parse('nkee')

        >>> MainPOS.parse('sþken')

        >>> MainPOS.parse('nhfn')

        >>> MainPOS.parse('nveo')


        :param tag:
        :return:
        """

        value = ""
        if tag[0] == MainPOS.noun:
            if len(tag) >= 4:
                value = "noun"
                value = Gender.parse(tag[1], value)
                value = Number.parse(tag[2], value)
                value = Case.parse(tag[3], value)
                if len(tag) == 5:
                    value = ProperNoun.parse(tag[4], value)
            return value

        elif tag[0] == MainPOS.adjective:
            if len(tag) == 6:
                value = "adjective"
                value = Gender.parse(tag[1], value)
                value = Number.parse(tag[2], value)
                value = Case.parse(tag[3], value)
                value = Declension.parse(tag[4], value)
                value = Degree.parse(tag[5], value)
            return value

        elif tag[0] == MainPOS.pronoun:
            if len(tag) == 5:
                value = "pronoun"

                value = Pronoun.parse(tag[1], value)

                value = Person.parse(tag[2], value)
                value = Gender.parse(tag[2], value)

                value = Number.parse(tag[3], value)
                value = Case.parse(tag[4], value)
            return value

        elif tag[0] == MainPOS.article:
            if len(tag) == 4:
                value = "article"
                value = Gender.parse(tag[1], value)
                value = Number.parse(tag[2], value)
                value = Case.parse(tag[3], value)
            return value

        elif tag[0] == MainPOS.numeral:
            if len(tag) == 5:
                value = "numeral"
                value = NumberCategory.parse(tag[1], value)
                value = Gender.parse(tag[2], value)
                value = Number.parse(tag[3], value)
                value = Case.parse(tag[4], value)

        elif tag[0] == MainPOS.verb:
            if len(tag) == 3 and tag[1] == "n":
                value = "verb"
                value = Mood.parse(tag[1], value)
                value = Voice.parse(tag[2], value)

            elif len(tag) == 6:
                value = "verb" + value
                value = Mood.parse(tag[1], value)
                value = Voice.parse(tag[2], value)
                value = Person.parse(tag[3], value)
                value = Number.parse(tag[4], value)
                value = Tense.parse(tag[5], value)
            return value

        elif tag[0] == MainPOS.adverb:
            if len(tag) == 2:

                value = "adverb"
                if tag[1] == "a":
                    value += " no case "
                elif tag[1] == "u":
                    value += " exclamation"
                elif tag[1] == "o":
                    value += " accusative"
                elif tag[1] == "þ":
                    value += " dative"
                elif tag[1] == "e":
                    value += " genitive"
            return value

        elif tag[0] == MainPOS.conjunction:
            if len(tag) == 2:
                value += "conjunction"
                if tag[1] == "n":
                    value += ""
                elif tag[1] == "t":
                    value += ""
                return value

        elif tag[0] == MainPOS.foreign:
            value += "foreign"
            return value

        elif tag[0] == MainPOS.unanalysed:
            value = "unanalysed word"
            return value

        elif tag[0] == MainPOS.punctuation:
            value = "punctuation"
            return value

        return value


def parse(tag):
    if len(tag) > 0:
        value = MainPOS.parse(tag.lower())
    else:
        value = ""
    return value


if __name__ == "__main__":
    print(parse("sfg3en"))
