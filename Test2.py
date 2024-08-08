import urllib.request

webUrl=urllib.request.urlopen('https://www.python.org/')

htmldata=webUrl.read()
"""print("result: "+str(webUrl.getCode()))"""
print(htmldata)
