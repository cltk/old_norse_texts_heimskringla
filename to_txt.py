"""From Sæmundar-Edda, converts all html_files/complete.html to txt_files/complete.txt"""

import os
from text_manager import text_extractor, extract_text


def converts_html_to_txt():
    book = "Sæmundar-Edda"
    for text_name in os.listdir(book):
        text_extractor("html", "txt", os.path.join(book, text_name), ["complete.html"], ["complete.txt"],
                       extract_text)


if __name__ == '__main__':
    converts_html_to_txt()
