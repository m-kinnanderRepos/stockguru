import requests
import json
from datetime import date, timedelta
import sys




def get_data(stockSymbol, price, config):
  
  today = date.today()
  fiveDaysAgo = today - timedelta(days=5)

  url = "https://api.finage.co.uk/history/stock/open-close"
  querystringFiveDaysAgo = {"stock":stockSymbol,"date":fiveDaysAgo.strftime("%Y-%m-%d"),"apikey":config["API"]["KEY"]}
  response = requests.request("GET", url, params=querystringFiveDaysAgo)

  array = json.loads(response.text)
  print("high for 5 days ago is : " + str(array["high"]))
  print("low for 5 days ago is : " + str(array["low"]))

  averageFiveDaysAgo = (array["high"] + array["low"]) / 2
  print("Average of the two is : " + str(averageFiveDaysAgo))

  diff = price / averageFiveDaysAgo
  print("diff is : " + str(diff))
  percent = 0
  if(diff < 1):
    percent = diff * 100
  
    if(percent > 46):
      print("greater than 46 percent")

    else:
      print("less than 46 percent")
  
  else:
    print("price is less than buy price")
  # print(array)
  # print(array["low"])

def read_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

          
if __name__ == "__main__":
    configFile = read_json("config.json")
    stockSymbol = input("Enter stock symbol: ")
    print("Stock symbol is " + stockSymbol)
    price = float(input("Enter buy price: "))
    print("Buy price is " + str(price))
    get_data(stockSymbol, price, configFile)
    # print(configFile["API"]["KEY"])
    
    