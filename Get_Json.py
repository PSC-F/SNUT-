
import urllib.parse
import requests
def dictget(dict1,obj):#嵌套字典中取目标值
   for k,v in dict1.items():
    if k == obj:
      return v
    elif type(v) is dict:
        ret= dictget(v,obj)
        if ret is not None:
         return ret
def get_body_attr(image,type):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"
    access_token = '24.31b9f9e9c2f2f68c9f5d8274400f3f6c.2592000.1548737227.282335-14499358'
    request_url = request_url + "?access_token=" + access_token
    header = {'Content-Type': 'application/x-www-form-urlencoded'}#, 'Connectio24.1ced36a63e943a61703ea34b37b1f608.2592000.1545295455.282335-14499358n': 'Keep-Alive'
    params = {'image':image,'type':type}
    urllib.parse.urlencode(params)
    request=requests.post(url=request_url, data=params, headers=header)
    print('人体属性响应'+str(request.elapsed.total_seconds())+'s')
    return request.text

def get_body_num(img,area,Show_F,Session):
    """img：解码后的值，Show_F ：第一次真第二次假 area：例"10,650,1910,650,1910,1070,10,1070"Session：第一次真第二次假"""
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_tracking"
    access_token = '24.31b9f9e9c2f2f68c9f5d8274400f3f6c.2592000.1548737227.282335-14499358'
    #header = {'Content-Type': 'application/x-www-form-urlencoded'}
    request_url = request_url + "?access_token=" + access_token
    params = {"dynamic": 'True', "case_id": 100, "case_init": Show_F, "image": img, 'show': 'true',
              "area": area}
    urllib.parse.urlencode(params)
    if Session ==True:
       httpsession = requests.session()
       request = httpsession.post(url=request_url, data=params)
       print(request.text)
       print('人流接口响应：' + str(request.elapsed.total_seconds()) + 's')
       return request.text
    else:
        request = requests.post(url=request_url, data=params)
        print(request.text)
        print('人流接口响应：'+str(request.elapsed.total_seconds())+'s')
    return request.text

import urllib.parse
import requests
def dictget(dict1,obj):#嵌套字典中取目标值
   for k,v in dict1.items():
    if k == obj:
      return v
    elif type(v) is dict:
        ret= dictget(v,obj)
        if ret is not None:
         return ret
def get_body_attr(image,type):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"
    access_token = '24.31b9f9e9c2f2f68c9f5d8274400f3f6c.2592000.1548737227.282335-14499358'
    request_url = request_url + "?access_token=" + access_token
    header = {'Content-Type': 'application/x-www-form-urlencoded'}#, 'Connectio24.1ced36a63e943a61703ea34b37b1f608.2592000.1545295455.282335-14499358n': 'Keep-Alive'
    params = {'image':image,'type':type}
    urllib.parse.urlencode(params)
    request=requests.post(url=request_url, data=params, headers=header)
    print('人体属性响应'+str(request.elapsed.total_seconds())+'s')
    return request.text

def get_body_num(img,area,Show_F,Session):
    """img：解码后的值，Show_F ：第一次真第二次假 area：例"10,650,1910,650,1910,1070,10,1070"Session：第一次真第二次假"""
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_tracking"
    access_token = '24.31b9f9e9c2f2f68c9f5d8274400f3f6c.2592000.1548737227.282335-14499358'
    #header = {'Content-Type': 'application/x-www-form-urlencoded'}
    request_url = request_url + "?access_token=" + access_token
    params = {"dynamic": 'True', "case_id": 100, "case_init": Show_F, "image": img, 'show': 'true',
              "area": area}
    urllib.parse.urlencode(params)
    if Session ==True:
       httpsession = requests.session()
       request = httpsession.post(url=request_url, data=params)
       print(request.text)
       print('人流接口响应：' + str(request.elapsed.total_seconds()) + 's')
       return request.text
    else:
        request = requests.post(url=request_url, data=params)
        print(request.text)
        print('人流接口响应：'+str(request.elapsed.total_seconds())+'s')
    return request.text

import urllib.parse
import requests
def dictget(dict1,obj):#嵌套字典中取目标值
   for k,v in dict1.items():
    if k == obj:
      return v
    elif type(v) is dict:
        ret= dictget(v,obj)
        if ret is not None:
         return ret
def get_body_attr(image,type):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"
    access_token = '24.31b9f9e9c2f2f68c9f5d8274400f3f6c.2592000.1548737227.282335-14499358'
    request_url = request_url + "?access_token=" + access_token
    header = {'Content-Type': 'application/x-www-form-urlencoded'}#, 'Connectio24.1ced36a63e943a61703ea34b37b1f608.2592000.1545295455.282335-14499358n': 'Keep-Alive'
    params = {'image':image,'type':type}
    urllib.parse.urlencode(params)
    request=requests.post(url=request_url, data=params, headers=header)
    print('人体属性响应'+str(request.elapsed.total_seconds())+'s')
    return request.text

def get_body_num(img,area,Show_F,Session):
    """img：解码后的值，Show_F ：第一次真第二次假 area：例"10,650,1910,650,1910,1070,10,1070"Session：第一次真第二次假"""
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_tracking"
    access_token = '24.31b9f9e9c2f2f68c9f5d8274400f3f6c.2592000.1548737227.282335-14499358'
    #header = {'Content-Type': 'application/x-www-form-urlencoded'}
    request_url = request_url + "?access_token=" + access_token
    params = {"dynamic": 'True', "case_id": 100, "case_init": Show_F, "image": img, 'show': 'true',
              "area": area}
    urllib.parse.urlencode(params)
    if Session ==True:
       httpsession = requests.session()
       request = httpsession.post(url=request_url, data=params)
       print(request.text)
       print('人流接口响应：' + str(request.elapsed.total_seconds()) + 's')
       return request.text
    else:
        request = requests.post(url=request_url, data=params)
        print(request.text)
        print('人流接口响应：'+str(request.elapsed.total_seconds())+'s')
    return request.text
