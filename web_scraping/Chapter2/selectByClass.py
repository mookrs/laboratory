from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), "html.parser")

# definitions in the BeautifulSoup documentation:
# findAll(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)

# this can use keyword instead. "class" is a protected keyword in Python.
# nameList = bsObj.findAll(class_="green")
nameList = bsObj.findAll("span", {"class": "green"}, text="the prince")
for name in nameList:
    # get_text() should always be the last thing you do.
    print(name.get_text())
