import requests
from bs4 import BeautifulSoup
prefix='https://www.ptt.cc'
payload={
    'from':'/bbs/Gossiping/index.html',
    'yes':'yes'
    }
sess=requests.session()
#確認滿18頁面 略過
re = sess.post('https://www.ptt.cc/ask/over18',data=payload)
re = sess.get('https://www.ptt.cc/bbs/Lifeismoney/index.html')
#print (re.text.encode('utf-8'))
soup = BeautifulSoup(re.text, "html.parser")
board=str(soup.select('.board')[0])
boardName =board[board.find('</span>')+7:board.find('</a>')]



for line in soup.select('.r-ent'):
    title =str(line.select('.title')[0])
    print ("看板 :" +boardName)
    print("標題  :  "+ BeautifulSoup(title,"html.parser").text)
    print ("日期  :  "+BeautifulSoup(str(line.select('.date')[0]),"html.parser").text)
    print ("作者  :  "+BeautifulSoup(str(line.select('.author')[0]),"html.parser").text)
    
    url =title[title.find('<a href')+9:title.find('html">')+4]
    url = prefix +url
    #透過URL進入文章頁面拿取內容
    print (url)
    sess2=requests.session()
    re2 = sess2.get(url)
    content = BeautifulSoup(re2.text, "html.parser")
    print ("內文 :" +content.text)
 
    
    print ("-------------------------------------------------------------------------")
