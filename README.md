# Warehouse Inventory Optimization

## 📌 Project Overview

Warehouse Inventory Optimization is a data-driven project developed as part of an internship to analyze warehouse inventory and support better inventory management decisions.

The project uses historical inventory and sales data to analyze demand patterns, forecast product demand, calculate inventory planning metrics, and provide an interactive dashboard using Streamlit.

## 🎯 Objectives

- Analyze warehouse inventory and sales data
- Understand demand patterns
- Forecast product demand
- Calculate reorder points
- Calculate safety stock
- Calculate Economic Order Quantity (EOQ)
- Identify low-stock inventory
- Visualize inventory and sales trends
- Provide an interactive inventory optimization dashboard

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Streamlit
- Plotly
- Scikit-learn
- Matplotlib
- Seaborn
- Power BI

## 📂 Project Structure

```text
warehouse-inventory-optimization/
│
├── app.py
├── main.py
├── extra.py
│
├── 1.EDA.py
├── 2.kmeans.py
├── 3.Random forest.py
├── 4.Regressor.py
│
├── calendar.csv
├── Inventory_report.csv
├── Cluster_report.csv
│
├── EDA_Daily_Sales_Trend.png
├── EDA_Monthly_Sales_Trend.png
├── EDA_Sales_Distribution.png
├── EDA_Top_10_Selling_Products.png
├── Cluster.png
├── Forecast.png
│
├── Inventory_optimization.pbix
├── requirements.txt
├── README.md
└── .gitignore
```

## 📊 Project Features

### 1. Exploratory Data Analysis

The project performs exploratory data analysis to understand inventory and sales patterns, including:

- Daily sales trends
- Monthly sales trends
- Sales distribution
- Top-selling products
- Inventory patterns

### 2. Demand Analysis

Historical sales data is analyzed to understand demand patterns and classify inventory based on demand levels.

The project identifies:

- Low Demand
- Medium Demand
- High Demand

### 3. Demand Forecasting

Historical sales information is used to estimate future demand and compare actual sales with forecasted sales.

The project provides visualizations to understand the difference between actual and forecasted demand.

### 4. Inventory Optimization

The project calculates important inventory management metrics such as:

- Forecast Demand
- Reorder Point
- Safety Stock
- Economic Order Quantity (EOQ)

These metrics support inventory planning and replenishment analysis.

### 5. K-Means Clustering

K-Means clustering is used to group inventory/products based on relevant characteristics.

The clustering analysis helps identify different inventory segments.

### 6. Machine Learning

Machine-learning techniques are explored for inventory and demand-related analysis, including:

- Random Forest
- Regression

These models are used to analyze relationships in the data and support forecasting and inventory analysis.

### 7. Interactive Streamlit Dashboard

The project includes an interactive Streamlit dashboard that displays:

- Forecast Demand
- Reorder Point
- Safety Stock
- EOQ
- Actual vs Forecast Sales
- Demand Distribution
- Inventory Summary
- Low Stock Items
- Inventory Details

## 📈 Dashboard

The Streamlit dashboard provides an interactive view of inventory performance and optimization metrics.

The dashboard includes:

- Actual Sales vs Forecast visualization
- Inventory Demand Distribution
- Inventory Summary
- Low Stock Identification
- Reorder Point
- Safety Stock
- Economic Order Quantity
- Inventory Details Table

## 📊 Dataset

The project uses historical inventory and sales data for analysis, forecasting, and inventory optimization.

Main data files include:

- `Inventory_report.csv`
- `calendar.csv`
- `Cluster_report.csv`

The data is used for exploratory analysis, demand forecasting, clustering, regression, and inventory optimization.

> **Note:** Dataset files should only be included in a public repository if they are permitted to be shared publicly and do not contain confidential or sensitive company information.

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Open the Project Directory

```bash
cd warehouse-inventory-optimization
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Dashboard

```bash
python -m streamlit run app.py
```

The dashboard will open automatically in your browser.

If it does not open automatically, visit:

```text
http://localhost:8501
```

## 📋 Requirements

The project requires Python and the packages listed in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

## 📊 Power BI

A Power BI report is included for additional inventory analysis and visualization.

```text
Inventory_optimization.pbix
```

The Power BI report provides additional visual analysis of the inventory data.

## 🔮 Future Enhancements

Future improvements could include:

- Real-time inventory monitoring
- Automated stock alerts
- Improved demand forecasting
- Automated reorder recommendations
- Real-time data integration
- Integration with warehouse management systems
- Advanced machine-learning forecasting
- Automated inventory optimization
- Interactive product-level filtering

## 📌 Project Outcome

The project provides a data-driven approach to warehouse inventory analysis by combining exploratory data analysis, forecasting, machine learning, inventory optimization techniques, and interactive visualization.

The Streamlit dashboard brings the major inventory insights together in a single interface for easier analysis and monitoring.

## 📜 Disclaimer

This project was developed as part of an internship for educational and project demonstration purposes.
