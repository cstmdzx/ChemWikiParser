import urllib
import urllib2

# url = 'https://www.baidu.com'
# url = 'https://www.google.com/'
url = 'https://zh.wikipedia.org/wiki/Category:%E5%8C%96%E5%AD%A6'
# url = 'https://en.wikipedia.org/wiki/Main_Page'
# url = 'http://baike.baidu.com/item/%E6%89%8B%E5%A5%97/1690692'
# url = 'https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5'
#url = 'http://www.bbc.com/'
# url = 'http://sucre.blog.51cto.com/1084905/270556'

# url = 'https://zh.wikipedia.org/wiki/%E5%A4%A7%E8%A5%BF%E6%B4%8B%E9%A2%B6%E9%A2%A8%E5%AD%A3'
url = 'http://baike.baidu.com/item/%E7%BD%91%E7%BA%A6%E8%BD%A6'

requesthead = {
'Host':'baike.baidu.com',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding':'gzip, deflate',
'Connection':'keep-alive',
'Cookie':'TBLkisOn=0; WMF-Last-Access=22-Dec-2016; CP=H2; GeoIP=US:DE:Wilmington:39.75:-75.55:v4; zhwikimwuser-sessionId=0b5c9cf6fdc94e8d',
'Cache-Control':'max-age=0',
'Referer':None}

#proxy = {'http':'192.168.190.201:1080'}
#proxy_support = urllib2.ProxyHandler(proxy)
#opener = urllib2.build_opener(proxy_support)
#urllib2.install_opener(opener)

print url
request = urllib2.Request(url, headers = requesthead)

response = urllib2.urlopen(request)

print response.read()
