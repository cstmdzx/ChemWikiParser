# -*- coding:UTF-8 -*-
import re

# category pattern <a class="CategoryTreeLabel  CategoryTreeLabelNs14 CategoryTreeLabelCategory" href="/wiki/Category:%E5%8C%96%E5%AD%A6%E5%B0%8F%E4%BD%9C%E5%93%81">化学小作品</a>

# page pattern

patternCategory = re.compile(r'<a class=\"CategoryTreeLabel  CategoryTreeLabelNs14 CategoryTreeLabelCategory\" href=\"(.+?)\">(.+?)</a>')

patternPage = re.compile(r'<li><a href=\"(.+?)\" title=\"(.+?)\">(.+?)</a></li>')

filetest = open('testres', 'w')

def href_parser(html):
    # to parse link from html string
    # list_category contains the category's link and the txt
    # list_page contains the page's link, title and the txt
    list_category = patternCategory.findall(html)
    # 0.url  1.txt
    # count = 0
    '''
    for eachres in list_category:
        if eachres[0] == '':
            continue
        # print eachres[0]
        count += 1
        print eachres[1]
        print eachres[2]
        filetest.write('======================================================\n')
        filetest.write(eachres[1] + '\n')
        filetest.write('++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
        filetest.write(eachres[2] + '\n')
    '''
    list_page = patternPage.findall(html)
    # 0.url  1.title  2.txt     namely,[1] == [2]
    list_page.pop() # the last one is unuseful
    '''
    for each_ul in list_page:
        print each_ul[0]
        print each_ul[1]
    print list_category.__len__()
    print list_page.__len__()
    print count
    '''
    # list_href.extend(res[:][0])
    # print list_page
    return [list_category, list_page]

if __name__ == '__main__':
    fileHtml = open('RootUrl', 'r')
    lineHtml = fileHtml.readline()
    [listCategory, listPage] = href_parser(lineHtml)
    print listCategory.__len__()
    print listPage.__len__()
    #print listHref


