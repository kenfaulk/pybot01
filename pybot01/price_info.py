import yfinance as yf

def get_current_price(ticker):
    return yf.Ticker(ticker).info.get("regularMarketPrice")

def get_price_history(ticker, period="1mo", interval="1d"):
    return yf.Ticker(ticker).history(period=period, interval=interval)
