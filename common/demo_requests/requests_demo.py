import requests, json

'''
get方法 
requests.get(url,params=,**kwargs)
url:api路径
params：url中的额外参数，字典或字节流
**kwargs：12个控制访问的参数，requests中除params的参数（headers：字典 请求头，cookies：字典或CookieJar，auth：元组 支持http认证功能，
        files：字典 传输文件，timeout：超时时间，proxies：字典 设置访问代理服务器 增加登陆认证，allow_redirects：True/False 重定向开关，
        stream：True/False 获取内容立即下载开关，verity：True/False，认证SSL证书，cert：本地SSL证书路径）

# 字典转换成json json.dumps(data)
# json转换成字典 json.load(dict)

post方法
headers={'Content_type': 'application/json'}
data={}

# 发送body为原格式的post请求
requests.post(url,data=data,headers=headers)

# 发送body为json格式的post请求
requests.post(url,json=data,headers=headers)



response常用方法
    status_code 响应码
    headers 响应头
    raw 返回原始响应体,对象在内存的地址
    url 获取url
    encoding 编码格式
    content 字节方式的响应体，自动编码gzip和deflate压缩
    json requests中内置的JSON解码器
    history 
    reason 
    cookies 获取cookie
    elapsed
    request
    text 字符串返回的响应体，根据响应头部的字符编码进行编码
    raise_for_status() 失败请求，抛出异常
    
'''
# get方法
# r = requests.get('https://www.baidu.com')
# print(r.text)

# post请求方法


'''
接口关联
pytest通过fixture来实现项目级的token关联
fixture作用域
    session、module、class、function
结合fixture实现接口关联
'''

