import pandas as pd
import re

# =========================================================
# 1. LOAD DATA
# =========================================================

df = pd.read_excel(
    r"D:\Data-Science\customers-1000(cleaned).xlsx"
)

print("Original Shape:", df.shape)


# =========================================================
# 2. REMOVE UNNECESSARY COLUMNS
# =========================================================

df = df.drop(
    columns=[
        "Unnamed: 15",
        "Unnamed: 16",
        "Country.1",
        "code"
    ],
    errors="ignore"
)


# =========================================================
# 3. REMOVE COMPLETELY DUPLICATE ROWS
# =========================================================

df = df.drop_duplicates()


# =========================================================
# 4. REMOVE DUPLICATE CUSTOMER IDs
# =========================================================

df = df.drop_duplicates(
    subset=["Customer Id"],
    keep="first"
)


# =========================================================
# 5. CLEAN TEXT COLUMNS
# =========================================================

text_columns = [
    "Customer Id",
    "First Name",
    "Last Name",
    "Company",
    "City",
    "Country",
    "Phone 1",
    "Phone 1 clean",
    "Phone 2",
    "Phone 2 clean",
    "Email",
    "Website"
]

for col in text_columns:
    df[col] = df[col].astype("string").str.strip()


# =========================================================
# 6. CLEAN EMAIL
# =========================================================

df["Email"] = df["Email"].str.lower()

email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

df["Email Valid"] = df["Email"].str.match(
    email_pattern,
    na=False
)


# =========================================================
# 7. CLEAN PHONE NUMBERS
# =========================================================

df["Phone 1 clean"] = (
    df["Phone 1 clean"]
    .astype("string")
    .str.replace(r"\D", "", regex=True)
)

df["Phone 2 clean"] = (
    df["Phone 2 clean"]
    .astype("string")
    .str.replace(r"\D", "", regex=True)
)


# =========================================================
# 8. CONVERT SUBSCRIPTION DATE
# =========================================================

df["Subscription Date"] = pd.to_datetime(
    df["Subscription Date"],
    errors="coerce"
)


# =========================================================
# 9. FINAL VALIDATION
# =========================================================

print("\n================ FINAL DATA CHECK ================")

print("\nFinal Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDuplicate Customer IDs:")
print(df["Customer Id"].duplicated().sum())

print("\nInvalid Emails:")
print((~df["Email Valid"]).sum())

print("\nInvalid Dates:")
print(df["Subscription Date"].isnull().sum())


# =========================================================
# 10. SHOW PHONE EXAMPLES
# =========================================================

print("\nPhone 1 Examples:")
print(df[["Country", "Phone 1 clean"]].head(10))

print("\nPhone 2 Examples:")
print(df[["Country", "Phone 2 clean"]].head(10))


# =========================================================
# 11. SAVE FINAL CLEANED DATA
# =========================================================
df = df.drop(
    columns=[
        "Phone 1",
        "Phone 2",
        "Email Valid"
    ],
    errors="ignore"
)

output_file = r"D:\Data-Science\customers-1000-final.csv"

df.to_csv(output_file, index=False)

print("Final Shape:", df.shape)
print("Final file saved:", output_file)
