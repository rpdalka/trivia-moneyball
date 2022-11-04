import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver_for_mac")

browser = webdriver.Chrome(executable_path = DRIVER_BIN)


browser.implicitly_wait(30)
# date = '2022-11-02'
# skipped '2022-10-05'
dates = ['2022-11-02', '2022-10-26', '2022-10-19','2022-10-12',
            '2022-09-28','2022-09-21', '2022-09-14', '2022-09-07', '2022-08-31',
            '2022-08-24','2022-08-17', '2022-08-10', '2022-08-03', '2022-07-27',
            '2022-07-20','2022-07-13', '2022-07-06', '2022-06-29', '2022-06-22',
            '2022-06-15','2022-06-08', '2022-06-01', '2022-05-25', '2022-05-18',
            '2022-05-11','2022-05-04', '2022-04-27', '2022-04-20', '2022-04-13',
            '2022-04-06','2022-03-30', '2022-03-23', '2022-03-16', '2022-03-09',
            '2022-03-02','2022-02-23', '2022-02-16', '2022-02-09', '2022-02-02',
            '2022-01-26','2022-01-19', '2022-01-12', '2022-01-05']

writer = pd.ExcelWriter('trivia-data.xlsx', engine='xlsxwriter')

for date in dates:
    browser.get('https://triviakings.com/results/scores/stoneysonp/' + date)
    df=pd.read_html(browser.find_element(By.XPATH, "//*[@id=\"scoretable\"]").get_attribute('outerHTML'))[0]
    df.to_excel(writer,sheet_name=date )

writer.save()
