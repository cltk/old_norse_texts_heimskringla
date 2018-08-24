"""
Source:
http://heimskringla.no/wiki/Kildeindex
"""
from text_manager import *


edda_snorri_sites = ["http://heimskringla.no/wiki/Sk%C3%A1ldskaparm%C3%A1l", "http://heimskringla.no/wiki/Prologus",
                     "http://heimskringla.no/wiki/H%C3%A1ttatal", "http://heimskringla.no/wiki/Gylfaginning",
                     "http://heimskringla.no/wiki/Edda_Snorra_Sturlusonar"]
edda_snorri_html = ["gylfaginning.html", "haattatal.html", "prologus.html", "skaaldskaparmaal.html"]
edda_snorri_txt = ["gylfaginning.txt", "haattatal.txtl", "prologus.txt", "skaaldskaparmaal.txt"]


older_edda_sites = ["http://heimskringla.no/wiki/Gr%C3%ADmnism%C3%A1l",
                    "http://heimskringla.no/wiki/H%C3%A1vam%C3%A1l",
                    "http://heimskringla.no/wiki/R%C3%ADgs%C3%BEula",
                    "http://heimskringla.no/wiki/Baldrs_draumar",
                    "http://heimskringla.no/wiki/Alv%C3%ADssm%C3%A1l",
                    "http://heimskringla.no/wiki/%C3%9Erymskvi%C3%B0a",
                    "http://heimskringla.no/wiki/Lokasenna",
                    "http://heimskringla.no/wiki/Hymiskvi%C3%B0a",
                    "http://heimskringla.no/wiki/H%C3%A1rbar%C3%B0slj%C3%B3%C3%B0",
                    "http://heimskringla.no/wiki/Sk%C3%ADrnism%C3%A1l",
                    "http://heimskringla.no/wiki/V%C3%B6lundarkvi%C3%B0a",
                    "http://heimskringla.no/wiki/F%C3%A1fnism%C3%A1l",
                    "http://heimskringla.no/wiki/Sigrdr%C3%ADfum%C3%A1l",
                    "http://heimskringla.no/wiki/Helrei%C3%B0_Brynhildar",
                    "http://heimskringla.no/wiki/Dr%C3%A1p_Niflunga",

                    "http://heimskringla.no/wiki/Gu%C3%B0r%C3%BAnarkvi%C3%B0a_in_fyrsta",
                    "http://heimskringla.no/wiki/Gu%C3%B0r%C3%BAnarkvi%C3%B0a_in_forna",
                    "http://heimskringla.no/wiki/Gu%C3%B0r%C3%BAnarkvi%C3%B0a_in_%C3%BEri%C3%B0ja",
                    "http://heimskringla.no/wiki/Oddr%C3%BAnarkvi%C3%B0a",
                    "http://heimskringla.no/wiki/Atlakvi%C3%B0a",
                    "http://heimskringla.no/wiki/Atlam%C3%A1l_in_gr%C3%A6nlenzku",
                    "http://heimskringla.no/wiki/Gu%C3%B0r%C3%BAnarhv%C3%B6t",
                    "http://heimskringla.no/wiki/Ham%C3%B0ism%C3%A1l",
                    "http://heimskringla.no/wiki/Gr%C3%B3ttas%C3%B6ngr",
                    "http://heimskringla.no/wiki/Vaf%C3%BEr%C3%BA%C3%B0nism%C3%A1l",
                    "http://heimskringla.no/wiki/Hyndlulj%C3%B3%C3%B0"]


def test_text_extractor():
    text_extractor("html", "txt", os.path.join("Sæmundar-Edda", "Atlakviða"), ["complete.html"], ["complete.txt"],
                   extract_text)


def test_load_text():
    test_text_extractor()
    loader = TextLoader(os.path.join("Sæmundar-Edda", "Atlakviða"), "txt")
    print(loader.get_available_names())
    print(loader.load()[:100])


def test_voluspa():
    text_extractor("html", "txt", os.path.join("Sæmundar-Edda", "Völuspá"), ["complete.html"], ["complete.txt"],
                   extract_text)
    loader = TextLoader(os.path.join("Sæmundar-Edda", "Völuspá"), "txt")
    print(loader.get_available_names())
    print(loader.load()[:100])


if __name__ == "__main__":
    # test_text_extractor()
    # test_load_text()
    test_voluspa()
