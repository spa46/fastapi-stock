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
