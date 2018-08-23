"""Functions to read "normal" texts to texts ready to be annotated"""

import os
import re
import codecs
from cltk.tokenize.word import tokenize_old_norse_words

__author__ = ["Clément Besnier <clemsciences@aol.com", ]
__license__ = "MIT License"


def prepostag_text(path, filename):
    """
    From a text like  provides a text easy to annotate
    prepostag_text("Sæmundar-Edda/Völuspá/txt_files", complete.txt)
    :param path:
    :param filename:
    :return:
    """
    with codecs.open(os.path.join(path, filename), "r", encoding="utf-8") as f:
        text = f.read()
    # Removes all the lines which are empty or begins with "#"
    text = "\n".join([line for line in text.split(os.linesep) if len(line) >= 1 and line[0] != "#"])
    print(text[:100])
    # Gets all the indices of the number of stanzas
    indices = [(m.start(0), m.end(0)) for m in re.finditer(r"[0-9]{1,2}\.", text)]
    # Extract the paragraphs thanks to indices
    paragraphs = [str(i+1)+"\n"+text[indices[i][1]:indices[i + 1][0]] for i in range(len(indices) - 1)]
    print(paragraphs[0].split(os.linesep))
    l_res = ["|\n".join(tokenize_old_norse_words(line))+"|\n" for paragraph in paragraphs
             for line in paragraph.split(os.linesep) if len(line) > 0]
    print(l_res[:3])
    with open(os.path.join(path, "test_pos_tagged_"+filename), "w", encoding="utf-8") as f:
        f.write("\n".join(l_res))


# def read_syllabified_text(filename):
#     """
#     Read sylllabified text like "syllabified_complete.txt"
#     :param filename:
#     :return:
#     """
#     with codecs.open(filename, "r", encoding="utf-8") as f:
#         text = f.read()
#     text = "\n".join([line for line in text.split("\n") if len(line) >= 1 and line[0] != "#"])
#     indices = [(m.start(0), m.end(0)) for m in re.finditer(r"[0-9]{1,2}\.", text)]
#     paragraphs = [text[indices[i][1]:indices[i + 1][0]] for i in range(len(indices) - 1)]
#     paragraphs = [[[[syllable.strip() for syllable in word.strip().split("\n") if syllable.strip() != ""]
#                     for word in verse.strip().split("-")] for verse in paragraph.split("+") if
#                    verse.strip() != "" and verse != "\xa0"] for paragraph in paragraphs]
#     return paragraphs
#
#
# def read_annotated_text(filename):
#     """
#     Function used with the annotated result of presyllbify_text like "syllabified_text_complete.txt"
#     :param filename:
#     :return:
#     """
#     # retrieval of annotated results from presyllbify_text
#     with codecs.open(filename, "r", encoding="utf-8") as f:
#         text = f.read()
#     # ancient form
#     text = re.sub(r"\+"+os.linesep+"-"+os.linesep+"\+"+os.linesep+"-", "*", text)
#     # ...
#     # text = re.sub(r"\+\r\n-\r\n\+\r\n-", "*", text)
#     # each paragraph is delimited by "*", empty lines and lines beginning with "#" are removed
#     paragraphs = [line for line in text.split("*") if len(line) >= 1 and line[0] != "#"]
#     # "+" delimits lines
#     # between "+", "-" delimits words
#     # between "-", "\n" delimits syllables
#     # noinspection PyTypeChecker
#     paragraphs = [
#         [
#             [
#                 [syllable.strip() for syllable in remove_punctuations(word).strip().split("\n")
#                  if syllable.strip() != ""]
#
#                 for word in verse.strip().split("-") if len(word) != 0
#             ]
#             for verse in paragraph.split("+") if verse.strip() != "" and verse != "\xa0"
#         ]
#         for paragraph in paragraphs if len(paragraph.strip()) != 0
#     ]
#     return paragraphs


if __name__ == "__main__":
    prepostag_text("Sæmundar-Edda/Völuspá/txt_files/", "complete.txt")
