"""

"""

import re
import os
import codecs

__author__ = ["Clément Besnier <clemsciences@aol.com", ]
__license__ = "MIT License"


def read_syllabified_text(filename):
    with codecs.open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    text = "\n".join([line for line in text.split("\n") if len(line) >= 1 and line[0] != "#"])
    indices = [(m.start(0), m.end(0)) for m in re.finditer(r"[0-9]{1,2}\.", text)]
    paragraphs = [text[indices[i][1]:indices[i + 1][0]] for i in range(len(indices) - 1)]
    paragraphs = [[[[syllable.strip() for syllable in word.strip().split("\n") if syllable.strip() != ""] for word in verse.strip().split("-")] for verse in paragraph.split("+") if
                   verse.strip() != "" and verse != "\xa0"] for paragraph in paragraphs]
    return paragraphs


def read_annotated_text(filename):
    with codecs.open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    text = re.sub(r"\+\r\n-\r\n\+\r\n-", "*", text)
    paragraphs = [line for line in text.split("*") if len(line) >= 1 and line[0] != "#"]
    # print(paragraphs[:2])
    paragraphs = [
        [
            [
                [
                    syllable.strip() for syllable in remove_punctuations(word).strip().split("\n") if syllable.strip() != ""
                ]
                for word in verse.strip().split("-") if len(word) != 0
            ]
            for verse in paragraph.split("+") if verse.strip() != "" and verse != "\xa0"
        ]
        for paragraph in paragraphs if len(paragraph.strip()) != 0
    ]
    return paragraphs


def remove_punctuations(text):
    res = text
    # for punctuation in "-:?":
    #    res = "".join(res.split(punctuation))
    if re.match(r"[0-9]+\.", text) is None:
        res = re.sub("[\-:?;.,]", "", res)
    res = re.sub("z", "s", res)
    res = re.sub("x", "ks", res)
    res = re.sub(r" +", " ", res)
    return res


def presyllbify_text(path, filename):
    with codecs.open(os.path.join(path, filename), "r", encoding="utf-8") as f:
        text = f.read()
    text = "\n".join([line for line in text.split("\n") if len(line) >= 1 and line[0] != "#"])
    indices = [(m.start(0), m.end(0)) for m in re.finditer(r"[0-9]{1,2}\.", text)]
    paragraphs = [text[indices[i][0]:indices[i + 1][0]] for i in range(len(indices) - 1)]
    presyllabified_text = [[line.strip().split(" ") for line in remove_punctuations(paragraph).split("\n") if line.strip() != ""] for paragraph in paragraphs]
    print(presyllabified_text[:3])
    l_res = []
    for index, i in enumerate(presyllabified_text):
        l_res.append("\n")
        # l_res.append(str(index+1)+".")
        for j in i:
            l_res.append("+")
            for k in j:
                l_res.append("-")
                if re.match(r"[0-9]+\.", k) is None:
                    l_res.append(k)
    with open(os.path.join(path, "pre_syl_"+filename), "w", encoding="utf-8") as f:
        f.write("\n".join(l_res))


if __name__ == "__main__":
    # paragraphs = read_syllabified_text("Sæmundar-Edda/Völuspá/txt_files/syllabified_complete.txt")
    # for paragraph in paragraphs:
    #     print(paragraph)
    # presyllbify_text("Sæmundar-Edda/Völuspá/txt_files/", "complete.txt")
    paragraphs = read_annotated_text("Sæmundar-Edda/Völuspá/txt_files/pre_syl_complete.txt")
    print(paragraphs)

