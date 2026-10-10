
# Lesson 3: Calculate portfolio return

# Total investment
investment = 100000

# Allocation weights
stock_weight = 0.50
gold_weight = 0.30
bond_weight = 0.20

# Hypothetical returns in percentage
stock_return = 10
gold_return = 5
bond_return = -2

# Calculate weighted portfolio return
portfolio_return = (
    stock_weight * stock_return
    + gold_weight * gold_return
    + bond_weight * bond_return
)

# Calculate total profit
profit = investment * portfolio_return / 100

# Calculate final portfolio value
final_value = investment + profit

# Display results
print("Initial Investment: Rs.", investment)
print(f"Portfolio Return: {portfolio_return:.2f}%")
print(f"Total Profit: Rs. {profit:.2f}")
print(f"Final Portfolio Value: Rs. {final_value:.2f}")
