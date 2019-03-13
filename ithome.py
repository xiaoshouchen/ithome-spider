from bs4 import BeautifulSoup
import urllib.request
import re
import pymysql
conn =pymysql.connect(host='localhost',user ='root',passwd='',db='myblog',charset='utf8')
cur=conn.cursor()
url="http://www.ithome.com"
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1)')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
file=data.decode('gbk')
title1='http://www\.ithome\.com/html/[a-z]+/[0-9]*\.htm'
a=re.findall(title1,file)
for i in range(0,len(a)):
   urltest=urllib.request.urlopen(a[i])
   strdata=urltest.read().decode('gbk')
   strdata=str(strdata)
   soup = BeautifulSoup(strdata,"html.parser")
   redemo="-"+" "+"[^\s]*"
   pattern=re.compile(redemo)
   rehtml="<[^<]*>"
   title=soup.h1.string
   title=str(title).encode('utf8')
   text = soup.find_all(class_="post_content")
   for string in text:
    content=string
   ad=soup.find_all(class_="yj_d")
   for adstring in ad:
        ad=adstring
   ad=str(ad)
   content=str(content)
   content=content.replace(ad,"")
   html=re.compile(rehtml)
   content=html.sub("\n",content)
   content=re.compile("\n+").sub(" ",content)
   content=content.encode('utf8')
   #content="content"
   sql="INSERT INTO `myblog`.`article` (`id`, `title`, `content`, `author`, `time`) VALUES (NULL,%s,%s, 'admin', '2016-03-08');"
   cur.execute(sql,[title,content]) 
   conn.commit()
conn.close()