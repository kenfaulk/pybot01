from pybot01 import get_current_price, get_pe_ratio, get_peg_ratio

def main():
    ticker = input("Enter a ticker symbol: ").upper()
    print(f"Price for {ticker}: {get_current_price(ticker)}")
    print(f"P/E Ratio: {get_pe_ratio(ticker)}")
    print(f"PEG Ratio: {get_peg_ratio(ticker)}")

if __name__ == "__main__":
    main()
