# Problem Statement 1: County-Wise Electric Vehicle Distribution
# 1. Top 10 counties
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(R"C:\Users\dipak\Downloads\ELECTRIC.csv")
top_counties = df['County'].value_counts().head(10)
print(top_counties)

# 2. BEV vs PHEV in top counties
bev_phev = df[df['County'].isin(top_counties.index)].groupby(['County', 'Electric Vehicle Type']).size().unstack().fillna(0)
bev_phev.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title("BEV vs PHEV Count by County")
plt.ylabel("Vehicle Count")
plt.xlabel("County")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Average Electric Range by County
avg_range = df.groupby("County")["Electric Range"].mean().dropna().sort_values(ascending=False).head(10)
avg_range.plot(kind='bar', figsize=(10, 5), color='green')
plt.title("Average Electric Range by County")
plt.ylabel("Average Range (miles)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Most common makes per county
top_make_by_county = df[df['County'].isin(top_counties.index)].groupby(['County', 'Make']).size().reset_index(name='count')
top_make_by_county = top_make_by_county.sort_values(['County', 'count'], ascending=[True, False])
print(top_make_by_county.groupby('County').first())
