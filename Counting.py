'''
Created on 2019年1月28日

@author: dt
'''
from collections import Counter 

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "http://facebook.com/movie/b.txt",
     "http://yahoo.com/123/000/c.jpg",
     "http://gliacloud.com/haha.png",
    ]

splitUrl = []

for url in urls:
    url = url[url.rfind("/") + 1:]
#    print(url)
    splitUrl.append(url)
#print (Counter(splitUrl))
count = 0
cntlist =Counter(splitUrl).items()

#print(sorted(cntlist))
for key, value in sorted(cntlist):
    count += 1 #只列前三top
    if count > 3:
        break
    print(key, value)
    
