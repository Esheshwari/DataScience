import pandas as pd

# Read CSV dataset
df = pd.read_csv(r"D:\Data-Science\employees.csv")

print("================ ORIGINAL DATASET ================")
print(df)

# Dataset information
print("\n================ DATASET INFORMATION ================")
df.info()

# Missing values
print("\n================ MISSING VALUES ================")
print(df.isnull().sum())

# Fill missing numerical values with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Fill missing categorical values
df["City"] = df["City"].fillna("Unknown")

# Check duplicate records
print("\n================ DUPLICATE RECORDS ================")
print("Duplicate rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Remove extra spaces
df["City"] = df["City"].str.strip()

# Standardize city names
df["City"] = df["City"].str.title()

print("\n================ CLEANED DATASET ================")
print(df)

# Final missing-value check
print("\n================ FINAL MISSING VALUES ================")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv(
    r"D:\Data-Science\cleaned_employees.csv",
    index=False
)

print("\nCleaned dataset saved successfully.")

import pandas as pd

# Read cleaned dataset
df = pd.read_csv(r"D:\Data-Science\cleaned_employees.csv")

print("================ CLEANED DATASET ================")
print(df)

# ------------------------------------------------
# FILTERING
# ------------------------------------------------

print("\n================ SALARY > 45000 ================")

filtered = df[df["Salary"] > 45000]
print(filtered)

# ------------------------------------------------
# SORTING
# ------------------------------------------------

print("\n================ SORTED BY SALARY ================")

sorted_df = df.sort_values(
    by="Salary",
    ascending=False
)

print(sorted_df)

# ------------------------------------------------
# GROUPING
# ------------------------------------------------

print("\n================ GROUPED BY DEPARTMENT ================")

grouped = df.groupby("Department")

print(grouped["Salary"].mean())

# ------------------------------------------------
# AGGREGATION
# ------------------------------------------------

print("\n================ AGGREGATION ================")

aggregation = df.groupby("Department")["Salary"].agg(
    ["sum", "mean", "min", "max", "count"]
)

print(aggregation)

# ------------------------------------------------
# PIVOT TABLE
# ------------------------------------------------

print("\n================ PIVOT TABLE ================")

pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="City",
    aggfunc="mean"
)

print(pivot)

# ------------------------------------------------
# MELT
# ------------------------------------------------

print("\n================ MELTED DATASET ================")

melted = pd.melt(
    df,
    id_vars=["ID", "Name"],
    value_vars=["Department", "City"]
)

print(melted)

print("\nData wrangling completed successfully.")

import pandas as pd

# Read cleaned dataset
df = pd.read_csv(r"D:\Data-Science\cleaned_employees.csv")

print("================ STATISTICS ================")

# AGE
print("\n---------- AGE ----------")

print("Mean:", df["Age"].mean())
print("Median:", df["Age"].median())
print("Mode:", df["Age"].mode()[0])
print("Variance:", df["Age"].var())
print("Standard Deviation:", df["Age"].std())
print("Minimum:", df["Age"].min())
print("Maximum:", df["Age"].max())

# SALARY
print("\n---------- SALARY ----------")

print("Mean:", df["Salary"].mean())
print("Median:", df["Salary"].median())
print("Mode:", df["Salary"].mode()[0])
print("Variance:", df["Salary"].var())
print("Standard Deviation:", df["Salary"].std())
print("Minimum:", df["Salary"].min())
print("Maximum:", df["Salary"].max())

# Complete statistical summary
print("\n================ DESCRIPTIVE STATISTICS ================")

print(df[["Age", "Salary"]].describe())
