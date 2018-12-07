#coding:utf-8
'''
	在应用宝上搜索应用信息
'''
from LogHandle import Logger
import HtmlGet
from bs4 import BeautifulSoup
import json

# url = 'http://android.myapp.com/myapp/search.htm?kw={0}'
# url = 'http://android.myapp.com/myapp/search.htm'
# url = 'http://sj.qq.com/myapp/search.htm'
# url = 'http://sj.qq.com/myapp/searchAjax.htm?kw=微信&pns=&sid='
url = 'https://sj.qq.com/myapp/searchAjax.htm'

def analyseHTML(html):
	'''
	分析html代码
	'''
	Logger.debug("analyseHTML")
	jsonObject = json.loads(html)
	for item in jsonObject[u'obj'][u'items']:
		Logger.info(item[u'appDetail'][u'appName'])
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
result = searchAppInfo("微信")
Logger.debug(result) 