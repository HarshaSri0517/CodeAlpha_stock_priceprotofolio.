stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 120,
    "AMZN": 300,
    "MSFT": 310
}

portfolio = {}
total_investment = 0

print("=== Stock Portfolio Tracker ===")

n = int(input("How many stocks do you want to add? "))

for i in range(n):
    stock = input("Enter stock name (AAPL, TSLA, GOOG, AMZN, MSFT): ").upper()

    if stock not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity

print("\n=== Portfolio Summary ===")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity

    print(f"{stock}: {quantity} x ${price} = ${value}")

    total_investment += value

print(f"\nTotal Investment Value = ${total_investment}")

# Save result to file
with open("portfolio_result.txt", "w") as file:
    file.write(f"Total Investment Value = ${total_investment}")

print("Result saved to portfolio_result.txt")