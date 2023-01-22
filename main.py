from requests import get
from bs4 import BeautifulSoup
from extractors.site_to_html import return_html
from extractors.file import html_to_file
from extractors.main_text import return_main_text
htmls=return_html()
html_to_file("Renpy_html",htmls)
texts=return_main_text(htmls)