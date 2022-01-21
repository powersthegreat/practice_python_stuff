import requests as requests
from bs4 import BeautifulSoup as BeautifulSoup

url = "https://www.tradingview.com/markets/cryptocurrencies/prices-all/"
results = requests.get(url)
src = results.content
soup = BeautifulSoup(src, "lxml")

coin_list = []
close_price_list = []

for a_tags in soup.find_all("a", {"class": "tv-screener__symbol"}):
    a_tags_text = a_tags.getText()
    coin_list.append(a_tags_text)


for td_tags in soup.find_all("span", {"class": "tv-data-table__cell tv-screener-table__cell tv-screener-table_cell--big"}):
    td_text = td_tags.getText()
    close_price_list.append(td_text)


def divide_chunks(list_1, n):
      
    for i in range(0, len(list_1), n): 
        yield list_1[i:i + n]
  
n = 6
divided_close_price_list = list(divide_chunks(close_price_list, n))
coin_to_price_dict = dict(zip(coin_list, divided_close_price_list))

def pulling_prices(coin, coin_dict):
    coin_name = str(coin)
    if coin_name == "coin":
        x = list(coin_dict.keys())
        for i in range(0, len(x)):
            print(str(i) + ".) " + str(x[i]))
    else:
        print("MKT CAP: " + "$" + coin_dict[coin_name][0])
        print("CURRENT PRICE: " + "$" + coin_dict[coin_name][2])
        print("TRADED VOLUME: " + coin_dict[coin_name][5])

     
user_input = input("Enter a coin name to see specs, enter 'list' to see list of currently traded coins, or enter 'stop' to end program:\n")
while user_input != "stop":
    pulling_prices(user_input, coin_to_price_dict)
    user_input = input("Enter a coin name to see specs or enter list to see list of currently traded coins: \n")