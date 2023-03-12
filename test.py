# 建立一个http链接
import urllib.request

# 读取一个网页
response = urllib.request.urlopen('http://www.baidu.com')
html = response.read()
print(html)
