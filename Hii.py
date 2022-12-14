import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
os.system("clear")
dau="\033[1;32m~ [✓] => "
s3x=f"""\033[1;93m             

\033[1;32m  __      __    _____  _       _                _______          _ 
\033[1;35m  \ \    / /   |  __ \(_)     | |              |__   __|        | |
\033[1;32m   \ \  / /   _| |  | |_ _ __ | |__    ______     | | ___   ___ | |
\033[1;35m    \ \/ / | | | |  | | | '_ \| '_ \  |______|    | |/ _ \ / _ \| |
\033[1;36m     \  /| |_| | |__| | | | | | | | |             | | (_) | (_) | |
\033[1;35m      \/  \__,_|_____/|_|_| |_|_| |_|             |_|\___/ \___/|_|
\033[1;33m                                                                    
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
{dau}\033[1;31mTool Reg Pro5 Siêu Vjp
{dau}\033[1;36mLink Facebook: \033[1;37mhttps://www.facebook.com/DDAV.infor
{dau}\033[1;33mZalo : \033[1;37m0398484461
{dau}\033[1;35mỦng Hộ Lấy Động Lực Làm Tool 
{dau}\033[1;34mVí Momo : \033[1;37m0398484461
- - - - - - - - - - - - - - - - - - - - - - - - -
"""
for h in s3x:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.0005)
import requests
from time import strftime
ngay=int(strftime('%d'))
key1=str(ngay*1246546+23472)
key = 'flacscaskvudz'+key1
url = 'https://vudinh.000webhostapp.com/index.html/key.html?key='+key
token_link1s = '7628f85259e13d72f17d4fe559486cf90f434196'
tokenlink = '73aef3a46dab477c62ee7ae493178724341ff81e'
link1s = requests.get(f'https://octolink.io/api?api={token_link1s}&url={url}').json()
octolink = requests.get(f'https://mneylink.com/api?api={tokenlink}&url={url}').json()
if link1s['status']=="error": 
    print(link1s['message'])
    print(dau,'Lựa Chọn 2 Link Để Lấy Key')
    print(dau,octolink['message'])
    quit()
else:
    link_key=link1s['shortenedUrl']
    linkkey=octolink['shortenedUrl']
print(dau,'\033[1;33mLink Để Vượt Key Là: '+link_key)
print(dau,'Lựa Chọn 2 Link Để Lấy Key')
print(dau,'\033[1;33mLink Để Vượt Key Là: '+linkkey)
keynhap = input('\033[1;32m~ [✓] =>  \033[1;33mKey Đã Vượt Là: ')
if keynhap == key:
    print('Key Đúng Mời Bạn Dùng Tool')
else:
    print("Key Sai Vui Lòng Vượt Link Lại")
    quit()
print('Đang vô tool')

class reg_pro5():
    def __init__(self,cookies, name) -> None:
        self.cookies = cookies
        self.id_acc = self.cookies.split('c_user=')[1].split(';')[0]
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'vi',
            'cookie': self.cookies,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'viewport-width': '1366',
        }
        url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
        profile = requests.get(url_profile, headers=headers).text
        try:
            self.fb_dtsg = profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
        except:
            self.fb_dtsg = profile.split(',"f":"')[1].split('","l":null}')[0]
    def Reg(self):
        
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            # Requests sorts cookies= alphabetically
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'viewport-width': '979',
            'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }

        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
