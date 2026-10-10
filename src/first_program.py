# My first Portfolio Optimization program

print("Welcome to Portfolio Optimization!")

# Total money available for investment
investment = 100000

# Percentage allocation
stock_weight = 0.50
gold_weight = 0.30
bond_weight = 0.20

# Calculate investment in each asset
stocks = investment * stock_weight
gold = investment * gold_weight
bonds = investment * bond_weight

# Display results
print("Total Investment: Rs.", investment)
print("Money invested in Stocks: Rs.", stocks)
print("Money invested in Gold: Rs.", gold)
print("Money invested in Bonds: Rs.", bonds)