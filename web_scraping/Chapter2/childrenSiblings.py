from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

# If you were to write it using the `descendants()` function instead of the
# `children()` function, about two dozen tags would be found within the
# table and printed, including `img` tags, `span` tags, and individual `td`
# tags.
for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)

print("----------")

# by selecting the title row and calling next_siblings, we can select all
# the rows in the table
for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

print("----------")

print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
