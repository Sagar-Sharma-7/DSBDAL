# ✅ GDP Analysis - Jupyter Notebook Code

# --------------------------------------
# 1. Import Libraries & Load Dataset
# --------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (adjust path if needed)
df = pd.read_csv('/mnt/data/world_gdp_data.csv', encoding='latin1')

# Preview dataset
print(df.head())


# --------------------------------------
# 2. Bar Graph - Belgium (2006–2024)
# --------------------------------------
# Filter Belgium data
belgium = df[df['country_name'] == 'Belgium']

# Select years 2006–2024
years = [str(year) for year in range(2006, 2025)]
gdp_values = belgium[years].values.flatten()

# Plot bar graph
plt.figure()
plt.bar(years, gdp_values)

plt.title('GDP Growth of Belgium (2006–2024)')
plt.xlabel('Year')
plt.ylabel('GDP Growth (%)')
plt.xticks(rotation=45)

plt.show()


# --------------------------------------
# 3. Pie Chart - GDP Growth (2010)
# --------------------------------------
# Countries to compare
countries = ['India', 'Nepal', 'Romania', 'South Asia', 'Singapore']

# Filter dataset
subset = df[df['country_name'].isin(countries)]

# Remove missing values for clean plot
subset = subset.dropna(subset=['2010'])

# Extract GDP growth values for 2010
gdp_2010 = subset['2010']

# Plot pie chart
plt.figure()
plt.pie(gdp_2010, labels=subset['country_name'], autopct='%1.1f%%')

plt.title('GDP Growth Distribution (2010)')

plt.show()


# --------------------------------------
# Notes:
# - Dataset uses GDP Growth (%) not actual GDP
# - Years are stored as columns
# - Ensure correct column names: 'country_name', '2010', etc.
# --------------------------------------
