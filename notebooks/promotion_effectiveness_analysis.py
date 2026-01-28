import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sales.csv")

# Basic checks
print(df.head())
print(df.info())

# Data cleaning
df['onpromotion'] = df['onpromotion'].fillna(False)
df['sales'] = df['sales'].fillna(0)
df['date'] = pd.to_datetime(df['date'])

# Create promotion flag
df['promotion_flag'] = df['onpromotion'].map({
    True: 'Promotion',
    False: 'No Promotion'
})

# Average sales comparison
avg_sales = df.groupby('promotion_flag')['sales'].mean()
print("Average Sales:")
print(avg_sales)

# Total sales contribution
total_sales = df.groupby('promotion_flag')['sales'].sum()
print("Total Sales:")
print(total_sales)

# Monthly sales trend
monthly_sales = df.groupby(
    [df['date'].dt.month, 'promotion_flag']
)['sales'].mean().unstack()

print("Monthly Sales Trend:")
print(monthly_sales)

# Visualization
avg_sales.plot(kind='bar', title='Average Sales: Promotion vs No Promotion')
plt.ylabel('Average Sales')
plt.show()

