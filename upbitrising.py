# -*- coding: utf-8 -*-
import pyupbit
import time
import telegram

bot = telegram.Bot(token='2044191300:AAFpQPgepqeQXBOWaIf3Djh_VZlMrf5gXbE')
chat_id = 2086229730

access = "tmobuBWWxvYxV9B2oW8ewuv0VsRZXEj8NIApk1Qn" 
secret = "xPbZVoYxzeuDkmh9aQPJlQqxn9S6sg1edb8YnEP8" 
upbit = pyupbit.Upbit(access, secret)
print("코인 급등주 자동매매 시작")
index = 0
KRW= upbit.get_balance("KRW") # 이걸로는 되는데 def로는 왜 안됄까
tickers = pyupbit.get_tickers(fiat="KRW")

def old호가(ticker) :
    price = pyupbit.get_current_price(ticker)
    return price
      
def new호가(ticker) :
    time.sleep(30)
    price = pyupbit.get_current_price(ticker)
    return price

def old호가1(ticker) :
    time.sleep(3)
    price = pyupbit.get_current_price(ticker)
    return price
      
def new호가1(ticker) :
    time.sleep(10)
    price = pyupbit.get_current_price(ticker)
    return price

# def 거래상승(): # 거래량이 1분 전보다 1.5배인 경우
#     old거래량 =  pyupbit.get_ohlcv(ticker, interval = "minute1")
#     time.sleep(60)
#     new거래량 = pyupbit.get_ohlcv(ticker, interval = "minute1")

#     if old거래량*1.5 < new거래량:
#         lst2 # 200개의 데이터를 불러오는데 이게 맞는지?
#     return
#위의 두개를 매칭 시켜야 되는데 안되면 거래량을 빼야되려나

def 현재가(ticker):
    return pyupbit.get_current_price(ticker) # 작동 확인 / 또한, 티커에 없는 애를 넣거나 티커에 있는 애를 별도로 지정하면, 해당 녀석만 출력 됨.

def 잔고(ticker):
    return upbit.get_balance(ticker) # 종목을 지정해야만, 정보를 불러옴

def 목표가(ticker):
    return upbit.get_avg_buy_price(ticker) # 종목을 지정해야만, 정보를 불러옴

def 매수(ticker, cash=KRW):
    order = upbit.buy_market_order(ticker, KRW*0.05)
    return order # 작동확인, 티커만 "KRW-BCT" 형식으로 넣으면 작동함.

def 부분매수(ticker, cash=KRW):
    order = upbit.buy_market_order(ticker, KRW*0.1)
    return order 

def 지금매수(ticker, cash=KRW):
    order = upbit.buy_market_order(ticker, KRW*0.2)
    return order 

def 매도(ticker, volume="잔고(ticker)"):
    order = upbit.sell_market_order(ticker, 잔고(ticker)*0.05)
    return order

def 일부매도(ticker, volume="잔고(ticker)"):
    order = upbit.sell_market_order(ticker, 잔고(ticker)*0.2)
    return order

def 반매도(ticker, volume="잔고(ticker)"):
    order = upbit.sell_market_order(ticker, 잔고(ticker)*0.5)
    return order

def 풀매도(ticker, volume="잔고(ticker)"):
    order = upbit.sell_market_order(ticker, 잔고(ticker))
    return order

def 총매수금액():
    return upbit.get_amount('ALL')

# print(총매수금액())
# index = 0
# def 메세지():
#     mes = bot.sendMessage(chat_id=chat_id, text="코인 급등주 자동 매매가 {0}분 동안 작동 중입니다.".format(index))
#     global index
#     index += 10
#     return mes


# while True:
#     # 데이터 스크래핑
#     url = "https://www.coingecko.com/ko/거래소/upbit"
#     resp = requests.get(url)

#     # 데이터 선택
#     bs = BeautifulSoup(resp.text,'html.parser')
#     selector = "tbody > tr > td > a"
#     columns = bs.select(selector)

#     # TOP 5 추출
#     ticker_in_krw = [x.text.strip() for x in columns if x.text.strip()[-3:] == "KRW"]
#     print(ticker_in_krw[:5])
#     time.sleep(900)

while True:
    메세지()
    for ticker in tickers:
        if 잔고(ticker) ==0:
            if old호가(ticker)*1.02 < new호가(ticker):
                bot.sendMessage(chat_id=chat_id, text="상승&급등주 {0}를 포착하였습니다.".format(ticker))
                if old호가1(ticker)*1.01 < new호가(ticker):
                    지금매수(ticker)
                    bot.sendMessage(chat_id=chat_id, text="급등주 {0}를 매수하였습니다.".format(ticker))
                elif old호가1(ticker) < new호가(ticker):
                    부분매수(ticker)
                    bot.sendMessage(chat_id=chat_id, text="상승주 {0}를 매수하였습니다.".format(ticker))


    
# 급등주 매수 전략
# 1. 거래량 상위 10개 종목 중 1초 사이에 5%의 급 상승이 있는 종목 구별
# 2. 1번 종목 중 1초 사이에 2% 상승이 있으면 보유 현금의 10% 매수
# 3. 2번에서 매수한 종목이 2초 사이에 5% 이상 하락시 손절
# 4. 3번에서 손절한 종목 제외 나머지 종목은 20% 상승 시 20% 매도, 50% 이상 상승시 반 매도
# 5. 4번에서 남은 종목 중 100% 이상 상승시 전량 매도
# 6. 위의 명령은 0.5초마다 반복  




