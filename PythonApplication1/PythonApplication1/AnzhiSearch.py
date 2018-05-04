#coding:utf-8
'''
	在安智市场上搜索应用信息
'''
from LogHandle import Logger
import HtmlGet
from bs4 import BeautifulSoup

# url = 'http://www.anzhi.com/search.php?keyword={0}'
url = 'http://www.anzhi.com/search.php'

def analyseHTML(html):
	'''
	分析html代码
	'''
	Logger.debug("analyseHTML")
	soup = BeautifulSoup(html,'lxml')


def searchAppInfo(keyword):
	'''
	关键字检索
	'''
	Logger.debug("searchAppInfo:[%s]" % keyword)
	try:
		tempUrl = url.format(keyword)
		html = HtmlGet.getSarchResult(url,{"keyword":keyword})
		# 分析html代码
		analyseHTML(html)
	except Exception as e:
		Logger.error(e)
		raise e


# 测试代码
result = searchAppInfo("微信")
Logger.debug(result) 