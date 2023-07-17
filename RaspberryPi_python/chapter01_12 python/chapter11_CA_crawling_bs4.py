import requests
import os
import time
import urllib.request
from bs4 import BeautifulSoup

search_query = "신민아"
url = f"https://www.google.com/search?q={search_query}&source=lnms&tbm=isch"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
img_tags = soup.find_all('img')

folder_path = "./신민아/"
if not os.path.exists(folder_path):
    os.mkdir(folder_path)

count = 0

for img_tag in img_tags:
    try:
        if count >= 50:
            break
        img_url = img_tag['src']
        img_name = search_query + str(count) + ".jpg"
        urllib.request.urlretrieve(img_url, os.path.join(folder_path, img_name))
        print("Downloading image", count+1)
        count += 1
        time.sleep(1)  # 사이트의 접속 제한을 피하기 위한 대기 시간 설정
    except:
        continue

print("Done downloading images!")
