import urllib2
import urllib
import httplib

apikey = 'RJ2t5qoOD6pfM4EWJex40'
#userid = 'A0131282'
#password = 'B7a8281828?'
url = 'https://ivle.nus.edu.sg/api/login/?apikey={}&url='.format(apikey)

#Generate POST information table
def postDict(userid,password):
	postdata ={'__LASTFOCUS':'',
'__EVENTTARGET':'',
'__EVENTARGUMENT':'',
'__VIEWSTATE':'/wEPDwULLTEzODMyMDQxNjEPFgIeE1ZhbGlkYXRlUmVxdWVzdE1vZGUCARYCAgEPZBYEAgEPD2QWAh4Gb25ibHVyBQ91c2VySWRUb1VwcGVyKClkAgkPD2QWBB4Lb25tb3VzZW92ZXIFNWRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdsb2dpbmltZzEnKS5zcmM9b2ZmaW1nLnNyYzE7Hgpvbm1vdXNlb3V0BTRkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnbG9naW5pbWcxJykuc3JjPW9uaW1nLnNyYzE7ZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQUJbG9naW5pbWcxYTg4Q/LO3lNCB13iJpTeINmF1JQmGv61ni1TVgDIOII=',
'__VIEWSTATEGENERATOR':'B0AF59B8',
'__SCROLLPOSITIONX':0,
'__SCROLLPOSITIONY':0,
'userid':userid,
'password':password,
'loginimg1.x':22,
'loginimg1.y':19}
	return postdata

#header
header = {'Host':'ivle.nus.edu.sg',
'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language':'en-US,en;q=0.5',
'Accept-Encoding':'gzip, deflate, br',
'Referer':'https://ivle.nus.edu.sg/api/login/?apikey=RJ2t5qoOD6pfM4EWJex40&url=datinker.com',
'Cookie':'_ga=GA1.3.2110009064.1450372795; __utma=145952555.2110009064.1450372795.1450372797.1458046625.2; __utmz=145952555.1450372797.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ASP.NET_SessionId=0vsok0bisqazsg3s013lxggl',
'Connection':'keep-alive'}

#obtain user-specific auth_token
def obtain_token(userid,password):
	data = urllib.urlencode(postDict(userid,password))
	request = urllib2.Request(url,data,header)
	try:	
		response = urllib2.urlopen(request)
		token = response.read()
	except urllib2.HTTPError as e:
		print 'Error: ',e.code
	return token

#retrieve json for timetable
def retrieve_timetable(userid,password):
	token = obtain_token(userid,password)
	timetable_url = 'https://ivle.nus.edu.sg/api/Lapi.svc/Timetable_Student?APIKey={}&AuthToken={}&AcadYear={}&Semester={}'.format(apikey,token,'2015/2016',2)
	request = urllib2.Request(timetable_url)
	try:
		response = urllib2.urlopen(request)
	except urllib2.HTTPError as e:
		print "Error: ",e.code
	return response.read()
