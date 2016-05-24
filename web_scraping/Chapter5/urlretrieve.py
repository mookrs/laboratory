from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
urlretrieve(imageLocation, "logo.jpg")
