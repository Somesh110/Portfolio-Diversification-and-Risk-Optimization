
# Lesson 6: Covariance and Portfolio Risk

import statistics

# Hypothetical daily returns in percentages
stock_returns = [2, -3, 4, -2, 1]
gold_returns = [-1, 1, -1, 2, 0]

# Calculate average returns
stock_mean = statistics.mean(stock_returns)
gold_mean = statistics.mean(gold_returns)

# Calculate covariance
covariance_sum = 0

for day in range(len(stock_returns)):
    stock_difference = stock_returns[day] - stock_mean
    gold_difference = gold_returns[day] - gold_mean

    covariance_sum += stock_difference * gold_difference

covariance = covariance_sum / len(stock_returns)

# Calculate individual volatilities
stock_vol = statistics.pstdev(stock_returns)
gold_vol = statistics.pstdev(gold_returns)

# Portfolio weights
stock_weight = 0.50
gold_weight = 0.50

# Calculate portfolio variance
portfolio_variance = (
    (stock_weight ** 2) * (stock_vol ** 2)
    + (gold_weight ** 2) * (gold_vol ** 2)
    + 2 * stock_weight * gold_weight * covariance
)

# Portfolio volatility is square root of variance
portfolio_volatility = portfolio_variance ** 0.5

# Display results
print(f"Covariance: {covariance:.2f}")
print(f"Stock Volatility: {stock_vol:.2f}%")
print(f"Gold Volatility: {gold_vol:.2f}%")
print(f"Portfolio Volatility: {portfolio_volatility:.2f}%")
