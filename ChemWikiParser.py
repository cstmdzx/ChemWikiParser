import urllib2

# url = 'https://zh.wikipedia.org/wiki/Category:%E5%8C%96%E5%AD%A6'

url = 'https://www.google.com/'

request = urllib2.Request(url)

response = urllib2.urlopen(url)

print response.read()
