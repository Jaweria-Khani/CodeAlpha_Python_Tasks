
#                                                    Programmed by: Jaweria Khan
#                                                    CodeAlpha Python Programming
#                                                    Task 2: Stock Portfolio Tracker

import yfinance as yf # type: ignore
import pandas as pd # type: ignore

# Initialize the portfolio as a DataFrame
portfolio = pd.DataFrame(columns=["Name", "Symbol", "Quantity", "Buy Price", "Current Price", "Value", "Gain/Loss"])

def get_stock_name(symbol):
    """Fetch the full name of the stock using yfinance."""
    try:
        stock = yf.Ticker(symbol)
        return stock.info['longName']
    except Exception as e:
        return None

def add_stock(symbol, quantity, buy_price):
    """Add a stock to the portfolio."""
    try:
        # Get stock details
        stock_name = get_stock_name(symbol)
        if not stock_name:
            print(f"Error: Could not fetch the name for symbol '{symbol}'. Please check the symbol.")
            return

        stock = yf.Ticker(symbol)
        current_price = stock.history(period="1d")['Close'][-1]
        value = quantity * current_price
        gain_loss = (current_price - buy_price) * quantity

        # Add to portfolio
        portfolio.loc[len(portfolio)] = [stock_name, symbol, quantity, buy_price, current_price, value, gain_loss]
        print(f"Successfully added {stock_name} ({symbol}) to the portfolio.")
    except Exception as e:
        print(f"Error adding stock: {e}")

def view_portfolio():
    """View the current portfolio."""
    if portfolio.empty:
        print("Your portfolio is empty.")
    else:
        print(portfolio)

def remove_stock(symbol):
    """Remove a stock from the portfolio."""
    global portfolio
    portfolio = portfolio[portfolio["Symbol"] != symbol]
    print(f"Stock with symbol '{symbol}' has been removed.")

# Main program loop
while True:
    print("\n--- Stock Portfolio Tracker ---")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Remove Stock")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
        quantity = int(input("Enter quantity: "))
        buy_price = float(input("Enter buy price per stock: "))
        add_stock(symbol, quantity, buy_price)
    elif choice == "2":
        view_portfolio()
    elif choice == "3":
        symbol = input("Enter the symbol of the stock to remove: ").upper()
        remove_stock(symbol)
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
