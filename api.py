import urllib.request
import bs4 as bs

url = 'https://www.sogral.dz/index.php/fr/nos-agences'

sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce, 'html.parser')


def extractLinks():
    Links = soup.findAll("a", {"class": "bt-title"})
    linkList = []
    for Link in Links:
        linkList.append(f"https://www.sogral.dz{Link.get('href')}")

    del linkList[0]
    return linkList


def extractData(link):

    url = 'https://www.sogral.dz/index.php/fr/nos-agences/28-nos-agences/124-el-oued-2'

    sauce = urllib.request.urlopen(link).read()
    soup = bs.BeautifulSoup(sauce, 'html.parser')

    data = soup.findAll("li")
    del data[0:26]
    del data[9:]
    temp = []
    for item in data:
        temp.append(item.text.split(':'))

    return temp


listL = extractLinks()

for link in listL:
    print(link.encode('utf-8').strip())
    for item in extractData(link):
        print(item)


'''
for item in extractData():
    print(f'{item[0]} : {item[1]}')
'''
