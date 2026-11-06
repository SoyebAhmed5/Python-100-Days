import requests
from bs4 import BeautifulSoup
import time

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch page: {response.status_code}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_stock_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    html = fetch_page(url)
    if not html:
        return None

    soup = parse_html(html)
    price_tag = soup.find("fin-streamer", {"data-symbol": ticker, "data-field": "regularMarketPrice"})
    if price_tag:
        return price_tag.text
    else:
        print("Stock price not found.")
        return None

def track_stock_price(ticker, interval=60):
    while True:
        price = get_stock_price(ticker)
        if price:
            print(f"{ticker}: ${price}")
        time.sleep(interval)

def main():
    print("Welcome to the Stock Price Tracker!")
    ticker = input("Enter the stock ticker symbol (e.g., AAPL, TSLA): ").upper()
    interval = int(input("Enter the update interval (in seconds): "))
    print(f"Tracking stock prices for {ticker} every {interval} seconds...")
    track_stock_price(ticker, interval)

if __name__ == "__main__":
    main()