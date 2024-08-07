#%%
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from tqdm import tqdm

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os 
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
import json
import folium
import warnings
import numpy as np
from bs4 import BeautifulSoup

#%% 서울 0
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=0&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver')) # 자기 자신의 chromedriver 넣으면 실행가능
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

서울교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    서울교육청예산.append(년도별교육청예산.text)


driver.close()

# %% 부산 1
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=1&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

부산교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    부산교육청예산.append(년도별교육청예산.text)


driver.close()

# %%
# %% 대구 2
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=2&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

대구교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    대구교육청예산.append(년도별교육청예산.text)


driver.close()

#%% 인천 3
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=3&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

인천교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    인천교육청예산.append(년도별교육청예산.text)


driver.close()

#%% 광주 4
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=4&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

광주교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    광주교육청예산.append(년도별교육청예산.text)


driver.close()

#%% 대전 5
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=5&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

대전교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    대전교육청예산.append(년도별교육청예산.text)


driver.close()

#%% 울산 6
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=6&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

울산교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    울산교육청예산.append(년도별교육청예산.text)


driver.close()

#%% 세종 7
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=7&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

세종교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    세종교육청예산.append(년도별교육청예산.text)


driver.close()

#%% 경기 8
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=8&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

경기교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    경기교육청예산.append(년도별교육청예산.text)


driver.close()

#%% 강원 9
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=9&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

강원교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    강원교육청예산.append(년도별교육청예산.text)


driver.close()

#%% 충북 10
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=10&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

충북교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    충북교육청예산.append(년도별교육청예산.text)


driver.close()

#%% 충남 11
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=11&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

충남교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    충남교육청예산.append(년도별교육청예산.text)


driver.close()

#%% 전북 12
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=12&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

전북교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    전북교육청예산.append(년도별교육청예산.text)


driver.close()

#%% 전남 13
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=13&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

전남교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    전남교육청예산.append(년도별교육청예산.text)


driver.close()

#%% 경북 14
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=14&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

경북교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    경북교육청예산.append(년도별교육청예산.text)


driver.close()

#%% 경남 15
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=15&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

경남교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    경남교육청예산.append(년도별교육청예산.text)


driver.close()

#%% 제주 16
url = "https://eduinfo.go.kr/portal/intrDiscMng/sdEduIntrDiscPage.do?idx=16&cateType=BUDG&stndY=2024#%20return%20false;"
driver = webdriver.Chrome(service=Service('/chromedriver'))
driver.set_window_position(0,0)
driver.maximize_window()
driver.get(url)

년도고르기 = driver.find_element(By.ID, '''searchFsclYy''').click()

제주교육청예산 = []

for i in range(1, 13):
    driver.find_element(By.CSS_SELECTOR, '''#searchFsclYy > option:nth-child({})'''.format(i)).click()

    driver.find_element(By.CSS_SELECTOR, '''body > div.edu_fin2_wrap > form > div.ct_search_box.mt20.mb20 > button''').click()
    #총괄요약표 
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > span > span.dynatree-expander''').click()
    #총괄요약표버튼
    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > span > a''').click()

    driver.find_element(By.CSS_SELECTOR, '''#tsTree > ul > li:nth-child(2) > ul > li > ul > li > span > a''').click()

    년도별교육청예산 = driver.find_element(By.XPATH, '''//*[@id="mySheet"]/tbody/tr[3]/td/div/div[1]/table/tbody/tr[2]/td[6]''')

    print(년도별교육청예산.text)
    제주교육청예산.append(년도별교육청예산.text)


driver.close()

# %%
# 지역별 교육청의 연도별 교육청 예산
년도 = [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013]
지역 = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남','제주']
# %%
df_서울 = pd.DataFrame({'지역' :지역[0], '년도' : 년도, '예산' : 서울교육청예산, "위도" : 37.5665, "경도" : 126.9780})
df_부산 = pd.DataFrame({'지역' :지역[1], '년도' : 년도, '예산' : 부산교육청예산, '위도': 35.1796, '경도': 129.0756})
df_대구 = pd.DataFrame({'지역' :지역[2], '년도' : 년도, '예산' : 대구교육청예산, '위도': 35.8722, '경도': 128.6014})
df_인천 = pd.DataFrame({'지역' :지역[3], '년도' : 년도, '예산' : 인천교육청예산, '위도': 37.4563, '경도': 126.7052})
df_광주 = pd.DataFrame({'지역' :지역[4], '년도' : 년도, '예산' : 광주교육청예산, '위도': 35.1595, '경도': 126.8526})
df_대전 = pd.DataFrame({'지역' :지역[5], '년도' : 년도, '예산' : 대전교육청예산, '위도': 36.3504, '경도': 127.3845})
df_울산 = pd.DataFrame({'지역' :지역[6], '년도' : 년도, '예산' : 울산교육청예산, '위도': 35.5396, '경도': 129.3114})
df_세종 = pd.DataFrame({'지역' :지역[7], '년도' : 년도, '예산' : 세종교육청예산, '위도': 36.4800, '경도': 127.2890})
df_경기 = pd.DataFrame({'지역' :지역[8], '년도' : 년도, '예산' : 경기교육청예산, '위도': 37.4138, '경도': 127.5183})
df_강원 = pd.DataFrame({'지역' :지역[9], '년도' : 년도, '예산' : 강원교육청예산, '위도': 37.8228, '경도': 128.1555})
df_충북 = pd.DataFrame({'지역' :지역[10], '년도' : 년도, '예산' : 충북교육청예산,'위도': 36.6357, '경도': 127.4913})
df_충남 = pd.DataFrame({'지역' :지역[11], '년도' : 년도, '예산' : 충남교육청예산, '위도': 36.6588, '경도': 126.6728})
df_전북 = pd.DataFrame({'지역' :지역[12], '년도' : 년도, '예산' : 전북교육청예산, '위도': 35.8200, '경도': 127.1088})
df_전남 = pd.DataFrame({'지역' :지역[13], '년도' : 년도, '예산' : 전남교육청예산, '위도': 34.8160, '경도': 126.4629})
df_경북 = pd.DataFrame({'지역' :지역[14], '년도' : 년도, '예산' : 경북교육청예산, '위도': 36.5759, '경도': 128.5055})
df_경남 = pd.DataFrame({'지역' :지역[15], '년도' : 년도, '예산' : 경남교육청예산, '위도': 35.4606, '경도': 128.2132})
df_제주 = pd.DataFrame({'지역' :지역[16], '년도' : 년도, '예산' : 제주교육청예산, '위도': 33.4996, '경도': 126.5312})

# %%
print(len(년도), len(서울교육청예산))
print(len(년도), len(세종교육청예산))
# %%
df_서울.info()
# %%
df_서울.head()
# %%
dfs = [df_서울, df_부산, df_대구, df_인천, df_광주, df_대전, df_울산, df_세종, df_경기, df_강원, df_충북, df_충남, df_전북, df_전남, df_경북, df_경남, df_제주]

# %%
result = pd.concat(dfs, ignore_index=True)

# %%
result.info()
# %%
print(result)
# %%
edu_df = result.copy()
# %%
edu_df.head(20)

#%%
edu_df['예산'] = edu_df['예산'].str.replace(',', '').astype(float)
# %%
plt.figure(figsize=(14,8))
line_plot = sns.lineplot(data=edu_df, x='년도', y='예산', hue='지역', marker = 'o')


for line, name in zip(line_plot.get_lines(), edu_df["지역"].unique()):
    y_values = line.get_ydata()[-1]
    x_values = line.get_xdata()[-1]
    line_plot.annotate(name, (x_values, y_values), xytext=(5, 0), textcoords="offset points")

plt.title('년도별 지역 예산')
plt.xlabel('년도')
plt.ylabel('예산 (단위: 원)')
plt.xticks(edu_df['년도'].unique())
plt.grid(True)
plt.legend(title='지역', loc = 'upper left')
plt.show()
# %%
edu_df.to_csv('지역별교육청예산.csv', index=False, encoding='utf-8-sig')

# %% 서울 경기 인천 한정으로 작업
sgi_df = pd.read_csv('../data/edumoney_data/지역별교육청예산.csv', encoding='utf-8')

# %%
sgi_df.info()
sgi_df.head()
# %%
sgi = sgi_df[sgi_df['지역'].isin(['서울', '인천', '경기'])]

# %%
sgi.info()
# %%
sgi.head()
# %%
plt.figure(figsize=(14,8))
line_plot = sns.lineplot(data=sgi, x='년도', y='예산', hue='지역', marker = 'o')


for line, name in zip(line_plot.get_lines(), sgi["지역"].unique()):
    y_values = line.get_ydata()[-1]
    x_values = line.get_xdata()[-1]
    line_plot.annotate(name, (x_values, y_values), xytext=(5, 0), textcoords="offset points")

plt.title('년도별 서울 경기 인천의 교육청 예산')
plt.xlabel('년도')
plt.ylabel('예산 (단위: 원)')
plt.xticks(sgi['년도'].unique())
plt.grid(True)
plt.legend(title='지역', loc = 'upper left')
plt.show()
# %%
sgi.to_csv('서울경기인천교육청예산.csv', index=False, encoding='utf-8-sig')
# %%
