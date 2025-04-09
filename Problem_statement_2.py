import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\dipak\OneDrive\Desktop\Python project\Electric_Vehicle_Population_Data.csv")# 1. EV count by model year
# 1. EV count by model year
yearly_count = df['Model Year'].value_counts().sort_index()
yearly_count.plot(marker='o', figsize=(10, 5))
plt.title("EV Adoption by Model Year")
plt.xlabel("Model Year")
plt.ylabel("Number of EVs")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. BEV vs PHEV trends
type_year_trend = df.groupby(['Model Year', 'Electric Vehicle Type']).size().unstack().fillna(0)
type_year_trend.plot(figsize=(12, 6))
plt.title("EV Type Trends by Model Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.grid(True)
plt.tight_layout()
plt.show()

# 3. Model Year trends per Make
make_year = df.groupby(['Model Year', 'Make']).size().unstack(fill_value=0)
make_year.T.head(5).T.plot(figsize=(12, 6))
plt.title("Top 5 EV Makes Over the Years")
plt.tight_layout()
plt.show()

# 4. Cumulative growth
df['Count'] = 1
cumulative = df.groupby("Model Year")["Count"].sum().cumsum()
cumulative.plot(kind='line', marker='o', figsize=(10, 5), color='orange')
plt.title("Cumulative Growth of EVs")
plt.xlabel("Model Year")
plt.ylabel("Cumulative Count")
plt.grid(True)
plt.tight_layout()
plt.show()
