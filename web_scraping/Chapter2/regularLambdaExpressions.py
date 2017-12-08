from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
images = bsObj.findAll(
    "img", {"src": re.compile("\.\./img/gifts/img.*\.jpg")})
for image in images:
    print(image.attrs["src"])

html = urlopen("http://www.pythonscraping.com/pages/page2.html")
bsObj = BeautifulSoup(html, "html.parser")
tags = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
for tag in tags:
    print(tag)
