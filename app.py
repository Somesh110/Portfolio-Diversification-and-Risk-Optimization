
# Lesson 22: Portfolio Analytics Dashboard

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
from scipy.optimize import minimize

# Configure dashboard
st.set_page_config(
    page_title="Portfolio Risk Analytics",
    page_icon="📊",
    layout="wide"
)

# Main heading
st.title("Portfolio Diversification & Optimization")
st.write("Financial Data Analytics and Risk Analysis")


# Load financial data uploaded by the user

st.sidebar.header("Financial Data")

uploaded_file = st.sidebar.file_uploader(
    "Upload Market Prices CSV",
    type=["csv"]
)

# Stop gracefully until a CSV is provided
if uploaded_file is None:
    st.info(
        "Upload a CSV file containing Date, SPY, GLD "
        "and BND columns to start the analysis."
    )
    st.stop()

# Read uploaded financial data
@st.cache_data
def load_data(file):
    data = pd.read_csv(
        file,
        parse_dates=["Date"],
        index_col="Date"
    )

    required_assets = ["SPY", "GLD", "BND"]

    missing = [
        asset for asset in required_assets
        if asset not in data.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    data = data[required_assets].apply(
        pd.to_numeric,
        errors="coerce"
    ).dropna()

    if len(data) < 2:
        raise ValueError("Not enough valid price records.")

    return data.sort_index()

try:
    prices = load_data(uploaded_file)

except Exception as error:
    st.error(f"Unable to load CSV: {error}")
    st.stop()


# Sidebar: Select financial assets
st.sidebar.header("Portfolio Settings")

selected_assets = st.sidebar.multiselect(
    "Select Financial Assets",
    options=["SPY", "GLD", "BND"],
    default=["SPY", "GLD", "BND"]
)

if not selected_assets:
    st.warning("Please select at least one asset.")
    st.stop()

selected_prices = prices[selected_assets].dropna()

# Calculate daily returns
daily_returns = selected_prices.pct_change(
    fill_method=None
).dropna()

# Calculate volatility
annual_volatility = (
    daily_returns.std() * np.sqrt(252) * 100
)

# Display overview
st.header("Market Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Assets Selected", len(selected_assets))

with col2:
    st.metric("Trading Days", len(selected_prices))

with col3:
    st.metric(
        "Average Annual Volatility",
        f"{annual_volatility.mean():.2f}%"
    )

# Normalize historical prices
normalized_prices = (
    selected_prices / selected_prices.iloc[0]
) * 100

# Display historical performance
st.header("Historical Market Performance")

st.line_chart(normalized_prices)

st.caption(
    "Historical adjusted prices normalized to 100. "
    "Past performance does not guarantee future returns."
)

# Display volatility table
st.header("Historical Risk Analysis")

risk_table = pd.DataFrame({
    "Annualized Volatility (%)": annual_volatility
})

st.dataframe(risk_table.round(2))


# -----------------------------------
# PORTFOLIO OPTIMIZATION
# -----------------------------------

st.header("Portfolio Optimization")

# This version analyzes all three ETFs
if len(selected_assets) != 3:
    st.warning(
        "Select all three ETFs to compare the portfolios."
    )
    st.stop()

# Convert prices into decimal daily returns
returns = selected_prices.pct_change(
    fill_method=None
).dropna()

# Split data into training and testing
train = returns.loc["2021-01-01":"2024-12-31"]
test = returns.loc["2025-01-01":]

if len(train) < 2 or len(test) < 2:
    st.error("Insufficient training or testing data.")
    st.stop()

# Calculate training covariance in percentage points
cov = (train * 100).cov().to_numpy()

# Equal-weight portfolio
equal_weights = np.array([1/3, 1/3, 1/3])

# Optimization function
def optimize_portfolio(bounds):

    result = minimize(
        lambda w: w @ cov @ w,
        equal_weights,
        method="SLSQP",
        bounds=bounds,
        constraints={
            "type": "eq",
            "fun": lambda w: np.sum(w) - 1
        },
        options={"ftol": 1e-12}
    )

    if not result.success:
        raise RuntimeError(result.message)

    return result.x

# Minimum-variance portfolio
min_var_weights = optimize_portfolio(
    [(0, 1)] * 3
)

# Constrained portfolio: 10% to 60% per asset
constrained_weights = optimize_portfolio(
    [(0.10, 0.60)] * 3
)

# Compare allocations
allocation_df = pd.DataFrame({
    "Equal Weight (%)": equal_weights * 100,
    "Minimum Variance (%)": min_var_weights * 100,
    "Constrained (%)": constrained_weights * 100
}, index=selected_assets)

st.subheader("Portfolio Allocation Comparison")
st.dataframe(allocation_df.round(2))

# Calculate out-of-sample performance
def evaluate_portfolio(weights):

    portfolio_returns = test.to_numpy() @ weights

    annual_volatility = (
        np.std(portfolio_returns, ddof=1)
        * np.sqrt(252) * 100
    )

    cumulative_return = (
        np.prod(1 + portfolio_returns) - 1
    ) * 100

    return annual_volatility, cumulative_return

strategies = {
    "Equal Weight": equal_weights,
    "Minimum Variance": min_var_weights,
    "Constrained": constrained_weights
}

results = []

for name, weights in strategies.items():

    volatility, total_return = evaluate_portfolio(
        weights
    )

    results.append({
        "Portfolio": name,
        "Annual Volatility (%)": volatility,
        "Total Return (%)": total_return
    })

results_df = pd.DataFrame(results)

st.subheader("Out-of-Sample Performance")
st.dataframe(results_df.round(2))

st.caption(
    "Weights optimized using 2021-2024 data. "
    "Performance evaluated on 2025 onward. "
    "Assumes daily rebalancing and excludes trading costs."
)



# -----------------------------------
# INTERACTIVE DASHBOARD CHARTS
# -----------------------------------

st.divider()

st.header("Portfolio Comparison Charts")

# Chart 1: Portfolio allocation
st.subheader("1. Portfolio Allocation Comparison")

st.bar_chart(allocation_df)

st.write(
    "This chart shows how investment weights "
    "differ between the three portfolio strategies."
)

# Chart 2: Portfolio risk
st.subheader("2. Portfolio Risk Comparison")

risk_chart = results_df.set_index("Portfolio")[
    ["Annual Volatility (%)"]
]

st.bar_chart(risk_chart)

st.write(
    "Lower volatility means smaller historical "
    "fluctuations in portfolio returns."
)

# Chart 3: Portfolio returns
st.subheader("3. Portfolio Return Comparison")

return_chart = results_df.set_index("Portfolio")[
    ["Total Return (%)"]
]

st.bar_chart(return_chart)

st.write(
    "This chart compares cumulative portfolio "
    "returns during the testing period."
)

# Final explanation
st.divider()

st.subheader("Key Financial Insight")

st.write(
    "Minimum-variance optimization aims to reduce "
    "portfolio volatility, not maximize returns. "
    "A lower-risk portfolio may also generate "
    "lower returns."
)

st.caption(
    "For educational and research purposes only. "
    "Historical performance does not guarantee "
    "future investment results."
)

