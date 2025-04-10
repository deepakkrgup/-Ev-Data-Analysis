import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\dipak\OneDrive\Desktop\Python project\Electric_Vehicle_Population_Data.csv")

# 1. Cities sharing the same electric utility
utility_city = df[['Electric Utility', 'City']].dropna().drop_duplicates()
shared_utilities = utility_city.groupby('Electric Utility')['City'].nunique()
print("Cities per Utility:\n", shared_utilities)

# 2. Count how many unique cities each utility connects
city_counts = shared_utilities.sort_values(ascending=False)
print("\nTop 10 utilities by city connections:\n", city_counts.head(10))

# 3. Bar plot for top utilities connecting the most cities
top_utilities = city_counts.head(10)
top_utilities.plot(kind='barh', figsize=(10, 6), color='skyblue')
plt.xlabel("Number of Unique Cities")
plt.title("Top 10 Utilities Connecting the Most Cities")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# 4. Heatmap of Utility vs City counts
top_utils = top_utilities.index
filtered_df = df[df['Electric Utility'].isin(top_utils)]
heatmap_data = pd.crosstab(filtered_df['Electric Utility'], filtered_df['City'])
plt.figure(figsize=(14, 6))
sns.heatmap(heatmap_data, cmap="Blues", cbar=False)
plt.title("Utility vs City Heatmap (Top 10 Utilities)")
plt.tight_layout()
plt.show()
