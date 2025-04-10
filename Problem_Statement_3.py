import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\dipak\OneDrive\Desktop\Python project\Electric_Vehicle_Population_Data.csv")

# 1. Top 10 models
top_models = df['Model'].value_counts().head(10)
top_models.plot(kind='bar', figsize=(10, 5))
plt.title("Top 10 EV Models")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2 & 3. Electric Range & MSRP for top models
filtered = df[df['Model'].isin(top_models.index)][['Model', 'Electric Range', 'Base MSRP']].dropna()
sns.boxplot(x='Model', y='Electric Range', data=filtered)
plt.title("Electric Range by Top Models")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.boxplot(x='Model', y='Base MSRP', data=filtered)
plt.title("MSRP by Top Models")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Scatter: MSRP vs Range
sns.scatterplot(x='Electric Range', y='Base MSRP', hue='Model', data=filtered)
plt.title("Electric Range vs MSRP")
plt.tight_layout()
plt.show()
df
