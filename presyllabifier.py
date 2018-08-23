"""Functions to read "normal" texts to texts ready to be annotated"""

import re
import os
import codecs
from utils import remove_punctuations

__author__ = ["Clément Besnier <clemsciences@aol.com", ]
__license__ = "MIT License"


def read_syllabified_text(filename):
    """
    Read sylllabified text like "syllabified_complete.txt"
    :param filename:
    :return:
    """
    with codecs.open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    text = "\n".join([line for line in text.split("\n") if len(line) >= 1 and line[0] != "#"])
    indices = [(m.start(0), m.end(0)) for m in re.finditer(r"[0-9]{1,2}\.", text)]
    paragraphs = [text[indices[i][1]:indices[i + 1][0]] for i in range(len(indices) - 1)]
    paragraphs = [[[[syllable.strip() for syllable in word.strip().split("\n") if syllable.strip() != ""]
                    for word in verse.strip().split("-")] for verse in paragraph.split("+") if
                   verse.strip() != "" and verse != "\xa0"] for paragraph in paragraphs]
    return paragraphs


def read_annotated_text(filename):
    """
    Function used with the annotated result of presyllbify_text like "syllabified_text_complete.txt"
    :param filename:
    :return:
    """
    # retrieval of annotated results from presyllbify_text
    with codecs.open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    # ancient form
    text = re.sub(r"\+"+os.linesep+"-"+os.linesep+"\+"+os.linesep+"-", "*", text)
    # ...
    # text = re.sub(r"\+\r\n-\r\n\+\r\n-", "*", text)
    # each paragraph is delimited by "*", empty lines and lines beginning with "#" are removed
    paragraphs = [line for line in text.split("*") if len(line) >= 1 and line[0] != "#"]
    # "+" delimits lines
    # between "+", "-" delimits words
    # between "-", "\n" delimits syllables
    # noinspection PyTypeChecker
    paragraphs = [
        [
            [
                [syllable.strip() for syllable in remove_punctuations(word).strip().split("\n")
                 if syllable.strip() != ""]

                for word in verse.strip().split("-") if len(word) != 0
            ]
            for verse in paragraph.split("+") if verse.strip() != "" and verse != "\xa0"
        ]
        for paragraph in paragraphs if len(paragraph.strip()) != 0
    ]
    return paragraphs


def presyllabify_text(path, filename):
    """
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
                    l_res.append(str(index+1)+".")

    with open(os.path.join(path, "test_pre_syl_"+filename), "w", encoding="utf-8") as f:
        f.write("\n".join(l_res))


if __name__ == "__main__":
    res_paragraphs = read_syllabified_text("Sæmundar-Edda/Völuspá/txt_files/syllabified_complete.txt")
    for res_paragraph in res_paragraphs:
        print(res_paragraph)
    presyllabify_text("Sæmundar-Edda/Völuspá/txt_files/", "complete.txt")
