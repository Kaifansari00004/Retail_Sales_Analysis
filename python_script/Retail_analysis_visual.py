import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick
import numpy as np

'''
# Monthly Revenue of 2019
# Loading csv file for visualization
monthly_revenue = pd.read_csv("C:\Data Analysis\my project\Query Results\Monthly_Revenue.csv")

# Combining Year and Month into single colounm
monthly_revenue["YearMonth"] = monthly_revenue["Year"].astype(str) + "-" + monthly_revenue["Month"].astype(str).str.zfill(2)


# 📊 Monthly Revenue for 2019
revenue_2019 = monthly_revenue[monthly_revenue["Year"] == 2019]

plt.figure(figsize=(10,5))

# line chart
plt.plot(
    revenue_2019["Month"],
    revenue_2019["Revenue"],
    marker="o",
    markersize=8,
    linewidth=2,
    color="crimson",
    markerfacecolor="white",
    markeredgecolor="black"
)

# Title & labels
plt.title("Monthly Revenue (2019)", fontsize=18, fontweight="bold", color="navy")
plt.xlabel("Month", fontsize=12, fontweight="bold")
plt.ylabel("Revenue", fontsize=12, fontweight="bold")

# Show months as names instead of numbers
plt.xticks(
    ticks=range(1,13),
    labels=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
)

# Grid + background
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_facecolor("#6766bd")

# Annotate each point with revenue (in K)
for x, y in zip(revenue_2019["Month"], revenue_2019["Revenue"]):
    plt.text(x, y+3000, f"{int(y/1000)}K", ha="center", fontsize=9, color="black")

plt.tight_layout()
plt.show()

'''

'''
# Visualization of product which contributes most
Porducts_Contribution = pd.read_csv("C:\Data Analysis\my project\Query Results\Top_3_Products_Category_Contributes_Most.csv")
Porducts_Contribution["Products"] = Porducts_Contribution["Category"].astype(str)
# Create bar chart
plt.figure(figsize=(10,10))
bars =plt.bar(Porducts_Contribution["Products"], Porducts_Contribution["Revenue"], color=["#D14033", "#543999", "#5E8A1D"])

# Add labels & title
plt.title("Top 3 Products by Revenue Contribution", fontsize=16)
plt.xlabel("Products", fontsize=12)
plt.ylabel("Revenue", fontsize=12)

# ✅ Format Y-axis to show in millions with 1 decimal
plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{x/1e6:.1f}M'))

# Add value labels (rounded, with commas)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 100000, f"{yval:,.0f}",
             ha="center", va="bottom", fontsize=10)

plt.show()

'''
'''
# Visualization of Most Sold Products 
Sold_Products = pd.read_csv("C:\Data Analysis\my project\Query Results\Top_5_Sold_Products.csv")
plt.figure(figsize=(6,6))
plt.pie(
    Sold_Products["total_sold"],
    labels=Sold_Products["ProductName"],
    autopct="%1.1f%%",       # show percentage
    startangle=90,           # rotate for better look
    colors=plt.cm.Pastel1.colors # use nice colors
)

plt.title("Top 5 Sold Products (Pie Chart Visualization)", fontsize=14, color = "Blue")
plt.show()
'''

# Visualization of Top Customers
Top_Customers = pd.read_csv("C:\Data Analysis\my project\Query Results\Top_10_customers.csv")

# Create bar chart
plt.figure(figsize=(10,6))
plt.bar(
    Top_Customers["Name"], 
    Top_Customers["total_spent"], 
    color=plt.cm.Pastel1.colors
)

# Add labels & title
plt.title("Top 10 Customers by Total Spent", fontsize=16)
plt.xlabel("Customer Name", fontsize=12)
plt.ylabel("Total Spent (Revenue)", fontsize=12)

# Rotate x-axis labels for readability
plt.xticks(rotation=45, ha="right")

# Show values above bars
# Show integer values (floored) above bars
for i, val in enumerate(Top_Customers["total_spent"]):
    plt.text(i, val + (0.01 * max(Top_Customers["total_spent"])), 
             str(int(np.floor(val))), ha='center', fontsize=10)

plt.tight_layout()
plt.show()