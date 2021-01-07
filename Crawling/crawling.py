from selenium import webdriver
import time

options = webdriver.ChromeOptions()
# options.add_argument("headless")
# driver = webdriver.Chrome('./chromedriver.exe', options=options)
driver = webdriver.Chrome('./chromedriver.exe')

url = "https://www.diningcode.com/list.php?query=외대"
driver.get(url)

for i in range(2):
    time.sleep(1)
    btn = driver.find_element_by_css_selector("span[class='more-btn']")
    btn.click()
    print(btn)

lis = driver.find_elements_by_css_selector("ul#div_list > li")
for li in lis:
    if li.get_attribute("onmouseenter") != None:
        li.click()
        driver.switch_to_window(driver.window_handles[-1])
        res_name = driver.find_element_by_class_name("tit").text
        print(res_name)
        time.sleep(5)

driver.close()
driver.quit()
'''
url = "https://www.diningcode.com/list.php?query=외대"

response = req
uests.get(url)
html = bs(response.text, "html.parser")

# lists = html.select("li[onmouseenter^='setIcon']")
lists = html.findAll("li", {"onmouseenter": re.compile("^setIcon")})
for list in lists:
    print(list)
'''