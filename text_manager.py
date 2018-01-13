# encoding:utf8
import os
import codecs
import json
from bs4 import BeautifulSoup


__author__ = "Clément Besnier"

accepted_formats = ["html", "json", "txt"]


def text_extractor(orig_format, dest_format, folder, orig_filenames, dest_filenames, extraction_method,
                     mode="r", encoding="utf8"):
    assert orig_format in ["html"]
    assert dest_format in ["txt"]
    for orig_filename, dest_filename in zip(orig_filenames, dest_filenames):
        with codecs.open(os.path.join(folder, orig_format+"_files", orig_filename), mode, encoding) as f_orig:
            with codecs.open(os.path.join(folder, dest_format+"_files", dest_filename), "w", encoding) as f_dest:
                f_dest.write(extract_text(f_orig.read()))


def extract_text(data):
    soup = BeautifulSoup(data, 'html.parser')
    return soup.get_text()


class TextLoader:
    def __init__(self, name, extension):
        self.name = name
        self.extension = extension

    @staticmethod
    def get_available_names():
        return [name for name in os.listdir(".") if "." not in name]

    def load(self):
        try:
            if self.extension in ["txt", "html"]:
                with codecs.open(os.path.join(self.name, self.extension+"_files", "complete."+self.extension),
                                 "r", encoding="utf8") as f:
                    return f.read()
            elif self.extension == "json":
                with open(os.path.join(self.name, self.extension+"_files", "complete."+self.extension),
                          "r", encoding="utf8") as f:
                    return json.load(f)
        except:
            print("Impossible to load the wished text")
            return None

if __name__ == "__main__":
    text_extractor("html", "txt", os.path.join("Sæmundar-Edda", "Atlakviða"), ["complete.html"], ["complete.txt"], extract_text)
    loader = TextLoader(os.path.join("Sæmundar-Edda", "Atlakviða"), "txt")
    print(loader.get_available_names())
    print(loader.load()[:100])

