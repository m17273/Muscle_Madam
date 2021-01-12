from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import openpyxl
import time
import re

wb = openpyxl.Workbook()

sheet = wb.active

sheet.append(["가게이름", "주소", "번호", "대표메뉴"])

options = webdriver.ChromeOptions()
# options.add_argument("headless")
# driver = webdriver.Chrome('./chromedriver.exe', options=options)
driver = webdriver.Chrome('./chromedriver.exe')
url = "https://www.diningcode.com/list.php?query=외대"
driver.get(url)

for i in range(9):
    time.sleep(1)
    btn = driver.find_element_by_css_selector("span[class='more-btn']")
    btn.click()
    print(btn)

lis = driver.find_elements_by_css_selector("ul#div_list > li")
for li in lis:
    if li.get_attribute("onmouseenter") != None:
        a = li.find_element_by_css_selector("a[class='blink']")
        url = a.get_attribute("href")
        print(url)
        time.sleep(0.5)

        res = requests.get(url)
        time.sleep(0.1)
        html = bs(res.text, 'html.parser')

        title = html.select_one('div.tit-point > p.tit').text

        try:
            sign = html.select_one('div.btxt').text
            sign = re.sub('외대', '', sign)
            sign = re.sub('[^A-Za-z0-9가-힣,]', '', sign)
            # split후 리스트에 담아주면 됨
        except:
             sign = ""

        addr = html.select_one('li.locat').text
        tel = html.select_one('li.tel').text

        menu = []
        price = []
        try:
            menu_info = html.select_one('div.menu-info')
            menus = html.find_all("p", "l-txt Restaurant_MenuItem")
            prices = html.find_all("p", "r-txt Restaurant_MenuPrice")
            for m in menus:
                m = m.text
                m = re.sub('\n', '', m)
                menu.append(m)
            for p in prices:
                price.append(p.text)
            items = list(zip(menu, price))
        except:
            print("no menuInfo")

        print(title, addr, tel, sign, sep='\n')

        # menus = ""
        # for menu, price in items:
        #     item = f"{menu} : {price}\n"
        #     menus += item

        t = title
        a = addr
        te = tel
        s = sign
        # m = menus

        sheet.append(([t, a, te, s]))


driver.close()
driver.quit()

wb.save("eat.xlsx")