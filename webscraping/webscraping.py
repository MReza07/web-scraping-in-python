import requests
from bs4 import BeautifulSoup
import pandas as pd


def t_shirt(page):
    url =f'https://www.flipkart.com/clothing-and-accessories/topwear/tshirt/men-tshirt/pr?sid=clo%2Cash%2Cank%2Cedy&otracker=categorytree&otracker=nmenu_sub_Men_0_T-Shirts&page={page}'
    r= requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

def extract(soup):
    divs = soup.find_all('div', class_="_1xHGtK")
    for items in divs:
        title = items.find('a', class_="IRpwTa").text
        company = items.find('div', class_='_2WkVRV').text
        original_prices = items.find('div', class_='_3I9_wc').text.replace("₹", " ")
        discount_prices = items.find('div', class_='_30jeq3').text.replace("₹", " ")
        discount = items.find('div', class_='_3Ay6Sb').text.replace("off", " ")
        t_shirt = {
            'product name': title,
            'company': company,
            'original_prices': original_prices,
            'discount_prices': discount_prices,
            'discount ': discount,

        }
        t_shirt_list.append(t_shirt)


t_shirt_list=[]
for i in range(1,5):
    print(f"Scripting page{i}!!")
    c = t_shirt(i)
    extract(c)
df = pd.DataFrame(t_shirt_list)
df.to_csv('rr.csv')





















