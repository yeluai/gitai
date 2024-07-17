import http.client
from urllib import request, parse


baseUrl = "www.datacups.com:80"
#baseUrl = "localhost:11434"


def send_post(url,path,data,header):#post请求函数
	conn = http.client.HTTPConnection(url)
	conn.request("POST",path,data,header)
	res = conn.getresponse()
	print(res.status,res.reason)

	data = res.read()

	print(data)

	conn.close()

data = {
        'model': 'mistral',
        'prompt':'why is the sky blue?'
    }
datas = parse.urlencode(data).encode('utf-8')
 
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}

send_post(baseUrl, path="/api/generate",data=datas,header=headers)