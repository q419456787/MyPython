import urllib.request
import os
#直接返回url的地址
def getResponse(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
    html=urllib.request.urlopen(req)
    html=html.read()
    return html

#传输的是该网页的当前的response
def get_currentNum(url):
    html=getResponse(url).decode('utf-8')
    a=html.find('current-comment-page')+23
    b=html.find(']',a,a+255)
    print('当前开始页面找到的是%s'%html[a:b])
    return html[a:b]


#获取当前页面的所有图片的地址 返回一个列表然后保存
def getImgAddr(url):
    html=getResponse(url)
    html=html.decode('utf-8')
    imgaddrlist=[]
    a=html.find('img src')
    while a!=-1:
        b=html.find('.jpg',a,a+255)
        if(b!=-1):
            print(html[a+9:b+4])
            imgaddrlist.append(html[a+9:b+4])
        a=html.find('img src',b+9)

    for i in imgaddrlist:
            print(i)

    return  imgaddrlist


#参数需要传输 图片地址列表, 保存的路径
def saveImg(imgaddr,folder='OOXX'):
    try:
        os.mkdir(folder)
    except:
        print('文件夹%s已经存在'%folder)

    os.chdir(folder)

    for item in imgaddr:
        response=getResponse(item)
        fileName=item.split('/')[-1]
        with open(fileName,mode='wb') as f:
            f.write(response)


def downloadmm(url='http://jandan.net/ooxx',pages=10):
    response=getResponse(url)

    currentNum=int(get_currentNum(url))

    for i in range(pages):
        currenturl=url+'/page-'+str(currentNum-i)+'#comments'
        print(currenturl)
        imgaddr_list=getImgAddr(currenturl)
        saveImg(imgaddr_list)


if __name__=='__main__':
    html=getResponse('http://jandan.net/ooxx').decode('utf-8')
    print(html)
    #downloadmm(pages=2)

