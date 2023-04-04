import requests as req
import os
from bs4 import BeautifulSoup as bs
import ssl

"""停用SSL憑證"""
ssl._create_default_https_context = ssl._create_unverified_context

"""使用UserAgent來模擬不同瀏覽器的存取,use_external_data=True存取外部數據"""
from fake_useragent import UserAgent
ua = UserAgent(use_external_data=True)

"""若開啟此檔案的位置並沒有alice這個資料夾,則建立一個"""
folderPath = 'alice'
if not os.path.exists(folderPath):
    os.makedirs(folderPath)
    
"""將ua提供的模擬伺服器設為隨機生成"""
my_headers = {
    'user-agent': ua.random
}

"""選擇你要爬圖文的網站"""
website="Insert Your Website"

"""由於要一次爬完所有圖文,所以story_list是回數,page_comics是該回的每一頁"""
story_list=[] #  準備放入每一回漫畫的連結, 每個元素都可連結到對應的回數
page_comics = [] # 準備放入某回漫畫的每一頁的圖片url


episodes=1
for epi in story_list: # 每一回漫畫中
    page_comics = [] # 重製/清空此list
    my_headers = {
        'user-agent': ua.random
    } # fake_useragent reset
    
    url = epi
    res = req.get(url, headers=my_headers)
    soup = bs(res.text, 'lxml')
    images = soup.select("ul.comic-contain > div > amp-img")
    for img in images:
        strUrl = img["src"] # 抓出每個元素的'src'的value, 為該圖片的url as a string
        page_comics.append(strUrl)
        
    count=1 # 一回漫畫裡的第幾張, 從1開始數
    
    for page in page_comics:
        os.system(f"curl {page}?t= -o {folderPath}/{episodes}-{count}.jpg")
        print(f"第{episodes}回 ID: {count}, 下載連結 {page}?t=") # ?t=  是真正的圖片網址
        count += 1
    
    episodes += 1 # 全部頁數run完準備進到下一回