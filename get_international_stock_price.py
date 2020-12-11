## parser.py
import requests
from bs4 import BeautifulSoup
def get_code(company_code):
    url = "https://finance.yahoo.com/quote/"+company_code+"?p="+company_code+".tsrc=fin-srch"
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

def get_price(company_code):
    bs_obj = get_code(company_code)
    no_today = bs_obj.find("span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
    return no_today.text
def get_stocks_info():
    pass

def get_stock_info(company_code):
    now_price = get_price(company_code)
    return now_price