import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\HP\OneDrive\Documents\promotion_effectiveness_analysis\data\sales.csv")

df.columns = df.columns.str.lower()

df['orderdate'] = pd.to_datetime(df['orderdate'], dayfirst=True, errors='coerce')



median_sales = df['sales'].median()

df['promotion_flag'] = df['sales'].apply(
    lambda x: 'Promotion' if x > median_sales else 'No Promotion'
)


avg_sales = df.groupby('promotion_flag')['sales'].mean()
total_sales = df.groupby('promotion_flag')['sales'].sum()

print("Average Sales:")
print(avg_sales)

print("\nTotal Sales:")
print(total_sales)


monthly_sales = df.groupby(
    [df['orderdate'].dt.month, 'promotion_flag']
)['sales'].mean().unstack()

print("\nMonthly Sales Trend:")
print(monthly_sales)


avg_sales.plot(kind='bar', title='Average Sales: Promotion vs No Promotion')
plt.xlabel('Promotion Status')
plt.ylabel('Average Sales')
plt.tight_layout()
plt.show()
