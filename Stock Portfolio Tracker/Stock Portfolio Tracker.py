# Hardcoded stock prices (UPDATED)
stock_prices = {
    "RELIANCE": 2800,
    "TCS": 3500,
    "INFY": 1500,
    "HDFCBANK": 1600,
    "ICICIBANK": 950
}

total_investment = 0

# User input
n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))
    
    if stock in stock_prices:
        total_investment += stock_prices[stock] * quantity
    else:
        print("Stock not found!")

# Display result
print("Total Investment Value:", total_investment)

# Optional: Save to file
choice = input("Do you want to save result to file? (yes/no): ").lower()

if choice == "yes":
    file_type = input("Enter file type (txt/csv): ").lower()
    
    if file_type == "txt":
        with open("portfolio.txt", "w") as file:
            file.write("Total Investment Value: " + str(total_investment))
        print("Saved to portfolio.txt")
    
    elif file_type == "csv":
        with open("portfolio.csv", "w") as file:
            file.write("Total Investment Value," + str(total_investment))
        print("Saved to portfolio.csv")
    
    else:
        print("Invalid file type!")
