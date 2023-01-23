from requests import get
from bs4 import BeautifulSoup

def get_sublinks(url):
    response=requests.get(f"{url}")
    soup=BeautifulSoup(response.text,"html.parser")
    atags=soup.find_all('a')
    sublinks = [a['href'] for a in filter(atags,lambda a:a.get('href')!=None)]
    return sublinks


def get_linked_pages(url, ftr_f=None):
    sublinks = [url]
    ll = sublinks
    while ll:
        l = ll.pop()
        ss = get_sublinks(l)
        for s in ss if s not in sublinks:
            sublinks.append(s)
            ll.append(s)
    if ftr_f:
        sublinks = list(filter(sublinks, ftr_f))
    return sublinks


def find_text_location(soup):
    last =soup.find('div',class_="col-md-9 content")
    sections=last.find_all('div',class_="section")
    return sections


def get_main_text(link):
    response=requests.get(link)
    soup=BeautifulSoup(response.text,"html.parser")
    sections = find_text_location(soup)
    ttt = list()
    for section in sections :
        s=section.get_text()
        s=s.replace("link","")
        ttt.append(string)
    return ttt


def write_file(file_name, text):
    file = open(f"{file_name}.txt",'w',encoding='utf-8-sig')
    for line in text :
        file.write(f"{line}\n")
    file.close()
    return