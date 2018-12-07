#coding:utf-8
'''
	获取查询结果的网页
'''
from LogHandle import Logger
import certifi
import urllib3
from bs4 import BeautifulSoup

waitSecond = 120
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

def getSarchResult(url, fields):
	Logger.debug("getSarchResult:[%s]" % url)
	# url转码
	headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
		"Connection": "keep-alive",
		"Cookie": "session_uuid=e6bab52f-a8a5-46a8-b0a6-3fdff3fc8bf0; pgv_pvid=3694994030; pac_uid=0_d87afe20b4a44; pgv_pvi=8890576896; tvfe_boss_uuid=4621a8bb8863e54b; ts_refer=android.myapp.com/myapp/search.htm; ts_uid=5264357848; pgv_si=s5172048896; pgv_info=ssid=s3366122330; sjqqcomUV=sjqqcomUV; JSESSIONID=aaaYSyWNTSpbPaNSa3Pmw; ts_last=sj.qq.com/myapp/search.htm",
		"Host": "sj.qq.com",
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}
	# response = http.request('GET',url, fields=fields, headers=headers)
	response = http.request('GET',url, fields=fields)
	# response = http.request('GET','http://sj.qq.com/myapp/searchAjax.htm?kw=微信&pns=&sid=')
	while(True):
		if(response.status == 200):
			return response.data
		else:
			Logger.warning("网络错误:[%s]" % response.status)
			Logger.info("等待:[%s]秒后重试" % waitSecond)
			time.sleep(waitSecond)