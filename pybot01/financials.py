import yfinance as yf

def get_pe_ratio(ticker):
    return yf.Ticker(ticker).info.get("trailingPE")

def get_peg_ratio(ticker):
    return yf.Ticker(ticker).info.get("pegRatio")
