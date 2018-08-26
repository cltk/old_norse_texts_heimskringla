"""Module to read different kinds of annotated texts
- syllabified texts
- POS tagged texts
"""

import codecs
import os
import re

from nltk.corpus.reader.tagged import TaggedCorpusReader
from cltk.tokenize.word import tokenize_old_norse_words

from utils import remove_punctuations
from text_manager import text_extractor, extract_text

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]
__license__ = "MIT License"

poetic_edda = "Sæmundar-Edda"
poetic_edda_titles = ['Rígsþula', 'Helreið Brynhildar', 'Gróttasöngr', 'Sigrdrífumál', 'Hárbarðsljóð', 'Grímnismál',
                      'Þrymskviða', 'Völuspá', 'Atlamál in grænlenzku', 'Hyndluljóð', 'Skírnismál', 'Hymiskviða',
                      'Atlakviða', 'Vafþrúðnismál', 'Oddrúnarkviða', 'Völundarkviða', 'Alvíssmál', 'Fáfnismál',
                      'Dráp Niflunga', 'Hávamál', 'Guðrúnarhvöt', 'Hamðismál', 'Baldrs draumar', 'Lokasenna',
                      'Guðrúnarkviða']


class Converter:
    @staticmethod
    def converts_html_to_txt():
        """
        >>> Converter.converts_html_to_txt()

        :return:
        """
        book = "Sæmundar-Edda"
        for text_name in os.listdir(book):
            text_extractor("html", "txt", os.path.join(book, text_name), ["complete.html"], ["complete.txt"],
                           extract_text)


class PoeticEddaPOSTaggedReader(TaggedCorpusReader):
    def __init__(self, poem_title):
        assert poem_title in poetic_edda_titles
        TaggedCorpusReader.__init__(self, os.path.join(poetic_edda, poem_title, "txt_files", "pos"),
                                    "*.txt")

    @staticmethod
    def preprocess(path, filename):
        """
        From a text like  provides a text easy to annotate
        >>> PoeticEddaPOSTaggedReader.preprocess("Sæmundar-Edda/Völuspá/txt_files", "complete.txt")

        :param path:
        :param filename:
        :return:
        """
        with codecs.open(os.path.join(path, filename), "r", encoding="utf-8") as f:
            text = f.read()
        # Removes all the lines which are empty or begins with "#"
        text = "\n".join([line for line in text.split(os.linesep) if len(line) >= 1 and line[0] != "#"])
        # Gets all the indices of the number of stanzas
        indices = [(m.start(0), m.end(0)) for m in re.finditer(r"[0-9]{1,2}\.", text)]
        # Extract the paragraphs thanks to indices
        paragraphs = [str(i + 1) + "\n" + text[indices[i][1]:indices[i + 1][0]] for i in range(len(indices) - 1)]
        print(paragraphs[0].split(os.linesep))
        l_res = ["\n".join([" ".join([word+"/" for word in tokenize_old_norse_words(line)]) for line in paragraph.split("\n") if len(line) > 0]) for paragraph in paragraphs]
        print(l_res[:3])
        with open(os.path.join(path, "test_pos_tagged_" + filename), "w", encoding="utf-8") as f:
            f.write("\n".join(l_res))

    def read_annotations(self):
        TaggedCorpusReader.read_annotations(self)


class PoeticEddaSyllabifiedReader(TaggedCorpusReader):
    """"""
    def __init__(self, poem_title):
        TaggedCorpusReader.__init__(self, os.path.join(poetic_edda, poem_title, "txt_files", "syllabified"),
                                    "*.txt")

    @staticmethod
    def preprocess(path, filename):
        """
        Functions to read "normal" texts to texts ready to be annotated
        From a text like Sæmundar-Edda/Völuspá/txt_files/complete.txt provides a text easy to annotate

        :param path:
        :param filename:
        :return:
        """
        with codecs.open(os.path.join(path, filename), "r", encoding="utf-8") as f:
            text = f.read()
        # Removes all the lines which are empty or begins with "#"
        text = "\n".join([line for line in text.split("\n") if len(line) >= 1 and line[0] != "#"])
        # Gets all the indices of the number of stanzas
        indices = [(m.start(0), m.end(0)) for m in re.finditer(r"[0-9]{1,2}\.", text)]
        # Extract the paragraphs thanks to indices
        paragraphs = [text[indices[i][0]:indices[i + 1][0]] for i in range(len(indices) - 1)]
        # For each paragraph, splits the line in words
        presyllabified_text = [[line.strip().split(" ") for line in remove_punctuations(paragraph).split("\n")
                                if line.strip() != ""]
                               for paragraph in paragraphs]
        print(presyllabified_text[:3])
        # l_res is the list of lines of the returned file
        l_res = []
        for index, paragraph in enumerate(presyllabified_text):
            # each paragraph begins with "\n"
            l_res.append("\n")
            for line in paragraph:
                # each new line begins with "+"
                l_res.append("+")
                for word in line:
                    # each new word begins with "-"
                    l_res.append("-")
                    if re.match(r"[0-9]+\.", word) is None:
                        l_res.append(word)
                    else:
                        l_res.append(str(index + 1) + ".")

        with open(os.path.join(path, "test_pre_syl_" + filename), "w", encoding="utf-8") as f:
            f.write("\n".join(l_res))

    @staticmethod
    def read_annotated_text(filename):
        """
        >>> paragraphs = PoeticEddaSyllabifiedReader.read_annotated_text("Sæmundar-Edda/Völuspá/txt_files/syllabified/syllabified_text_complete.txt")
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

        read syllable-annotated text
        """
        with codecs.open(filename, "r", encoding="utf-8") as f:
            text = f.read()
        text = re.sub(r"\+" + os.linesep + "-" + os.linesep + "[0-9]+" + os.linesep + "\+" + os.linesep + "-", "*",
                      text)
        paragraphs = [line for line in text.split("*") if len(line) >= 1 and line[0] != "#"]
        paragraphs = [
            [
                [
                    [
                        syllable.strip() for syllable in remove_punctuations(word).strip().split("\n") if
                        syllable.strip() != ""
                    ]
                    for word in verse.strip().split(r"-") if len(word) != 0
                ]
                for verse in paragraph.split("+") if verse.strip() != "" and verse != "\xa0"
            ]
            for paragraph in paragraphs if len(paragraph.strip()) != 0
        ]
        return paragraphs

    @staticmethod
    def transform(src_filename, dst_filename):
        """
        From a parsed annotated text to a formatted text
        :param src_filename:
        :param dst_filename:
        :return:
        """
        paragraphs = PoeticEddaSyllabifiedReader.read_annotated_text(src_filename)
        text = ""
        for paragraph in paragraphs:
            text = text + "\n"
            for line in paragraph:
                text = text + "\n"
                for syllables in line:
                    # print(syllables)
                    text = text + "".join(syllables) + "/" + "+".join(syllables) + " "
                    # for syllable in //word:
                    #     text = text + "+".join(syllable)
        with codecs.open(dst_filename, "w", encoding="utf-8") as f:
            f.write(text)


# TODO write a function which converts annotation of syllabified texts to list of syllables 
# TODO write a function which converts annotation of POS tagged texts to classes of morpho-syntactic features


if __name__ == "__main__":
    reader = TaggedCorpusReader(os.path.join("Sæmundar-Edda",
                                             "Völuspá",
                                             "txt_files", "pos"),
                                "pos_tagged.txt",
                                sep="|")
    # print(reader.raw()[:300])
    print(reader.words()[:300])

    # Sæmundar-Edda/Völuspá/txt_files/syllabified/syllabified_text_complete.txt
    voluspa_paragraphs = PoeticEddaSyllabifiedReader.read_annotated_text("Sæmundar-Edda/Völuspá/txt_files/syllabified/"
                                                                         "syllabified_text_complete.txt")
    print(voluspa_paragraphs[0])
    print(len(voluspa_paragraphs))
    PoeticEddaSyllabifiedReader.transform("Sæmundar-Edda/Völuspá/txt_files/syllabified/syllabified_text_complete.txt",
                                          "Sæmundar-Edda/Völuspá/txt_files/syllabified/syllabified.txt")
