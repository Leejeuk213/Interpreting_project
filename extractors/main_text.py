from requests import get
from bs4 import BeautifulSoup

def return_main_text(htmls):
    for html in htmls :
        response=get(f"{html['link']}")
        soup=BeautifulSoup(response.text,"html.parser")
        last =soup.find('div',class_="col-md-9 content")
        sections=last.find_all('div',class_="section")
        for section in sections :
            string=section.get_text()
            string=string.replace("link","")
            file_name=f"{html['index']}.txt"
            file = open(f'text_result/{file_name}','a',encoding='utf-8')
            print(string,file=file)
            file.close()
    return