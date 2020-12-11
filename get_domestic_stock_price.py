## parser.py
import requests
from bs4 import BeautifulSoup
def get_code(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

def get_price(company_code):
    bs_obj = get_code(company_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind = no_today.find("span", {"class": "blind"})
    now_price = blind.text
    return now_price

company = {"삼성전자우":"005935"}   

def get_stocks_info():
    for item, code in company.items():
            now_price = get_price(code)
            print(item + " : " + now_price)


def get_stock_info(company_name):
    now_price = get_price(company[company_name])
    return now_price