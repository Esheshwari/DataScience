import pandas as pd

# Given CIE marks
cie1 = [20, 15, 16, 19.20]
cie2 = [17, 23, 24, 24, 20]
cie3 = [23, 20, 20, 24]

# Store all CIE marks in a DataFrame
df = pd.DataFrame({
    "CIE 1": pd.Series(cie1),
    "CIE 2": pd.Series(cie2),
    "CIE 3": pd.Series(cie3)
})

print("=============== CIE DATA ===============")
print(df)

# Combine all three CIEs into ONE dataset
all_marks = pd.concat([
    df["CIE 1"],
    df["CIE 2"],
    df["CIE 3"]
], ignore_index=True).dropna()

print("\n=============== ALL CIE MARKS ===============")
print(all_marks)

# Statistics on the combined dataset
print("\n=============== STATISTICS ===============")

print("Mean:", all_marks.mean())
print("Median:", all_marks.median())
print("Mode:", all_marks.mode().tolist())
print("Variance:", all_marks.var())
print("Standard Deviation:", all_marks.std())
print("Minimum:", all_marks.min())
print("Maximum:", all_marks.max())

print("\n=============== DESCRIPTIVE STATISTICS ===============")
print(all_marks.describe())
