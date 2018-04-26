#coding:utf-8
from LogHandle import Logger
import urllib3
# 分析html用的库
from bs4 import BeautifulSoup

Logger.info(u'开始')

# 忽略警告：InsecureRequestWarning: UnverifiIOError: [Errno 0] Errored HTTPS request
# is being made.  Adding certificate verification is strongly advised.
# requests.packages.urllib3.disable_warnings()
# 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
http = urllib3.PoolManager()
# 通过request()方法创建一个请求：
r = http.request('GET', 'https://itunes.apple.com/cn/genre/ios-%E5%9B%BE%E4%B9%A6/id6018?mt=8')
Logger.info(r.status)  # 200
# 获得html源码,utf-8解码
                     # print(r.data.decode('gbk', 'ignore').encode('utf-8'))

# 解析html
soup = BeautifulSoup(r.data,'lxml')
# Logger.info(bs.title)

# 解析App Store
index = 0
# 获取分类列表页面的链接
classify = {}
for link in soup.select('#genre-nav a'):
	Logger.info(link.text + link.attrs['href'])
	classify[index] = {'title':link.text ,'href':link.attrs['href']}
	index+=1

# 字母顺序链接
alphabeticalOrder = {}
for alphabetical in soup.select('#selectedgenre ul')[0].select('a'):
	Logger.info(alphabetical.text + alphabetical.attrs['href'])
	alphabeticalOrder[alphabetical.text] = {'title':alphabetical.text ,'href':alphabetical.attrs['href']}
	#index+=1

# 翻页链接


# app详情页面链接
for info in soup.select('#selectedcontent a'):
	Logger.info(info.text + info.attrs['href'])

index=0

## 使用urllib2.open()方法发送请求,并返回服务器响应的类文件对象
#request = urllib2.Request('http://www.baidu.com')
## 类文件对象支持文件对象操作方法,如read()方法读取返回文件对象的全部内容并将其转换成字符串格式并赋值给html变量
#response = urllib2.urlopen(request)

## 打印html变量,即可显示出整个页面
#html = response.read()
#Logger.info(html)
## print(html)
## 解析html
#bs=BeautifulSoup(html,'lxml')
#print bs.title
def getHtml(url):
	'''
	获取指定网址的html代码
	'''
	pass