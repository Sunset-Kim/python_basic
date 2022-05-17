# API

import requests
# requests 패키지를 이용한다 - Library (라이브러리)

import pandas as pd
# 시각화 하는 라이브러리

# 1. 사용자의 관심종목 추가하기
# - 특정 주식의 지금 가격 보기
# 2. 실시간 인기종목 보기
# 3. 종목의 시세변동 보기

# https://api.finance.naver.com/service/itemSummary.naver?itemcode=035720


# 1. API 에다가 정보를 요청해 (뭘까)
# 2. API 에서 가져온 정보를 리턴해
def get_stock_summary(itemcode):
  res = requests.get("https://api.finance.naver.com/service/itemSummary.naver?itemcode=" + itemcode)
  return res.json()
  # Mocking 한다
  current_price = res.now
  
  return {
    'current_price': current_price,
    'item_code': itemcode
  }
  
def get_trending_stocks():
  raw_res = requests.get("https://m.stock.naver.com/api/mystock/group/-2")
  res = raw_res.json()
  stocks = res["stocks"]
  return stocks

def visualize_trending_stocks(stocks):
  # 데이터를 시간화 하는 로직
  stocks_df = pd.DataFrame(stocks)
  stocks_df.to_html("api/주식/tmp.html")
  
trending_stock = get_trending_stocks()
visualize_trending_stocks(trending_stock)
print('하하')
