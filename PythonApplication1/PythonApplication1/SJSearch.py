#coding:utf-8
'''
	在应用宝上搜索应用信息
'''
from LogHandle import Logger
import HtmlGet
from bs4 import BeautifulSoup

# url = 'http://android.myapp.com/myapp/search.htm?kw={0}'
# url = 'http://android.myapp.com/myapp/search.htm'
# url = 'http://sj.qq.com/myapp/search.htm'
url = 'http://sj.qq.com/myapp/searchAjax.htm?kw=微信&pns=&sid='

def analyseHTML(html):
	'''
	分析html代码
	'''
	Logger.debug("analyseHTML")
	soup = BeautifulSoup(html,'lxml')
	#查询结果列表J_SearchDefaultListBox
	for info in soup.select('#J_SearchDefaultListBox li'):
		# 查找详细页面的链接
		detailLink = info.select("a[class='icon']")
		pass


def searchAppInfo(kw):
	'''
	关键字检索
	'''
	Logger.debug("searchAppInfo:[%s]" % kw)
	try:
		tempUrl = url.format(kw)
		html = HtmlGet.getSarchResult(url, {"kw":kw})
		# 分析html代码
		analyseHTML(html)
	except Exception as e:
		Logger.error(e)
		raise e

# 测试代码
result = searchAppInfo("")
Logger.debug(result) 