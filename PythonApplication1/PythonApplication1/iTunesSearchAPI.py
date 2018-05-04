#coding:utf-8
'''
	在iTunes搜索应用信息
'''
from LogHandle import Logger
import HtmlGet
import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# url =
# 'https://itunes.apple.com/search?country=CN&entity=software&limit=5&term={0}'
url = 'https://itunes.apple.com/search'

def analyseJSON(html):
	'''
	分析json代码
	'''
	Logger.debug("analyseJSON")
	result = {}
	jsonObject = json.loads(html)
	if(jsonObject["resultCount"] == 0):
		#没有找到app信息
		Logger.warning("没有找到app信息,关键字:[%s]" % term)
	else:
		# 获取app信息
		# 类别，数组
		Logger.debug("类别:[%s]" % jsonObject["results"][0]["genres"])
		result["genres"] = jsonObject["results"][0]["genres"]
		# 开发企业
		Logger.debug("开发企业:[%s]" % jsonObject["results"][0]["sellerName"])
		result["developer"] = jsonObject["results"][0]["sellerName"]
		# 功能介绍
		Logger.debug("功能介绍:[%s]" % jsonObject["results"][0]["description"])
		result["description"] = jsonObject["results"][0]["description"]
		# bundleId
		Logger.debug("bundleId:[%s]" % jsonObject["results"][0]["bundleId"])
		result["id"] = jsonObject["results"][0]["bundleId"]
	return result

def searchAppInfo(term):
	'''
	根据关键字查找app信息
	'''
	Logger.debug("searchAppInfo:[%s]" % term)
	try:
		tempUrl = url.format(term)
		html = HtmlGet.getSarchResult(url, {"country":"CN", "entity":"software", "limit":"5", "term":term})
		return analyseJSON(html)
	except Exception as e:
		Logger.error(e)
		raise e

# 测试代码
result = searchAppInfo("微信")
Logger.debug(result) 