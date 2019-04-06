from bs4 import BeautifulSoup
import urllib.request
import os
import time

def getlink(name):
    print("here")
    nextsearch = None
    soup = BeautifulSoup(open(f"downloads/{name}", 'r').read() , 'html.parser')
    print(soup.find_all('a'))
    for link in soup.find_all('a'):
        print(link)
        print("start")
        if link.get_text().find('tune page') == 0:
            print("tune")
            collection.append("tune" + str(x) + ".html")
            time.sleep(5)
            downloadthis(domain + link.get('href'), "downloads", "tune" + str(x))
            x = x+1
            # completetext.append(songcatcher(domain + link.get('href')))
        if link.get_text() == "next":
            print("next")
            # y = y + 1
            furl = "index" + str(y) + ".html"
            downloadthis(domain + link.get('href'), "downloads", "index" + str(y))
            time.sleep(5)
            getlink(furl)
    print(collection)


def downloadthis(url, folder=".", name="error"):
    file = name + ".html"
    path = os.path.join(folder, file)
    print(path)
    if os.path.exists(path):
        return
    urllib.request.urlretrieve(url, path)
    print("complete")

def songcatcher(name):
    soup = BeautifulSoup(open(f"downloads/{name}", 'r').read() , 'html.parser')
    soug.find("textarea")
    soup.contents[0].strip()
    return soup

y = 0
x = 0
collection = []
completetext = []
domain = "http://abcnotation.com"
url = "http://abcnotation.com/searchTunes?q=country&f=c&o=a&s=0"

downloadthis(url, "downloads", "index" + str(y))
getlink("index0.html")

save=open(f"complete.abc", "a")
for all in collection:
    save.write(songcatcher(all) + "\n")
save.close()

print(completetext)
