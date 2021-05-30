import requests
from bs4 import BeautifulSoup

#With a link of a Wikipedia page, it find the born date
def findBornDate(link):
    response_date=requests.get(link)
    soup= BeautifulSoup(response_date.text,features="html.parser")
    tds = soup.find('time',{'class':'nowrap date-lien bday'})#nowrap date-lien bday is the date class
    return tds['datetime']

#this function take the personnality link and use it with findBornDate(link)
def findDate(name):
    name.replace(' ','+')
    url='https://fr.wikipedia.org/w/index.php?title=Sp%C3%A9cial:Recherche&fulltext=1&search='+name+'&ns0=1'
    response=requests.get(url)
    if response.ok:
        soup= BeautifulSoup(response.text,features="html.parser")
        objet = soup.find('div',{'id':'wdsearch_container'})
        objet = soup.find('div',{'class':'mw-search-result-heading'})
        a=objet.find('a')
        link1=a['href']
        linkWikipediaPage='https://fr.wikipedia.org'+link1
        date = findBornDate(linkWikipediaPage)
        return date
    else:
        return response
