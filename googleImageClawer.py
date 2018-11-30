
# coding: utf-8

# In[ ]:

import selenium.webdriver
from bs4 import BeautifulSoup
import re
import os
import urllib.request
import json
from urllib.parse import quote
import time
import json
import socket
socket.setdefaulttimeout(10)


# In[ ]:

# soup = BeautifulSoup(driver.page_source, "html.parser")
# print(soup.prettify())


# In[ ]:

def downloadImage(word,scroll):
    key = quote(word)#關鍵字
    url='https://www.google.com.tw/search?q='+key+'&tbm=isch'

    driver = selenium.webdriver.Chrome()
    driver.set_window_position(0,0) #瀏覽器位置
    driver.set_window_size(1280,720) #瀏覽器大小
    driver.get(url)
    print(driver.title)

    index=1
    n=0
    while n < scroll:#scroll捲動次數
        soup = BeautifulSoup(driver.page_source, "html.parser")
        html = soup.find_all('div', class_='rg_meta notranslate') #找到藏有url的標籤
        html = str(html) #原本type不明所以轉str
        reg = r'"ou.*?(http.*?)"'#"=%quot; 型態記得注意
        reg = re.compile(reg)
        list = re.findall(reg,html)
        try:
            if index-len(list) == 0:
                a=driver.find_element_by_id('smb')
                a.click()
                time.sleep(3) 
        except:
            print('',end='')
        
        print('捲動第'+str(n)+'次，總有'+str(len(list))+'張')
        if not os.path.exists("./" + word):#make dir
                os.mkdir("./" + word)

        for num in range(index,len(list)):
            try:
                page=len(os.listdir('./'+word))+1
                urllib.request.urlretrieve(list[num],"./" + word+'/'+str(page)+'.jpg')
                print(str(page),end='|')
            except:
                print('x',end='|')
        index = len(list)

        driver.execute_script('window.scrollTo(0, 1000000000)')#scroll driver
        time.sleep(3)
        
        n+=1
    print('|')
    print('總共爬到'+str(len(list))+'張，成功下載'+str(page)+'張')
    print('finist')


# In[ ]:

downloadImage('田中美海',10)


# In[ ]:




# In[ ]:




# In[ ]:



