import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_key_stats(url):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    key_stats_container = soup.find('div', class_='eYanAe')

    if not key_stats_container:
        return {}

    key_stats = {}
    for stat_container in key_stats_container.find_all('div', class_='gyFHrc'):
        label_element = stat_container.find('div', class_='mfs7Fc')
        value_element = stat_container.find('div', class_='P6K39c')

        if label_element and value_element:
            label = label_element.text.strip()
            value = value_element.text.strip()
            key_stats[label] = value

    return key_stats

nifty50 = [
    "BHARTIARTL", "TECHM", "INFY", "LT", "HCLTECH", "APOLLOHOSP", "ONGC",
    "TCS", "WIPRO", "KOTAKBANK", "BAJAJFINSV", "HDFCBANK", "ADANIPORTS", "JSWSTEEL",
    "ITC", "CIPLA", "M&M", "TITAN", "HDFCLIFE", "SUNPHARMA", "BAJFINANCE", "BRITANNIA",
    "SBILIFE", "RELIANCE", "DIVISLAB", "HINDUNILVR", "ASIANPAINT", "HINDALCO", "TATASTEEL",
    "COALINDIA", "ICICIBANK", "AXISBANK", "NESTLEIND", "DRREDDY", "NTPC", "BAJAJ-AUTO",
    "EICHERMOT", "INDUSINDBK", "GRASIM", "SHRIRAMFIN", "SBIN", "POWERGRID", "TATAMOTORS",
    "MARUTI", "TATACONSUM", "ULTRACEMCO", "ADANIENT", "HEROMOTOCO"
]

base_url = "https://www.google.com/finance/quote/"

all_stock_data = []

for stock_code in nifty50:
    url = f"{base_url}{stock_code}:NSE"
    key_stats = extract_key_stats(url)
    key_stats['Stock Code'] = stock_code  
    all_stock_data.append(key_stats)

df = pd.DataFrame(all_stock_data)
df.to_excel('nifty50_stock_data.xlsx', index=False)
print("Data has been saved to nifty50_stock_data.xlsx")




"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

nifty50 = [
    "BHARTIARTL", "TECHM", "INFY", "LT", "HCLTECH", "APOLLOHOSP", "ONGC",
    "TCS", "WIPRO", "KOTAKBANK", "BAJAJFINSV", "HDFCBANK", "ADANIPORTS", "JSWSTEEL",
    "ITC", "CIPLA", "M&M", "TITAN", "HDFCLIFE", "SUNPHARMA", "BAJFINANCE", "BRITANNIA",
    "SBILIFE", "RELIANCE", "DIVISLAB", "HINDUNILVR", "ASIANPAINT", "HINDALCO", "TATASTEEL",
    "COALINDIA", "ICICIBANK", "AXISBANK", "NESTLEIND", "DRREDDY", "NTPC", "BAJAJ-AUTO",
    "EICHERMOT", "INDUSINDBK", "GRASIM", "SHRIRAMFIN", "SBIN", "POWERGRID", "TATAMOTORS",
    "MARUTI", "TATACONSUM", "ULTRACEMCO", "ADANIENT", "HEROMOTOCO"
]


base_url = "https://www.google.com/finance/quote/"
price_class = "YMlKec fxKbKc"

stock_data = pd.DataFrame(columns=["Stock Name", "Price"])

for ticker in nifty50:
    try:
        url = f"{base_url}{ticker}:NSE"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        price_element = soup.find(class_=price_class)
        if price_element:
            price = float(price_element.text.strip()[1:].replace(",", ""))
            stock_data = pd.concat([stock_data, pd.DataFrame({"Stock Name": [ticker], "Price": [price]})], ignore_index=True)
        else:
            print(f"Price not found for {ticker}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {ticker}: {e}")

if not stock_data.empty:  
    stock_data.to_excel("nifty50_stock_prices.xlsx", index=False)
    print("Excel file generated successfully!")
else:
    print("No stock data found. Please check for errors or potential website changes.")

"""

'''

from bs4 import BeautifulSoup
import requests

def extract_key_stats(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  key_stats_container = soup.find('div', class_='eYanAe')

  key_stats = {}
  for stat_container in key_stats_container.find_all('div', class_='gyFHrc'):
    label_element = stat_container.find('div', class_='mfs7Fc')
    value_element = stat_container.find('div', class_='P6K39c')

    if label_element and value_element:
      label = label_element.text.strip()
      value = value_element.text.strip()
      key_stats[label] = value

  return key_stats

url = "https://www.google.com/finance/quote/INFY:NSE"
key_stats = extract_key_stats(url)

for label, value in key_stats.items():
  print(f"{label}: {value}")
'''
