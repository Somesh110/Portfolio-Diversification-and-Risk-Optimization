
# Lesson 8: Visualize Portfolio Optimization

import statistics
import matplotlib.pyplot as plt
from pathlib import Path

# Hypothetical daily returns
stock_returns = [2, -3, 4, -2, 1]
gold_returns = [-1, 1, -1, 2, 0]

# Store graph data
stock_percentages = []
portfolio_volatilities = []

# Test allocations from 0% to 100%
for stock_percent in range(101):

    stock_weight = stock_percent / 100
    gold_weight = 1 - stock_weight

    daily_portfolio_returns = []

    for day in range(len(stock_returns)):
        daily_return = (
            stock_weight * stock_returns[day]
            + gold_weight * gold_returns[day]
        )
        daily_portfolio_returns.append(daily_return)

    # Calculate volatility
    volatility = statistics.pstdev(
        daily_portfolio_returns
    )

    stock_percentages.append(stock_percent)
    portfolio_volatilities.append(volatility)

# Identify minimum-risk allocation
minimum_risk = min(portfolio_volatilities)
best_index = portfolio_volatilities.index(minimum_risk)
best_stock_percentage = stock_percentages[best_index]

# Original 50/50 portfolio risk
original_risk = portfolio_volatilities[50]

# Create graph
plt.figure(figsize=(9, 5))

plt.plot(
    stock_percentages,
    portfolio_volatilities,
    label="Portfolio Volatility"
)

plt.scatter(
    best_stock_percentage,
    minimum_risk,
    color="green",
    label="Minimum-Risk Portfolio"
)

plt.scatter(
    50,
    original_risk,
    color="red",
    label="Original 50/50 Portfolio"
)

plt.xlabel("Stock Allocation (%)")
plt.ylabel("Daily Volatility (%)")
plt.title("Portfolio Optimization - Risk Analysis")

plt.legend()
plt.grid(True)

# Save graph in output folder
Path("output").mkdir(exist_ok=True)

plt.savefig(
    "output/portfolio_risk_curve.png",
    dpi=150,
    bbox_inches="tight"
)

# Print results
print(f"Best Stock Allocation: {best_stock_percentage}%")
print(f"Best Gold Allocation: {100 - best_stock_percentage}%")
print(f"Minimum Volatility: {minimum_risk:.2f}%")

# Display graph
plt.show()
