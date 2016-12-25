def herf_parser(html):
    # to parse link from html string
    # print 'parsered'
    list_href = list()
    return list_href

if __name__ == '__main__':
    fileHtml = open('test.html', 'r')
    lineHtml = fileHtml.readline()
    listHref = herf_parser(lineHtml)
    print listHref


