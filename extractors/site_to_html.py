from requests import get
from bs4 import BeautifulSoup

def return_html() :
    base_url="https://www.renpy.org/doc/html/"
    response=get(f"{base_url}")
    result=[]
    soup=BeautifulSoup(response.text,"html.parser")
    trees=soup.find_all('div',class_="toctree-wrapper compound")
    for tree in trees :
        a_lists=tree.find_all('li',class_="toctree-l1")
        for a_list in a_lists :
            lasts=a_list.find_all('a',class_="reference internal",recursive=False)
            for last in lasts :
                href=last['href']
                string=''+last.string.strip()
                data = {
                    'link':f"https://www.renpy.org/doc/html/{href}",
                    'index':string.replace('/',' and ')
                }
                result.append(data)
    return result