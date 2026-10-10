
# Lesson 5: Correlation Analysis

import statistics

# Hypothetical daily returns
stock_returns = [2, -3, 4, -2, 1]
gold_returns = [-1, 1, -1, 2, 0]

# Calculate correlation
correlation = statistics.correlation(
    stock_returns, gold_returns
)

# Display result
print("Correlation:", round(correlation, 2))

# Interpret correlation
if correlation > 0:
    print("Assets tend to move in the same direction.")
elif correlation < 0:
    print("Assets tend to move in opposite directions.")
else:
    print("No linear correlation.")
