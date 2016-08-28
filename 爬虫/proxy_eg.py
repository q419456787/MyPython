import  urllib.request
import  random

#还可以定义个ip列表自己去搜
iplist=['','']

url='http://www.whatismyip.com.tw/'

#先定义一个代理
proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})

#创建一个opener 来代理
opener=urllib.request.build_opener(proxy_support)

opener.addheaders=[('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')]
#注入这个opener

urllib.request.install_opener(opener)

response=urllib.request.urlopen(url)

html=response.read().decode('utf-8')

print(html)