import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Style
sns.set(style="darkgrid")

# Load dataset
file_path = r"C:/Users/LENOVO/Downloads/SupplyChainGHGEmissionFactors_v1.3.0_NAICS_CO2e_USD2022.csv"
df = pd.read_csv(file_path)


# STEP 1: Inspect & clean columns

print("Columns in dataset:\n", df.columns)

# Remove extra spaces
df.columns = df.columns.str.strip()


# STEP 2: Select correct columns

df['Emission'] = df['Supply Chain Emission Factors without Margins']

# Rename for simplicity
df['Industry'] = df['2017 NAICS Title']


# STEP 3: Data cleaning

# Convert to numeric
df['Emission'] = pd.to_numeric(df['Emission'], )

# Drop missing values
df = df.dropna(subset=['Emission', 'Industry'])


# STEP 4: Basic info

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df['Emission'].describe())


# STEP 5: Top 10 Industries

top10 = df.nlargest(10, 'Emission')

plt.figure(figsize=(10,6))
sns.barplot(x='Emission', y='Industry', data=top10)
plt.title("Top 10 Industries by Emissions")
plt.xlabel("Emission")
plt.ylabel("Industry")
plt.tight_layout()
plt.show()


# STEP 6: Distribution Plot

plt.figure(figsize=(8,5))
sns.histplot(df['Emission'], kde=True)
plt.title("Emission Distribution")
plt.xlabel("Emission")
plt.tight_layout()
plt.show()


# STEP 7: Boxplot (Outliers)

plt.figure(figsize=(8,5))
sns.boxplot(x=df['Emission'])
plt.title("Emission Outliers")
plt.tight_layout()
plt.show()


# STEP 8: Scatter Plot

plt.figure(figsize=(8,5))
plt.scatter(range(len(df)), df['Emission'])
plt.title("Emission Scatter Plot")
plt.xlabel("Index")
plt.ylabel("Emission")
plt.tight_layout()
plt.show()


# STEP 9: Top 5 Pie Chart

top5 = df.nlargest(5, 'Emission')

plt.figure(figsize=(6,6))
plt.pie(top5['Emission'], labels=top5['Industry'], autopct='%1.1f%%')
plt.title("Top 5 Emission Contribution")
plt.tight_layout()
plt.show()


# STEP 10: Average Emission

avg_emission = df['Emission'].mean()
print("\nAverage Emission:", avg_emission)