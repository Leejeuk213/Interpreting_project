from requests import get
from bs4 import BeautifulSoup

def return_main_text(htmls):
    for html in htmls :
        response=get(f"{html['link']}")
        soup=BeautifulSoup(response.text,"html.parser")
        last =soup.find('div',class_="col-md-9 content")
        sections=last.find_all('div',class_="section")
        result=[]
        for section in sections :
            string=section.get_text()
            string=string.replace("link","")
            result.append(string)
        file_name=f"{html['index']}.txt"
        file = open(f'text_result/{file_name}','w',encoding='utf-8')
        for string in result :
            print(string,file=file)
        file.close()
    return