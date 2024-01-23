import requests
import urllib.parse
import time
import pandas as pd
import openpyxl
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.driver_finder import DriverFinder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

# Global Variables
names = []
scraped_price = []
scraped_product = []
scraped_item_num = []
scraped_kirby_num = []
urls = []
scraped_kirby_price = []
difference_arr = []

# formate price from site
def format_price(x):
    if len(x) == 7:
        x = x[:5] + '.' + x[5:]
    elif len(x) == 6:
        x = x[:4] + '.' + x[4:]
        return x
    elif len(x) == 5:
        x = x[:3] + '.' + x[3:]
        return x
    elif len(x) == 4:
        x = x[:2] + '.' + x[2:]
        return x
    else:
        x = x[:1] + '.' + x[1:]
        return x
    
def write_to_excel(x):
    #df = pd.DataFrame({'Name': names, 'Product': scraped_product, 'Price': scraped_price, 'Product Num': scraped_item_num, 'Kirby Num': scraped_kirby_num, 'Kirby Price': scraped_kirby_price, 'Difference': difference_arr})
    df = pd.DataFrame({'Name': names, 'Product': scraped_product, 'Price': scraped_price, 'Product Num': scraped_item_num, 'Kirby Num': scraped_kirby_num, 'Kirby Price': scraped_kirby_price})
    df.to_excel(x + '.xlsx', index=False)
    

# selenium tools
def main(input, sheetName):
    file = open(input, 'r')
    line = file.readline()

    for line in file:
        
        token = "faf7a64c32e74fca9a1d151299e4a54f3ed61fce420" # scrape.do token
        
        urllib.parse.quote(line)
        search = "http://api.scrape.do?token={}&url={}".format(token, line)
        response = requests.request('GET', search)

        driver = webdriver.Chrome() # selenium OPEN, GET, WAIT
        driver.get(line)
        time = WebDriverWait(driver, 7)
        page_source = driver.page_source

        if 'homedepot.com' in line:
            home_depot(page_source, line)
        elif 'lowes.com' in line:
            lowes(page_source, line)
        elif 'grainger.com' in line:
            grainger(page_source, line)
        elif line == '':
            quit()

        driver.close()
    

    #price_difference(scraped_price, scraped_kirby_price)
    # write into excel file here
    write_to_excel(sheetName)
        

def home_depot(source, url):
    #column = 1
    name = 'Home Depot'
    soup = BeautifulSoup(source, 'html.parser', on_duplicate_attribute='ignore')
    product = soup.find('h1', attrs={'sui-h4-bold sui-line-clamp-unset'}).get_text()
    price = soup.find('div', attrs={'price-format__large price-format__main-price'}).get_text()
    price = format_price(price)
    item_num_fam = soup.find('h2', 'sui-font-regular sui-text-xs sui-leading-normal sui-tracking-normal sui-normal-case sui-line-clamp-unset sui-text-left')
    item_num = item_num_fam.find_next_sibling('h2').get_text()

    info = [name, product, price, item_num, url]
    #scraped_data.append(info)


def lowes(source, url):
    name ='Lowes'
    soup = BeautifulSoup(source, 'html.parser', on_duplicate_attribute='ignore')
    product = soup.find('h1', attrs={'kQJGef'}).get_text()
    price = soup.find('div', attrs={'main-price undefined split split-left'}).get_text()
    item_num = soup.find('p', attrs={'eCVRrO'}).get_text()
    item_num = item_num[6:]

    print(price)

    names.append(name)
    scraped_product.append(product)
    scraped_price.append(price)
    scraped_item_num.append(item_num)
    #scraped_data.append(info)
            

def grainger(source, url):
    name = 'Grainger'
    soup = BeautifulSoup(source, 'html.parser', on_duplicate_attribute='ignore')
    product = soup.find('h1', attrs={'lypQpT'}).get_text()
    price = soup.find('span', attrs={'rbqU0E lVwVq5'}).get_text()
    try:
        per = soup.find('span', attrs={'G32gdF'}).get_text()
        if per == '/ each':
            per = ' '
    except:
        per = ' '
    item_num = soup.find('div', attrs={'vDgTDH'}).find('dd').get_text()

    info = [name, product, price, item_num, url]
    #scraped_data.append(info)


if __name__ == '__main__':
    main()
