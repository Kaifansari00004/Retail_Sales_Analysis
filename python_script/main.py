import pandas as pd


# now we load our cleaned and structured dataset into mysql
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:1234@localhost:3306/retail_mysql")

conn = engine.connect()
print("✅ Connection successful")

customers = pd.read_csv("customers_large.csv")
orders = pd.read_csv("orders_large.csv")
products = pd.read_csv("products_large.csv")
# file loaded

customers.drop_duplicates(inplace=True)
orders.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)
# dropped duplicates values

print(customers.isnull().sum())
print(orders.isnull().sum())
print(products.isnull().sum())
# check for missing values

customers["JoinDate"] = pd.to_datetime(customers["JoinDate"])
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])
print(customers)
print(orders)
# converted text dates into real ones

# Add Year-Month column for trend analysis
orders["OrderMonth"] = orders["OrderDate"].dt.to_period("M")

# Add Profit (assuming 20% margin for demo)
orders["Profit"] = orders["TotalAmount"] * 0.2

# Add Discount (5% if Quantity > 5, else 0)
orders["Discount"] = orders["Quantity"].apply(lambda x: 0.05 if x > 5 else 0)

print("Customers:\n", customers.head())
print("\nProducts:\n", products.head())
print("\nOrders:\n", orders.head())

customers.to_sql('customers_data',engine,index=False,if_exists='replace')
products.to_sql('product_data',engine,index=False,if_exists="replace")
orders.to_sql('orders_data',engine,index=False,if_exists='replace')