# modify html to one line
# just for test

fileTest = open('test.html', 'r')
linesTest = fileTest.readlines()

strHtml = ''
for eachLineTest in linesTest:
    eachLineTest = eachLineTest.replace('\n', '')
    eachLineTest = eachLineTest.replace('\r', '')
    strHtml += eachLineTest

fileRes = open('RootUrl', 'w')
# strHtml = strHtml.replace('\n', '')
# strHtml = strHtml.replace('\r', '')
# strHtml.rstrip('')
print strHtml
fileRes.write(strHtml)


