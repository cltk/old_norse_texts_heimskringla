from bs4 import BeautifulSoup
import codecs
sites = ["http://heimskringla.no/wiki/Sk%C3%A1ldskaparm%C3%A1l", "http://heimskringla.no/wiki/Prologus",
         "http://heimskringla.no/wiki/H%C3%A1ttatal", "http://heimskringla.no/wiki/Gylfaginning",
         "http://heimskringla.no/wiki/Edda_Snorra_Sturlusonar"]
for filename in ["gylfaginning.html", "haattatal.html", "prologus.html", "skaaldskaparmaal.html"]:
    with open(filename, "r") as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        print(soup.get_text())


with codecs.open("gylfaginning.html", "r", "utf8") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    print(soup.get_text())
