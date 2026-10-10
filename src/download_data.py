
# Lesson 9: Download Real Financial Market Data

import yfinance as yf
from pathlib import Path

# Select financial assets
tickers = ["SPY", "GLD", "BND"]

# Download historical market data
data = yf.download(
    tickers,
    start="2021-01-01",
    end="2026-10-01",
    auto_adjust=True,
    progress=False
)

# Check whether download was successful
if data.empty:
    raise SystemExit("No data downloaded. Check your internet.")

# Extract adjusted closing prices
prices = data["Close"][tickers].dropna()

if prices.empty:
    raise SystemExit("No complete price records available.")

# Display first five rows
print("Historical Market Prices:")
print(prices.head())

# Save data to CSV file
data_folder = Path(__file__).resolve().parent.parent / "Data"
data_folder.mkdir(exist_ok=True)

file_path = data_folder / "market_prices.csv"
prices.to_csv(file_path)

print("\nData downloaded successfully!")
print("Total trading days:", len(prices))
print("File saved to:", file_path)
