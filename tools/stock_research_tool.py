
import yfinance as yf
from crewai.tools import tool




@tool("Live Stock Information Tool")
def get_stock_summary(stock_symbol: str) -> str:
    """
         always specify the datatype of the input and output parameter
         retrieve the stock price and other relevant information for a given stock symbot using yahoo finance
         parameter:
          stock-symbol as input
         output :
           a summary of the stock price, daily changes and other key data
    """

    stock = yf.Ticker(stock_symbol)
    info = stock.info
    print(info)

    stock_price = info.get("regularMarketPrice")
    change = info.get("regularMarketChange")
    change_percent = info.get("regularMarketChangePercent")
    stock_currency = info.get("currency", "USD")

    if stock_price is None:
        return f"Cannot retrieve price for {stock_symbol.upper()}"

            # Handle possible None values safely
    change = change if change is not None else 0
    percent_change = change_percent if change_percent is not None else 0

    return (
          f"Stock: {stock_symbol.upper()}\n"
          f"Price: {stock_price} {stock_currency}\n"
          f"Change: {change:.2f} ({percent_change:.2f}%)\n"
       )

#print(get_stock_summary("CC"))