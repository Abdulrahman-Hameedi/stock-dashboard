import yfinance as yf
import pandas as pd


# fetch current price and % change
def get_stockPrice_and_Change(ticker: str):
    stock = yf.Ticker(ticker)
    data = stock.history(period = '2d')
    if data.empty or len(data) < 2:
        return None, None
    curr_price = data['Close'].iloc[-1]
    prev_price = data['Close'].iloc[-2]
    percent_change = ((curr_price - prev_price) / prev_price) * 100
    return curr_price, percent_change

# data of stock in last 5 years
def get_historical_data(ticker: str, period = '5y'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)

    if data.empty:
        return None

    return data

def get_financial_ratios(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info  # dictionary of company data
    ratios = {
        "PE Ratio": info.get("trailingPE"),
        "Market Cap": info.get("marketCap"),
        "EV/EBITDA": info.get("enterpriseToEbitda"),
        "Free Cash Flow": info.get("freeCashflow"),
        "Debt to Equity": info.get("debtToEquity"),
        "Return on Equity": info.get("returnOnEquity"),
        "Return on Assets": info.get("returnOnAssets"),
    }
    return ratios

if __name__ == "__main__":
    # print(get_stockPrice_and_Change("AAPL"))
    print(get_historical_data("GOOGL"))
    pass