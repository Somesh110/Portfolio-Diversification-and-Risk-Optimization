
# Minimum-Risk Portfolio Optimization

import statistics

# Hypothetical daily returns
stock_returns = [2, -3, 4, -2, 1]
gold_returns = [-1, 1, -1, 2, 0]

# Calculate average returns
stock_mean = statistics.mean(stock_returns)
gold_mean = statistics.mean(gold_returns)

# Calculate variance
stock_variance = statistics.pvariance(stock_returns)
gold_variance = statistics.pvariance(gold_returns)

# Calculate covariance
covariance = sum(
    (s - stock_mean) * (g - gold_mean)
    for s, g in zip(stock_returns, gold_returns)
) / len(stock_returns)

# Start with an extremely high risk
minimum_risk = float("inf")

best_stock_weight = 0
best_gold_weight = 0

# Test allocations from 0% to 100%
for stock_percent in range(101):

    stock_weight = stock_percent / 100
    gold_weight = 1 - stock_weight

    # Calculate portfolio variance
    portfolio_variance = (
        stock_weight ** 2 * stock_variance
        + gold_weight ** 2 * gold_variance
        + 2 * stock_weight * gold_weight * covariance
    )

    # Calculate portfolio volatility
    portfolio_risk = portfolio_variance ** 0.5

    # Save the allocation with the lowest risk
    if portfolio_risk < minimum_risk:
        minimum_risk = portfolio_risk
        best_stock_weight = stock_weight
        best_gold_weight = gold_weight

# Display optimal allocation
print("Minimum-Risk Portfolio")
print("----------------------")
print(f"Stocks: {best_stock_weight * 100:.0f}%")
print(f"Gold: {best_gold_weight * 100:.0f}%")
print(f"Minimum Volatility: {minimum_risk:.2f}%")
