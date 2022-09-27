from tda import auth, client
import json
import datetime
import pandas
import time


api_key = '5W348KLER7G2MNO77MMYDBULKDGPFOTQ@AMER.OAUTHAP'
redirect_url = 'https://localhost'
driver_path = "C:\Program Files\Webdrivers\chromedriver.exe"
token_path = 'token'


try:
    client = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    serv_object = Service(driver_path)
    driver = webdriver.Chrome(service=serv_object)
    token_path = 'token'
    client = auth.client_from_login_flow(driver, api_key, redirect_url, token_path)

# formatting for startdate and enddate, very  hard to get so don't lose it!
start_date = datetime.datetime(year=2022, month=3, day=4)
end_date = datetime.datetime(year=2022, month=3, day=14)

response = client.get_price_history_every_thirty_minutes('SND', start_datetime=start_date, end_datetime=end_date, need_extended_hours_data=None)
# print(json.dumps(response.json(), indent=4))

#creating a csv from historical price json
df = pandas.read_json (response)
df.to_csv (r'data_feeds/csvs/E_tda.csv', index = None)