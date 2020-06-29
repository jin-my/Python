#-*- coding:utf-8 -*-


import os, subprocess, threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


path ='"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"' #Chrome 폴더
subprocess.Popen(path)

band_home = "https://band.us/band/"
band_id = "00000000"  # 밴드 아이디, 8자리.
band_category = "file"
downDir = "C:/BandCrawlingDownloader" #다운로드할 폴더
chrome_options = Options()

chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = 'C:/chromedriver.exe' #크롬드라이버를 별도로 다운로드 후 해당경로를 지정.
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
driver.implicitly_wait(3)

driver.get(band_home + band_id + "/" + band_category)

time.sleep(3)
print(driver.current_url)

while(True): #로그인 할 때까지 대기
    if driver.current_url == band_home + band_id + "/" + band_category:
        break

# driver.find_element_by_id("input_search").send_keys("검색어") # 검색어 검색 하여 크롤링
driver.find_element_by_xpath("//button[@data-uiselector='searchBtn']").click()
#driver.find_element_by_class_name("cFileList").find_elements_by_xpath("//a[@href='#']").click()
time.sleep(2) #.find_elements_by_class_name("uFlexItem")
# abc = driver.find_element_by_class_name("cFileList").find_elements_by_css_selector('a')

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

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


abc = driver.find_element_by_class_name("cFileList").find_elements_by_class_name("download")
print(len(abc))
for i, el in enumerate(abc):
    el.send_keys('\n')
    print(i, el)
    time.sleep(1)
# print(abc)
driver.find_element_by_class_name("cFileList").find_element_by_css_selector('a').send_keys('\n')  # 해당 링크 명령어에 엔터를 실행하도록 자바스크립트로 url이 등록되어있어서,
# find_element_by_link_text("Send InMail").click()
# print(driver)

#searchBtn
# class="cFileList"

# a href="#" data-uiselector="downloadFile" class="download"
# span class="subText -ellipsis"
 # <span> ::before  "2020년 5월"


