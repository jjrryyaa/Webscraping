from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.request import Request
from bs4 import BeautifulSoup


def openURL(url):
    try:
        req = Request(url, headers = {"User-Agent": "Mozilla/5.0"})
        html = urlopen(req)
    except HTTPError as e:
        print("HTTP error " + str(e.code))
        return None
    return html


def getTitle(url):
    html = openURL(url)
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        print("Attribute error")
        return None
    return title




title = getTitle('http://www.pythonscraping.com/pages/page3.html')
if title == None:
    print('Title could not be found')
else:
    print(title)

