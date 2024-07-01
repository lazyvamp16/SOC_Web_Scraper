from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "D:/code/SOC_webscraper/chromedriver-win64/chromedriver.exe"  # Replace with the path to your ChromeDriver
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service)

url = "https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%2050"
driver.get(url)
driver.implicitly_wait(10)

#wait = WebDriverWait(driver, 20)
#download_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@onclick='dnldEquityStock()']")))
#download_link.click()
time.sleep(10)

page_source = driver.page_source
driver.quit()
soup = BeautifulSoup(page_source, 'html.parser')
table = soup.find('table', {'id': 'equityStockTable'})
if table:
    print ("found table")
    stock_links = table.find_all('a', href=True, class_='symbol-word-break')
    stock_names = [link.text.strip() for link in stock_links]

#print (stock_names)
