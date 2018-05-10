import re
import os
import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"}
url='https://bing.ioliu.cn/'
count = 1

def subdownload(pics, director):
    global count
    for i in pics:
        i = i.replace("800x480", "1920x1080")
        print("download: " + i)
        r = requests.get(i, stream=True, headers=headers)
        with open('{director}/{count}.jpg'.format(director=director,count=count),'wb') as f:
            count += 1
            for chunk in r.iter_content():
                f.write(chunk)

for i in range(67):
    current_url = '{url}?p={number}'.format(url=url, number=i+1)
    print(current_url)
    htmltext = requests.get(current_url).text

    pic = re.compile('data-progressive="(.+?800x480.jpg)"')
    pics = pic.findall(htmltext)

    path = os.path.abspath(r'picture')
    if not os.path.isdir(path):
        os.makedirs(path)

    subdownload(pics,path)



