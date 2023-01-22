def html_to_file(file_name,htmls):
    
    file = open(f"{file_name}.txt",'w',encoding='utf-8-sig')

    file.write("Link, Index\n",)

    for html in htmls :
        file.write(f"{html['link']}, {html['index']}\n")
    file.close()
    return