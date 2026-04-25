# -------------------------------
# 1. Import Libraries
# -------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# -------------------------------
# 2. Load Dataset
# -------------------------------
file_path = "C:/Users/mahes/OneDrive/Desktop/Projects/sales-data-analysis-dashboard/data/sales_data.csv"
df = pd.read_csv(file_path)


# -------------------------------
# 3. Preview Data
# -------------------------------
print("========== Top 5 Rows ==========")
print(df.head(), "\n")


# -------------------------------
# 4. Dataset Overview
# -------------------------------
print("========== Dataset Overview ==========")
print("Shape:", df.shape)
print("\nColumns:", list(df.columns))
print("\nInfo:")
df.info()


# -------------------------------
# 5. Data Cleaning
# -------------------------------
print("\n========== Data Cleaning ==========")

# Convert date columns safely
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# Drop rows where Order Date is missing
df = df.dropna(subset=['Order Date'])

# Drop unwanted columns if exist
drop_cols = ['csvbase_row_id', '\ufeffRow ID']
df = df.drop(columns=[col for col in drop_cols if col in df.columns])

print("Cleaning Done ✔️")


# -------------------------------
# 6. Feature Engineering
# -------------------------------
print("\n========== Feature Engineering ==========")

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.strftime('%Y-%m')

print("New Features Added: Year, Month")


# -------------------------------
# 7. Basic Analysis
# -------------------------------
print("\n========== Basic Analysis ==========")

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products:\n", top_products)

top_cities = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Cities:\n", top_cities)

category_sales = df.groupby('Category')['Sales'].sum()
print("\nSales by Category:\n", category_sales)


# -------------------------------
# 8. Time-based Analysis
# -------------------------------
print("\n========== Time-based Analysis ==========")

monthly_sales = df.groupby('Month')['Sales'].sum()

print("\nMonthly Sales Trend (Top 10):")
print(monthly_sales.head(10))

top_months = monthly_sales.sort_values(ascending=False).head(5)
print("\nTop 5 Months:\n", top_months)


# -------------------------------
# 9. Profit Analysis
# -------------------------------
print("\n========== Profit Analysis ==========")

profit_category = df.groupby('Category')['Profit'].sum()
print("\nProfit by Category:\n", profit_category)

loss_products = df.groupby('Product Name')['Profit'].sum().sort_values().head(5)
print("\nTop 5 Loss Making Products:\n", loss_products)


# -------------------------------
# 10. Visualizations
# -------------------------------

# Sales by Category
df.groupby('Category')['Sales'].sum().plot(kind='bar')
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.show()

# Monthly Sales Trend
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# Profit by Category
profit_category.plot(kind='bar')
plt.title("Profit by Category")
plt.ylabel("Profit")
plt.show()


# -------------------------------
# 11. Save Clean Data
# -------------------------------
print("\n========== Saving Clean Data ==========")

df.to_csv("C:/Users/mahes/OneDrive/Desktop/Projects/sales-data-analysis-dashboard/data/clean_data.csv", index=False)

print("Clean Data Saved Successfully ✔️")