#coding:utf-8
from LogHandle import Logger
import urllib3
from bs4 import BeautifulSoup
from urlparse import *

filename='D:\\03_work\\20180420\\PythonApplication1\\PythonApplication1\\data.csv'
url = 'https://itunes.apple.com/cn/genre/ios-{0}/id{1}?mt=8&letter={2}&page={3}#page'
category = {
	6000:{ 'key':6000, 'name':'商务'},
	6001:{ 'key':6001, 'name':'天气'},
	6002:{ 'key':6002, 'name':'工具'},
	6003:{ 'key':6003, 'name':'旅游'},
	6004:{ 'key':6004, 'name':'体育'},
	6005:{ 'key':6005, 'name':'社交'},
	6006:{ 'key':6006, 'name':'参考'},
	6007:{ 'key':6007, 'name':'效率'},
	6008:{ 'key':6008, 'name':'摄影与录像'},
	6009:{ 'key':6009, 'name':'新闻'},
	6010:{ 'key':6010, 'name':'导航'},
	6011:{ 'key':6011, 'name':'音乐'},
	6012:{ 'key':6012, 'name':'生活'},
	6013:{ 'key':6013, 'name':'健康健美'},
	6014:{ 'key':6014, 'name':'游戏', 'categorys':{
			7001:{'key':7001,'name':'动作游戏'},
			7002:{'key':7002,'name':'冒险游戏'},
			7003:{'key':7003,'name':'街机游戏'},
			7004:{'key':7004,'name':'桌面游戏'},
			7005:{'key':7005,'name':'卡牌游戏'},
			7006:{'key':7006,'name':'娱乐场游戏'},
			7007:{'key':7007,'name':'骰子游戏'},
			7008:{'key':7008,'name':'教育类游戏'},
			7009:{'key':7009,'name':'聚会游戏'},
			7011:{'key':7011,'name':'音乐'},
			7012:{'key':7012,'name':'益智解谜'},
			7013:{'key':7013,'name':'竞速游戏'},
			7014:{'key':7014,'name':'角色扮演游戏'},
			7015:{'key':7015,'name':'模拟游戏'},
			7016:{'key':7016,'name':'体育'},
			7017:{'key':7017,'name':'策略游戏'},
			7018:{'key':7018,'name':'问答游戏'},
			7019:{'key':7019,'name':'文字游戏'}
		}},
	6015:{ 'key':6015, 'name':'财务'},
	6016:{ 'key':6016, 'name':'娱乐'},
	6017:{ 'key':6017, 'name':'教育'},
	6018:{ 'key':6018, 'name':'图书'},
	6020:{ 'key':6020, 'name':'医疗'},
	6021:{ 'key':6021, 'name':'报刊杂志', 'categorys':{
			13001:{'key':13001,'name':'新闻及政治'},
			13002:{'key':13002,'name':'流行与时尚 '},
			13003:{'key':13003,'name':'家居与园艺'},
			13004:{'key':13004,'name':'户外与自然'},
			13005:{'key':13005,'name':'运动与休闲'},
			13006:{'key':13006,'name':'汽车'},
			13007:{'key':13007,'name':'艺术与摄影'},
			13008:{'key':13008,'name':'新娘与婚礼'},
			13009:{'key':13009,'name':'商务与投资'},
			13010:{'key':13010,'name':'儿童杂志'},
			13011:{'key':13011,'name':'电脑与网络'},
			13012:{'key':13012,'name':'烹饪与饮食'},
			13013:{'key':13013,'name':'手工艺与爱好'},
			13014:{'key':13014,'name':'电子产品与音响'},
			13015:{'key':13015,'name':'娱乐'},
			13017:{'key':13017,'name':'心理与生理'},
			13018:{'key':13018,'name':'历史'},
			13019:{'key':13019,'name':'文学杂志与期刊'},
			13020:{'key':13020,'name':'男士兴趣'},
			13021:{'key':13021,'name':'电影与音乐'},
			13023:{'key':13023,'name':'子女教养与家庭'},
			13024:{'key':13024,'name':'宠物'},
			13025:{'key':13025,'name':'职业与技能'},
			13026:{'key':13026,'name':'地方新闻'},
			13027:{'key':13027,'name':'科学'},
			13028:{'key':13028,'name':'青少年'},
			13029:{'key':13029,'name':'旅游与地域'},
			13030:{'key':13030,'name':'女士兴趣'}
		}},
	6022:{ 'key':6022, 'name':'商品指南'},
	6023:{ 'key':6023, 'name':'美食佳饮'},
	6024:{ 'key':6024, 'name':'购物'},
	6025:{ 'key':6025, 'name':'贴纸', 'categorys':{
			16001:{'key':16001,'name':'表情与用语'},
			16003:{'key':16003,'name':'动物与自然'},
			16005:{'key':16005,'name':'艺术 '},
			16006:{'key':16006,'name':'节庆'},
			16007:{'key':16007,'name':'名人明星'},
			16008:{'key':16008,'name':'卡通动漫'},
			16009:{'key':16009,'name':'饮食'},
			16010:{'key':16010,'name':'游戏'},
			16026:{'key':16026,'name':'时尚'},
			16014:{'key':16014,'name':'影视'},
			16015:{'key':16015,'name':'音乐'},
			16017:{'key':16017,'name':'人物'},
			16019:{'key':16019,'name':'地点与物品'},
			16021:{'key':16021,'name':'体育与活动'},
			16025:{'key':16025,'name':'儿童与家庭'}
		}}}

http = urllib3.PoolManager()

for key in category:
	tempUrl = ''
	id = 0
	str1 = ''
	page=1
	appid=''
	if(category[key].has_key('categorys')):
		# 含有子分类
		for keyChild in category[key]['categorys']:
			str1 = category[key]['name'] + '-' + category[key]['categorys'][keyChild]['name']
			id = keyChild
			# 每个Key对应26个字母
			for letter in range(65,91):
				# 页号，循环加1，直到页码返回404
				# TODO 预防断网404重试多次
				while(True):
					if(letter==91):
						tempUrl = url.format(str1,id,'*',page)
					else:
						tempUrl = url.format(str1,id,chr(letter),page)
					page+=1;
					#
					response = http.request('GET',tempUrl)
					Logger.info("%s:%d"%(tempUrl,response.status))
					if(response.status==200):
						appid=''
						Logger.info("%s:%d"%(tempUrl,response.status))
						# 获取链接
						soup = BeautifulSoup(response.data,'lxml')
						for info in soup.select('#selectedcontent a'):
							result = urlparse(info.attrs['href'])
							array=result.path.split('/')
							appid=array[len(array)-1].replace('id','')
							with open(filename,'a+') as f:
								f.write("%s,%s,%s\n" % (info.text,appid,info.attrs['href']))
						if(appid==''):
							page=1
							break
					else:
						Logger.warning("%s:%d"%(tempUrl,response.status))
						page=1
						break
	else:
		# 不含子分类
		str1 = category[key]['name']
		id = key
		# 每个Key对应26个字母
		for letter in range(65,91):
			# 页号，循环加1，直到页码返回404
			# TODO 预防断网404重试多次
			while(True):
				if(letter==91):
					tempUrl = url.format(str1,id,'*',page)
				else:
					tempUrl = url.format(str1,id,chr(letter),page)
				page+=1;
				#
				response = http.request('GET',tempUrl)
				if(response.status==200):
					appid=''
					Logger.info("%s:%d"%(tempUrl,response.status))
					# 获取链接
					soup = BeautifulSoup(response.data,'lxml')
					for info in soup.select('#selectedcontent a'):
						result = urlparse(info.attrs['href'])
						array=result.path.split('/')
						appid=array[len(array)-1].replace('id','')
						with open(filename,'a+') as f:
							f.write("%s,%s,%s\n" % (info.text.encode('utf-8'),appid,info.attrs['href']))
					if(appid==''):
						page=1
						break
				else:
					Logger.warning("%s:%d"%(tempUrl,response.status))
					page=1
					break

