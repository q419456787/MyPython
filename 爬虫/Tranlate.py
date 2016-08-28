import urllib.request
import urllib.parse
import time
while True:
    content=input('请输入需要翻译的东西(输入"q!"退出程序)')
    if(content=='q!'):
        break
    data={}
    data['from']='en'
    data['to']='zh'
    data['query']=content
    data['simple_means_flag']='3'

    url='http://fanyi.baidu.com/v2transapi'

    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    data=urllib.parse.urlencode(data).encode('utf-8')

    req=urllib.request.Request(url,data,head)
    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')


    import  json
    res=json.loads(html)



    print("翻译结果为%s" % res['dict_result']['simple_means']['symbols'][0]['parts'][0]['means'])

    time.sleep(5)
