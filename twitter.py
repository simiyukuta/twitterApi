import urllib
import urllib2,cookielib
from bs4 import BeautifulSoup
import sys

class roboti:
	def getOpener(self):
		cj=cookielib.CookieJar()
		opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.149 Safari/537.36')]
		return opener
		
		
	def login(self,username,password,opener):
		url='https://twitter.com/login'
		#find token
		find_tk=opener.open(url)
		tk=find_tk.read()
		soup=BeautifulSoup(tk)
		resp=soup.find_all('input',limit=7)
		auth_token=resp[5]
		auth_dict=auth_token.attrs
		token=auth_dict['value']
		url='https://twitter.com/sessions'
		params=urllib.urlencode({'session[username_or_email]':username,'session[password]':password,'authenticity_token':token,'scribe_log':'','redirect_after_login':'','authenticity_token':token})
		resp=opener.open(url,params)
		response=resp.read()
		#soup=BeautifulSoup(response)
		#title='Welcome to twitter'
		#message='Hello world,it feels nice to do this.'
		#response=self.postMessage(title,message,opener)
		return response
		
	def postMessage(self,status,opener):
		token_url='https://twitter.com/'
		opener.addheaders = [('Referer', 'https://twitter.com/')]
		opener.addheaders = [('origin', 'https://twitter.com/')]
		opener.addheaders = [('x-requested-with', 'XMLHttpRequest')]
		the_html=opener.open(token_url)
		the_txt=the_html.read()
		soup=BeautifulSoup(the_txt)
		resp=soup.find_all('input',limit=3)
		auth_token=resp[2]
		auth_dict=auth_token.attrs
		token=auth_dict['value']
		url='https://twitter.com/i/tweet/create'
		params=urllib.urlencode({'authenticity_token':token,'place_id':'','status':status})
		resp=opener.open(url,params)
		return resp
#get the arguments and convert the list to a string
status=' '.join(sys.argv[1:])
#status="the bug is that I am failing to simulate a real human environment for the robot,ah it worked"
robot=roboti()
opener=robot.getOpener()
username='yourusername'
password='yourpassword'
robot.login(username,password,opener)
resp=robot.postMessage(status,opener)
print resp


