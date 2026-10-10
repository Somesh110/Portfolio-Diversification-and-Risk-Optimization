
# Lesson 4: Portfolio Risk and Diversification

import statistics

# Hypothetical daily returns in percentage
stock_returns = [2, -3, 4, -2, 1]
gold_returns = [-1, 1, -1, 2, 0]

# Portfolio allocation
stock_weight = 0.50
gold_weight = 0.50

# Calculate daily portfolio returns
portfolio_returns = []

for day in range(len(stock_returns)):
    daily_return = (
        stock_weight * stock_returns[day]
        + gold_weight * gold_returns[day]
    )
    portfolio_returns.append(daily_return)

# Calculate volatility
stock_risk = statistics.pstdev(stock_returns)
gold_risk = statistics.pstdev(gold_returns)
portfolio_risk = statistics.pstdev(portfolio_returns)

# Display results
print("Stock Volatility:", round(stock_risk, 2), "%")
print("Gold Volatility:", round(gold_risk, 2), "%")
print("Portfolio Volatility:", round(portfolio_risk, 2), "%")
