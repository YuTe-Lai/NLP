import requests
import json
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import time


def udn_bug(url):
    options = Options()        #解決瀏覽器問題（彈跳式視窗）
    prefs = {'profile.default_content_setting_values':{
        'notifications': 2
    }}
    #options.add_argument("--headless") #是否顯示瀏覽器
    options.add_experimental_option('prefs', prefs)    
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options =options) # chrome瀏覽器

    #driver.set_window_size(720,1280)#瀏覽器視窗大小

    driver.get(url)
    driver.implicitly_wait(30)

    SCROLL_PAUSE_TIME = 5 #捲軸下滑的間隔時間，視網路速度決定

    #無限往下捲動
    last_height = driver.execute_script("return document.body.scrollHeight") # Get scroll height
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height  

    content = BeautifulSoup(driver.page_source)
    driver.quit()
    
    return content


#爬取文章內文
def article_content(url):
    inin = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    a = soup.find(class_ = 'article-content__paragraph')
    ppp = a.find_all('p')
    for s in ppp:
        if len(s.text) >2:
            #print(s.text)
            s = s.text
            s = s.replace('\r\n','')
            inin.append(s)
            
    inin = ''.join(inin)
    return inin


#transform to dataframe
def html_to_df(content):
    title = []
    url = []
    category = []
    time = []
    contents = []
    
    article_tag = content.find(class_ = "story-list__text")
    
    i = 0
    while i < len(content.find_all(class_ = "story-list__text")):
        elements = [article_tag.find('a')] #To List
        for s in elements:
            #print("title：" + s.text)
            title.append(s.text)
            #print("url：" + s.get('href'))
            complete_url = 'https://udn.com'+s.get('href')
            url.append(complete_url)
            ccc = article_content(complete_url)
            #print(ccc)
            contents.append(ccc)
            
            
            
        category_tag = article_tag.find_all(class_ = "story-list__cate btn btn-blue")
        for s in category_tag:
            category.append(s.text)
            #print("category:" + s.text)
    
        time_tag = article_tag.find_all('time')
        for s in time_tag:
            time.append(s.text)
            #print("time：" + s.text)
        i = i+1
        article_tag = article_tag.find_next(class_ = "story-list__text")
        
    list_df = [title,url,category,time,contents]
    df = pd.DataFrame(list_df).transpose()
    df.columns = ['title','url','category','time','content']
    return df


#content = udn_bug('https://udn.com/news/archive?date=20201106')
#news_1106 = html_to_df(content)
