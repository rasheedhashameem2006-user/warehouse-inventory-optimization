
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Warehouse Inventory Optimization",
    page_icon="📦",
    layout="wide"
)

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("📦 Warehouse Inventory Optimization Dashboard")
st.caption("Inventory analysis, demand forecasting and reorder recommendations")

# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

try:
    inventory_df = pd.read_csv("inventory_report.csv")
except FileNotFoundError:
    st.error("inventory_report.csv was not found.")
    st.stop()

# ---------------------------------------------------------
# DATA VALIDATION
# ---------------------------------------------------------

required_columns = ["date", "sales"]

missing_columns = [
    column for column in required_columns
    if column not in inventory_df.columns
]

if missing_columns:
    st.error(
        f"Missing required columns: {', '.join(missing_columns)}"
    )
    st.stop()

# Convert date
inventory_df["date"] = pd.to_datetime(
    inventory_df["date"],
    errors="coerce"
)

# Convert sales to numeric
inventory_df["sales"] = pd.to_numeric(
    inventory_df["sales"],
    errors="coerce"
)

# Remove invalid rows
inventory_df = inventory_df.dropna(
    subset=["date", "sales"]
).copy()

# Sort by date
inventory_df = inventory_df.sort_values("date")

# ---------------------------------------------------------
# FORECAST CALCULATION
# ---------------------------------------------------------

# If your CSV already contains a forecast column,
# use it. Otherwise calculate a 7-day moving average.

if "forecast" not in inventory_df.columns:

    inventory_df["forecast"] = (
        inventory_df["sales"]
        .rolling(window=7, min_periods=1)
        .mean()
    )

else:

    inventory_df["forecast"] = pd.to_numeric(
        inventory_df["forecast"],
        errors="coerce"
    )

    inventory_df["forecast"] = inventory_df["forecast"].fillna(
        inventory_df["sales"]
        .rolling(window=7, min_periods=1)
        .mean()
    )

# ---------------------------------------------------------
# INVENTORY PARAMETERS
# ---------------------------------------------------------

lead_time = 7

ordering_cost = 50

holding_cost = 2

service_factor = 1.65

# ---------------------------------------------------------
# SAFETY STOCK
# ---------------------------------------------------------

demand_std = inventory_df["sales"].std()

if pd.isna(demand_std):
    demand_std = 0

safety_stock = demand_std * service_factor

inventory_df["safety_stock"] = safety_stock

# ---------------------------------------------------------
# REORDER POINT
# ---------------------------------------------------------

# Reorder Point =
# Demand during lead time + Safety Stock

inventory_df["reorder_point"] = (
    inventory_df["forecast"] * lead_time
    + inventory_df["safety_stock"]
)

# ---------------------------------------------------------
# EOQ
# ---------------------------------------------------------

annual_demand = inventory_df["sales"].sum()

if annual_demand > 0 and holding_cost > 0:

    eoq = np.sqrt(
        (2 * annual_demand * ordering_cost)
        / holding_cost
    )

else:

    eoq = 0

inventory_df["eoq"] = eoq

# ---------------------------------------------------------
# FORECAST ACCURACY
# ---------------------------------------------------------

actual = inventory_df["sales"]
forecast = inventory_df["forecast"]

# Avoid division by zero
valid_accuracy = actual != 0

if valid_accuracy.sum() > 0:

    mape = (
        np.abs(
            (actual[valid_accuracy] - forecast[valid_accuracy])
            / actual[valid_accuracy]
        ).mean()
        * 100
    )

    forecast_accuracy = max(0, 100 - mape)

else:

    forecast_accuracy = 0

# ---------------------------------------------------------
# CURRENT / SUMMARY VALUES
# ---------------------------------------------------------

forecast_demand = inventory_df["forecast"].iloc[-1]

current_reorder_point = inventory_df[
    "reorder_point"
].iloc[-1]

current_safety_stock = inventory_df[
    "safety_stock"
].iloc[-1]

total_inventory = inventory_df["sales"].sum()

total_products = len(inventory_df)

# Count low-stock records
low_stock_items = (
    inventory_df["sales"]
    < inventory_df["reorder_point"]
).sum()

# ---------------------------------------------------------
# KPI SECTION
# ---------------------------------------------------------

st.subheader("📊 Inventory KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Forecast Demand",
    f"{forecast_demand:,.2f}"
)

col2.metric(
    "Reorder Point",
    f"{current_reorder_point:,.2f}"
)

col3.metric(
    "Safety Stock",
    f"{current_safety_stock:,.2f}"
)

col4.metric(
    "EOQ",
    f"{eoq:,.2f}"
)

# ---------------------------------------------------------
# SALES VS FORECAST
# ---------------------------------------------------------

st.subheader("📈 Actual Sales vs Forecast")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=inventory_df["date"],
        y=inventory_df["sales"],
        mode="lines+markers",
        name="Actual Sales"
    )
)

fig.add_trace(
    go.Scatter(
        x=inventory_df["date"],
        y=inventory_df["forecast"],
        mode="lines+markers",
        name="Forecast"
    )
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Units Sold",
    hovermode="x unified",
    height=450
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------------
# DEMAND CLASSIFICATION
# ---------------------------------------------------------

inventory_df["inventory_type"] = inventory_df["sales"].apply(
    lambda x:
        "Low Demand"
        if x < 3000
        else
        "Medium Demand"
        if x < 5000
        else
        "High Demand"
)

pie_data = (
    inventory_df["inventory_type"]
    .value_counts()
    .reset_index()
)

pie_data.columns = [
    "inventory_type",
    "count"
]

# ---------------------------------------------------------
# DEMAND DISTRIBUTION
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("🥧 Demand Distribution")

    fig_pie = px.pie(
        pie_data,
        names="inventory_type",
        values="count",
        title="Inventory Demand Distribution"
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

# ---------------------------------------------------------
# INVENTORY SUMMARY
# ---------------------------------------------------------

with col2:

    st.subheader("📦 Inventory Summary")

    st.metric(
        "Total Products",
        f"{total_products:,}"
    )

    st.metric(
        "Total Inventory",
        f"{total_inventory:,.0f}"
    )

    st.metric(
        "Low Stock Items",
        f"{low_stock_items:,}"
    )

    st.metric(
        "Forecast Accuracy",
        f"{forecast_accuracy:.2f}%"
    )

# ---------------------------------------------------------
# LOW STOCK WARNING
# ---------------------------------------------------------

st.subheader("⚠️ Stock Status")

if low_stock_items > 0:

    st.warning(
        f"{low_stock_items} inventory records are below "
        "their calculated reorder point."
    )

else:

    st.success(
        "No inventory records are currently below "
        "the calculated reorder point."
    )

# ---------------------------------------------------------
# INVENTORY DETAILS
# ---------------------------------------------------------

st.subheader("📋 Inventory Details")

table_columns = [
    "date",
    "sales",
    "forecast",
    "reorder_point",
    "safety_stock",
    "eoq"
]

existing_columns = [
    column
    for column in table_columns
    if column in inventory_df.columns
]

display_df = inventory_df[existing_columns].copy()

# Format numerical columns
for column in existing_columns:

    if column != "date":

        display_df[column] = display_df[column].round(2)

st.dataframe(
    display_df,
    use_container_width=True,
    height=400
)

# ---------------------------------------------------------
# LAST UPDATED
# ---------------------------------------------------------

st.divider()

st.write(
    "Last Updated:",
    datetime.now().strftime("%d-%m-%Y %H:%M:%S")
)

