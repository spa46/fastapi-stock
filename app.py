# import yfinance as yf
import yahooquery as yf

# Done
# # https://github.com/financedata-org/FinanceDataReader
# import FinanceDataReader as fdr
#
#
# # df_NASDAQ = fdr.StockListing('NASDAQ')
# # print(df_NASDAQ)
#
# df_snp500 = fdr.StockListing('S&P500')
# print(df_snp500)

#########################################################

# msft = yf.Ticker("MSFT")
# print(msft.quarterly_earnings)

import json
aapl_yf = yf.Ticker("AAPL")
print(json.dumps(aapl_yf.all_modules, indent=4))

print(aapl_yf.recommendations)
print(aapl_yf.recommendation_trend)

#aapl.cashflowStatementHistory
# "exDividendDate": "2023-05-12 09:00:00",

# print(aapl_yf.asset_profile)
# print(aapl_yf.earning_history)
# print(aapl_yf.earnings)
# print(aapl_yf.earnings_trend)
# aapl_financials = aapl_yf.financials

# print(aapl_financials)

# df = yf.download('MSFT', interval='1h', period='1d')
# print(df)

import json
# company = yf.Ticker('TSLA')
# code = 'TSLA'
# # print(json.dumps(company.info, indent=4))
#
# for k,v in company.info.items():
#     if 'priceToBook' in k:
#         print(k, v)

# name = company.info['shortName']
# industry = company.info['industry']
# marketcap = company.info['marketCap']
# summary = company.info['longBusinessSummary']
# currentprice = company.info['currentPrice']
# targetprice = company.info['targetMeanPrice']
#
# per = company.info['trailingPE']
# eps = company.info['trailingEps']
# pbr = company.info['priceToBook']
#
# print(code,name,industry,marketcap,summary,currentprice,targetprice,per,eps,pbr)

msft = yf.Ticker("MSFT")

# get all stock info (slow)
# print(msft.info)
# print(msft.fast_info)
# get historical market data
# print(msft.history(period="1mo"))
# print(msft.recommendations_summary)


import pandas as pd
import numpy as np
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

import yahooquery as yf
# import FinanceDataReader as fdr # https://github.com/financedata-org/FinanceDataReader
#
# df = fdr.StockListing('SP500')
# print(df)

import json
ticker = yf.Ticker("AAPL")
# print(json.dumps(aapl_yf.all_modules, indent=4))

# print(aapl_yf.recommendations)
# print(aapl_yf.recommendation_trend)

# print(json.dumps(ticker.quotes, indent=4))

# print(json.dumps(ticker.all_modules,indent=4))
# print(ticker.cash_flow("a"))

print(ticker.dividend_history('2010-01-01'))
# print(ticker.dividend_history('20-01-01'))
# print(ticker.cash_flow("q", True)[['asOfDate', 'periodType', 'CashDividendsPaid']])
# print(ticker.cash_flow()[['asOfDate', 'periodType', 'CashDividendsPaid']])

# 배당률: Trailing: 12개월 배당 금액 / 현재 주가
# 배당률: Forward: 직전 배당 지급금액 * 연간 배당 횟수 (예외 배당 제외) / 현재주가
# 5개년 평균 수익률: 5개년 평균 배당률
# 배당 안정성: (5년간 배당 여부 / 5) * 100
# 배당 성향: 배당금액 / 당기순이익
# 배당 성장 안정성:
# 연평균 배당 성장률: 8.84%


# dividend yield:
#        2022-08-05   0.230000
#        2022-11-04   0.230000
#        2023-02-10   0.230000
#        2023-05-12   0.240000
# Date	Open	High	Low	Close*	Adj Close**	Volume
# May 12, 2023	173.62	174.06	171.00	172.57	172.57	45,497,800
# (0.23+0.23+0.23+0.24) / 172.57 = 0.005389 = 0.53%

df = ticker.history(start='2021-09-24', end='2022-09-26')
# df = ticker.history()
print('====')
print(df.head())

print(json.dumps(ticker.summary_detail, indent=4))
