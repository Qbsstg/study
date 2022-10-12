"""
输入：开始日期、结束日期
输出：CSV
南京、无锡、徐州、常州、苏州、南通、连云港、淮安、盐城、扬州、镇江、泰州、宿迁
# place = ("南京","无锡","徐州","常州","苏州","南通","连云港","淮安","盐城","扬州","镇江","泰州","宿迁")
地区    日期    最低温度    最高温度
# <a href="/weather/jiangsu/nanjing_lishi.htm">南京</a>
"""
import csv
import requests
from bs4 import BeautifulSoup
import re

# url = "https://qq.ip138.com/weather/jiangsu/lishi.htm"
searchUrl = "https://qq.ip138.com/weather/lishi_search.asp"

headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
body1 = {
    'k': '玄武',
    'from': '2022-7-1',
    'to': '2022-9-27',
    'Submit': '提交',
    'act': 'byDate'
}

# resp = requests.get(url, headers=headers1)


# 获取到所有链接
# for a in a_list:
#     href = a.get('href')  # 直接通过get就可以拿到属性的值
#     href = "https://qq.ip138.com" + href
#     lianjie_list.append(href)

#  创建文件
path = "aa.csv"
with open(path, 'a') as f:
    # f = open("E:\\天气11211321.csv", mode="w", newline=""
    scvwriter = csv.writer(f)
    scvwriter.writerow(["地区", '日期', '天气', '最低温度', '最高温度'])

resp = requests.post(searchUrl, headers=headers1, data=body1)
resp.encoding = 'utf-8'  # 处理乱码
main_page = BeautifulSoup(resp.text, "html.parser")

# print(main_page)

find = main_page.find_all("table")


print(find)

# a_list = main_page.find("div", attrs={"class": "list"}).find_all("a")
# table = main_page.find("table", attrs={"class": "t12"})
# trs = table.find_all("tr")[1:]
# for tr in trs:
#     tds = tr.find_all("td")  # 拿到每行中的所有td
#     name = tds[0].text  # .text标识拿到被标签标记的内容（日期）
#     name1 = tds[1].text  # .text标识拿到被标签标记的内容（天气）
#     name2 = tds[2].text  # .text标识拿到被标签标记的内容（温度）
#     lis = re.findall(r"\d+", name2)
#     name3 = lis[0]
#     name4 = lis[1]
#     scvwriter.writerow([name, name1, name3, name4])
#     print("over~")
f.close()
print("over")
