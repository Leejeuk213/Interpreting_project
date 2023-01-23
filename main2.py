from html import parser
from html import hirarchy
from html import filtering_func as ff


if __name__ == "__main__":
	base_url = "https://www.renpy.org/doc/html"
	links = parser.get_linked_pages(base_url, ftr_f=ff.sublink(base_url))
	#hir = hirarchy.get_hirarchy(links)
	#parser.html_to_file(base_url, hir)
	parser.wrtie_file(base_url, links)
	for link in links:
		texts = parser.get_main_text(link)
    	file_name=link.split("/")[-1]  	
    	wrtie_file(f'text/{file_name}', texts)

