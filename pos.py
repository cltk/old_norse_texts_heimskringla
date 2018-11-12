"""
POS tags reader for Old Norse texts.
The tagset is available at http://nlp.cs.ru.is/pdf/Tagset.pdf.
Some changes were made:
cc for coordinating conjunctions
ct for


"""

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]
__license__ = "MIT License"

from collections import defaultdict


class POSElement:

    @staticmethod
    def parse(tag, value):
        return value


class Gender(POSElement):
    masculine = "k"
    feminine = "v"
    neuter = "h"

    verbose = defaultdict(str)
    verbose[masculine] = "masculine"
    verbose[feminine] = "feminine"
    verbose[neuter] = "neuter"

    @staticmethod
    def parse(tag, value):
        """
        >>> Gender.parse("k", "")
        ' masculine'
        >>> Gender.parse("v", "")
        ' feminine'
        >>> Gender.parse("h", "")
        ' neuter'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Gender.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Gender.verbose


class Number(POSElement):
    singular = "e"
    plural = "f"

    verbose = defaultdict(str)
    verbose[singular] = "singular"
    verbose[plural] = "plural"

    @staticmethod
    def parse(tag, value):
        """
        >>> Number.parse("e", "")
        ' singular'
        >>> Number.parse("f", "")
        ' plural'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Number.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Number.verbose


class Case:
    nominative = "n"
    accusative = "o"
    dative = "þ"
    genitive = "e"

    verbose = defaultdict(str)
    verbose[nominative] = "nominative"
    verbose[accusative] = "accusative"
    verbose[dative] = "dative"
    verbose[genitive] = "genitive"

    @staticmethod
    def parse(tag, value):
        """
        >>> Case.parse("n", "")
        ' nominative'
        >>> Case.parse("o", "")
        ' accusative'
        >>> Case.parse("þ", "")
        ' dative'
        >>> Case.parse("e", "")
        ' genitive'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Case.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Case.verbose


class Declension:
    strong = "s"
    weak = "v"
    indeclinable = "o"

    verbose = defaultdict(str)
    verbose[strong] = "strong"
    verbose[weak] = "weak"
    verbose[indeclinable] = "indeclinable"

    @staticmethod
    def parse(tag, value):
        """
        >>> Declension.parse("s", "")
        ' strong'
        >>> Declension.parse("v", "")
        ' weak'
        >>> Declension.parse("o", "")
        ' indeclinable'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Declension.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Declension.verbose


class Degree:
    positive = "f"
    comparative = "m"
    superlative = "e"

    verbose = defaultdict(str)
    verbose[positive] = "positive"
    verbose[comparative] = "comparative"
    verbose[superlative] = "superlative"

    @staticmethod
    def parse(tag, value):
        """
        >>> Degree.parse("f", "")
        ' positive'
        >>> Degree.parse("m", "")
        ' comparative'
        >>> Degree.parse("e", "")
        ' superlative'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Degree.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Degree.verbose


class ProperNoun:
    person = "m"
    place = "ö"
    other = "s"

    verbose = defaultdict(str)
    verbose[person] = "person"
    verbose[place] = "place"
    verbose[other] = "other"

    @staticmethod
    def parse(tag, value):
        """
        >>> ProperNoun.parse("m", "")
        ' person'
        >>> ProperNoun.parse("ö", "")
        " place'
        >>> ProperNoun.parse("s", "")
        ' other'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + ProperNoun.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in ProperNoun.verbose


class Pronoun:
    demonstrative = "a"
    indefinite_demonstrative = "b"
    possessive = "e"
    indefinite = "o"
    personal = "p"
    interrogative = "s"
    relative = "t"

    verbose = defaultdict(str)
    verbose[demonstrative] = "demonstrative"
    verbose[indefinite_demonstrative] = "indefinite demonstrative"
    verbose[possessive] = "possessive"
    verbose[indefinite] = "indefinite"
    verbose[personal] = "personal"
    verbose[interrogative] = "interrogative"
    verbose[relative] = "relative"

    @staticmethod
    def parse(tag, value):
        """
        >>> Pronoun.parse("a", "")
        ' demonstrative'
        >>> Pronoun.parse("b", "")
        ' indefinite demonstrative'
        >>> Pronoun.parse("e", "")
        ' possessive'
        >>> Pronoun.parse("o", "")
        ' indefinite'
        >>> Pronoun.parse("p", "")
        ' personal'
        >>> Pronoun.parse("s", "")
        ' interrogative'
        >>> Pronoun.parse("t", "")
        ' relative'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Pronoun.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Pronoun.verbose


class Person:
    first = "1"
    second = "2"
    third = "3"

    verbose = defaultdict(str)
    verbose[first] = "first"
    verbose[second] = "second"
    verbose[third] = "third"

    @staticmethod
    def parse(tag, value):
        """
        >>> Person.parse("1", "")
        ' first'
        >>> Person.parse("2", "")
        ' second'
        >>> Person.parse("3", "")
        ' third'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Person.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Person.verbose


class NumberCategory:
    cardinal = "f"
    ordinal = "o"

    verbose = defaultdict(str)
    verbose[cardinal] = "cardinal"
    verbose[ordinal] = "ordinal"

    @staticmethod
    def parse(tag, value):
        """
        >>> NumberCategory.parse("f", "")
        ' cardinal'
        >>> NumberCategory.parse("o", "")
        ' ordinal'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + NumberCategory.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in NumberCategory.verbose


class Mood:
    infinitive = "n"
    imperative = "b"
    indicative = "f"
    subjunctive = "v"
    supine = "s"
    present_participle = "l"
    past_participle = "þ"

    verbose = defaultdict(str)
    verbose[infinitive] = "infinitive"
    verbose[imperative] = "imperative"
    verbose[indicative] = "indicative"
    verbose[subjunctive] = "subjunctive"
    verbose[supine] = "supine"
    verbose[present_participle] = "present participle"
    verbose[past_participle] = "past participle"

    @staticmethod
    def parse(tag, value):
        """
        >>> Mood.parse("n", "")
        ' infinitive'
        >>> Mood.parse("b", "")
        ' imperative'
        >>> Mood.parse("f", "")
        ' indicative'
        >>> Mood.parse("v", "")
        ' subjunctive'
        >>> Mood.parse("s", "")
        ' supine'
        >>> Mood.parse("l", "")
        ' present participle'
        >>> Mood.parse("þ", "")
        ' past participle'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Mood.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Mood.verbose


class Voice:
    active = "g"
    middle = "m"

    verbose = defaultdict(str)
    verbose[active] = "active"
    verbose[middle] = "middle"

    @staticmethod
    def parse(tag, value):
        """
        >>> Voice.parse("g", "")
        ' active'
        >>> Voice.parse("m", "")
        ' middle'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Voice.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Voice.verbose


class Tense:
    present = "n"
    past = "þ"

    verbose = defaultdict(str)
    verbose[present] = "present"
    verbose[past] = "past"

    @staticmethod
    def parse(tag, value):
        """
        >>> Tense.parse("n", "")
        'present"
        >>> Tense.parse("þ", "")
        'past'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Tense.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Tense.verbose


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

    verbose = defaultdict(str)
    verbose[noun] = "noun"
    verbose[adjective] = "adjective"
    verbose[pronoun] = "pronoun"
    verbose[article] = "article"
    verbose[numeral] = "numeral"
    verbose[verb] = "verb"
    verbose[adverb] = "adverb"
    verbose[conjunction] = "conjunction"
    verbose[unanalysed] = "unanalysed"
    verbose[punctuation] = "punctuation"
    verbose[foreign] = "foreign"

    # A universal part-of-speech tagset by Petrov S., Das D., McDonald R.

    universal = defaultdict(str)
    universal[noun] = "NOUN"
    universal[adjective] = "ADJ"
    universal[pronoun] = "PRON"
    universal[article] = "DET"
    universal[numeral] = "NUM"
    universal[verb] = "VERB"
    universal[adverb] = "ADV"  # in this category, belong ADV, ADP and PRT
    universal[conjunction] = "CONJ"
    universal[unanalysed] = "X"
    universal[foreign] = "X"
    verbose[punctuation] = "."

    @staticmethod
    def apply(tag: str, l_pos: list, value: str):
        i = 1
        for pos in l_pos:
            if isinstance(pos, list):
                for j in pos:
                    if j.can_apply(tag[i]):
                        value = j.parse(tag[i], value)
            else:
                value = pos.parse(tag[i], value)
            i += 1
        return value

    @staticmethod
    def parse(tag):
        """
        >>> MainPOS.parse('fakeþ')
        'pronoun demonstrative masculine singular dative'
        >>> MainPOS.parse('sfg3eþ')
        'verb indicative active third singular past'
        >>> MainPOS.parse('lvensf')
        'adjective feminine singular nominative strong positive'
        >>> MainPOS.parse('fp1en')
        'pronoun personal first singular nominative'
        >>> MainPOS.parse('nkee')
        'noun masculine singular genitive'
        >>> MainPOS.parse('sþgken')
        'verb past participle active masculine singular nominative'
        >>> MainPOS.parse('nhfn')
        'noun neuter plural nominative'
        >>> MainPOS.parse('nveo')
        'noun feminine singular accusative'

        :param tag:
        :return:
        """

        value = ""
        if tag[0] == MainPOS.noun:
            if len(tag) >= 4:
                value = MainPOS.verbose[tag[0]]
                value = MainPOS.apply(tag, [Gender, Number, Case], value)
                if len(tag) == 5:
                    value = ProperNoun.parse(tag[4], value)
            return value

        elif tag[0] == MainPOS.adjective:
            if len(tag) == 6:
                value = MainPOS.verbose[tag[0]]
                value = MainPOS.apply(tag, [Gender, Number, Case, Declension, Degree], value)
            return value

        elif tag[0] == MainPOS.pronoun:
            if len(tag) == 5:
                value = MainPOS.verbose[tag[0]]
                value = MainPOS.apply(tag, [Pronoun, [Person, Gender], Number, Case], value)
            return value

        elif tag[0] == MainPOS.article:
            if len(tag) == 4:
                value = MainPOS.verbose[tag[0]]
                value = MainPOS.apply(tag, [Gender, Number, Case], value)
            return value

        elif tag[0] == MainPOS.numeral:
            if len(tag) == 5:
                value = MainPOS.verbose[tag[0]]
                value = MainPOS.apply(tag, [NumberCategory, Gender, Number, Case], value)

        elif tag[0] == MainPOS.verb:
            if len(tag) == 3 and tag[1] == "n":
                value = MainPOS.verbose[tag[0]]
                value = MainPOS.apply(tag, [Mood, Voice], value)
                value = Mood.parse(tag[1], value)
                value = Voice.parse(tag[2], value)

            elif len(tag) == 6 and tag[1] == "þ":
                value = MainPOS.verbose[tag[0]]
                value = MainPOS.apply(tag, [Mood, Voice, Gender, Number, Case], value)

            elif len(tag) == 6:
                value = MainPOS.verbose[tag[0]]
                value = MainPOS.apply(tag, [Mood, Voice, Person, Number, Tense], value)
            return value

        elif tag[0] == MainPOS.adverb:
            if len(tag) == 2:
                value = MainPOS.verbose[tag[0]]
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
                value = MainPOS.verbose[tag[0]]
                if tag[1] == "n":
                    value += ""
                elif tag[1] == "t":
                    value += ""
                return value

        elif tag[0] == MainPOS.foreign:
            value = MainPOS.verbose[tag[0]]
            return value

        elif tag[0] == MainPOS.unanalysed:
            value = MainPOS.verbose[tag[0]]
            return value

        elif tag[0] == MainPOS.punctuation:
            value = MainPOS.verbose[tag[0]]
            return value

        return value

    @staticmethod
    def parse_universal(tag):
        """
        >>> MainPOS.parse_universal('fakeþ')
        'PRON'
        >>> MainPOS.parse_universal('sfg3eþ')
        'VERB'
        >>> MainPOS.parse_universal('lvensf')
        'ADJ'
        >>> MainPOS.parse_universal('fp1en')
        'PRON'
        >>> MainPOS.parse_universal('nkee')
        'NOUN'
        >>> MainPOS.parse_universal('sþgken')
        'VERB'
        >>> MainPOS.parse_universal('nhfn')
        'NOUN'
        >>> MainPOS.parse_universal('nveo')
        'NOUN'

        :param tag:
        :return:
        """

        if tag[0] == MainPOS.noun or tag[0] == MainPOS.adjective or\
                tag[0] == MainPOS.article or tag[0] == MainPOS.pronoun or \
                tag[0] == MainPOS.numeral or tag[0] == MainPOS.verb or \
                tag[0] == MainPOS.conjunction or tag[0] == MainPOS.foreign or \
                tag[0] == MainPOS.unanalysed or tag[0] == MainPOS.punctuation:
            return MainPOS.universal[tag[0]]

        elif tag[0] == MainPOS.adverb:
            if len(tag) == 2:
                if tag[1] == "a":
                    return "ADV"
                elif tag[1] == "u":
                    return "ADV"
                elif tag[1] == "o" or tag[1] == "þ" or tag[1] == "e":
                    return "ADP"
        return ""

    @staticmethod
    def generate_all_possible_tags():
        """
        TODO correct it because this should not return a list whose length is equal to 1249!

        >>> len(MainPOS.generate_all_possible_tags())
        1249

        :return: All the possible tags
        """
        tags = []

        noun_tags = [MainPOS.noun + gender + number + case for gender in Gender.verbose for number in Number.verbose
                     for case in Case.verbose]

        noun_tags.extend([tag + pn_tag for tag in noun_tags for pn_tag in ProperNoun.verbose])
        tags.extend(noun_tags)

        adj_tags = [MainPOS.adjective + gender + number + case + declension + degree for gender in Gender.verbose
                    for number in Number.verbose for case in Case.verbose for declension in Declension.verbose
                    for degree in Degree.verbose]

        tags.extend(adj_tags)

        pron_tags = [MainPOS.pronoun + pronoun + person + number + case for pronoun in Pronoun.verbose
                     for person in Person.verbose for number in Number.verbose for case in Case.verbose]
        pron_tags.extend([MainPOS.pronoun + pronoun + gender + number + case for pronoun in Pronoun.verbose
                          for gender in Gender.verbose for number in Number.verbose for case in Case.verbose])

        tags.extend(pron_tags)

        tags.extend([MainPOS.article + gender + number + case for gender in Gender.verbose for number in Number.verbose
                     for case in Case.verbose])

        tags.extend(
            [MainPOS.numeral + number_category + gender + number + case for number_category in NumberCategory.verbose
             for gender in Gender.verbose for number in Number.verbose for case in Case.verbose])

        verb_tags = [MainPOS.verb + mood + voice for mood in Mood.verbose for voice in Voice.verbose]
        verb_tags.extend([MainPOS.verb + mood + voice + gender + number + case for mood in Mood.verbose
                          for voice in Voice.verbose for gender in Gender.verbose for number in Number.verbose
                          for case in Case.verbose])
        verb_tags.extend(
            [MainPOS.verb + mood + voice + person + number + tense for mood in Mood.verbose for voice in Voice.verbose
             for person in Person.verbose for number in Number.verbose for tense in Tense.verbose])

        tags.extend(verb_tags)

        tags.extend(["aa", "au", "ao", "aþ", "ae"])
        tags.extend(["cn", "ct", "cc"])
        tags.append(MainPOS.foreign)
        tags.append(MainPOS.unanalysed)
        tags.append(MainPOS.punctuation)
        return tags


def parse(tag):
    if len(tag) > 0:
        value = MainPOS.parse(tag.lower())
    else:
        value = ""
    return value


if __name__ == "__main__":
    print(parse("sfg3en"))
    print(len(MainPOS.generate_all_possible_tags()))
    print(MainPOS.generate_all_possible_tags())
