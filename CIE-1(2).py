import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 1. CREATE DATASET
# ============================================================

data = {
    "Year": list(range(1999, 2023)),

    "Revenue": [
        13.3, 14.2, 14.9, 15.4, 17.1, 18.6,
        19.1, 20.9, 22.8, 23.5, 22.7, 24.1,
        27.0, 27.6, 28.1, 27.4, 25.4, 24.6,
        22.8, 21.3, 21.4, 19.2, 23.2, 23.2
    ],

    "Growth_Rate": [
        None, 7, 4, 4, 11, 8, 3, 9, 9, 3,
        -3, 6, 12, 2, 2, -2, -7, -3, -7,
        -7, 1, -10, 21, 0
    ],

    "Q1": [
        None, None, None, None, 3.8, 4.4, 4.8, 4.9,
        5.3, 5.6, 5.1, 5.6, 6.1, 6.5, 6.6, 6.7,
        6.0, 5.9, 5.7, 5.1, 5.0, 4.7, 5.1, 5.7
    ],

    "Q2": [
        None, None, None, None, 4.3, 4.7, 5.1, 5.4,
        5.8, 6.1, 5.6, 5.9, 6.9, 6.9, 7.1, 7.2,
        6.5, 6.3, 6.0, 5.4, 5.3, 3.8, 5.9, 5.7
    ],

    "Q3": [
        None, None, None, None, 4.5, 4.9, 5.3, 5.5,
        5.9, 6.3, 6.0, 6.3, 7.2, 7.2, 7.3, 7.0,
        6.6, 6.4, 5.8, 5.4, 5.6, 5.4, 6.2, 5.9
    ],

    "Q4": [
        None, None, None, 3.0, 4.6, 4.5, 3.9, 5.1,
        5.8, 5.6, 6.0, 6.2, 6.8, 7.0, 7.1, 6.6,
        6.3, 6.0, 5.3, 5.4, 5.4, 5.3, 6.0, 5.9
    ]
}

df = pd.DataFrame(data)


# ============================================================
# 2. PREPROCESSING
# ============================================================

print("=" * 60)
print("DATASET")
print("=" * 60)
print(df)

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)
print(df.isnull().sum())

print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)
print(df.duplicated().sum())


# ============================================================
# 3. DESCRIPTIVE STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)

print(df[["Revenue", "Growth_Rate"]].describe())


# ============================================================
# 4. MAXIMUM AND MINIMUM
# ============================================================

max_revenue = df.loc[df["Revenue"].idxmax()]
min_revenue = df.loc[df["Revenue"].idxmin()]

max_growth = df.loc[df["Growth_Rate"].idxmax()]
min_growth = df.loc[df["Growth_Rate"].idxmin()]

print("\nMAXIMUM REVENUE")
print(max_revenue)

print("\nMINIMUM REVENUE")
print(min_revenue)

print("\nHIGHEST GROWTH")
print(max_growth)

print("\nLOWEST GROWTH")
print(min_growth)


# ============================================================
# 5. QUARTERLY SUM
# ============================================================

# Add Q1 + Q2 + Q3 + Q4
# Only calculate when all four quarters are available

df["Quarterly_Sum"] = (
    df["Q1"] +
    df["Q2"] +
    df["Q3"] +
    df["Q4"]
)

# Difference between quarterly total and annual revenue
df["Quarterly_Difference"] = (
    df["Quarterly_Sum"] - df["Revenue"]
)

print("\n" + "=" * 60)
print("QUARTERLY VS ANNUAL REVENUE")
print("=" * 60)

print(
    df[
        [
            "Year",
            "Revenue",
            "Q1",
            "Q2",
            "Q3",
            "Q4",
            "Quarterly_Sum",
            "Quarterly_Difference"
        ]
    ].dropna()
)


# ============================================================
# 6. REVENUE CHANGE AND CALCULATED GROWTH
# ============================================================

df["Revenue_Change"] = df["Revenue"].diff()

df["Calculated_Growth"] = (
    df["Revenue"].pct_change() * 100
)

print("\n" + "=" * 60)
print("REVENUE CHANGE AND GROWTH")
print("=" * 60)

print(
    df[
        ["Year",
         "Revenue",
         "Revenue_Change",
         "Growth_Rate",
         "Calculated_Growth"]
    ]
)


# ============================================================
# 7. CREATE 8-PLOT DASHBOARD
# ============================================================

fig, axes = plt.subplots(
    4, 2,
    figsize=(16, 18)
)

fig.suptitle(
    "McDonald's Revenue Data Analysis Dashboard",
    fontsize=22,
    fontweight="bold"
)


# ============================================================
# SCROLLABLE 8-PLOT DASHBOARD
# ============================================================

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create main window
root = tk.Tk()
root.title("McDonald's Revenue Data Analysis Dashboard")
root.geometry("1400x900")

# Create scrollable canvas
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window(
    (0, 0),
    window=scrollable_frame,
    anchor="nw"
)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


# ============================================================
# CREATE FIGURE
# ============================================================

fig, axes = plt.subplots(
    8, 1,
    figsize=(13, 32)
)

fig.suptitle(
    "McDonald's Revenue Data Analysis",
    fontsize=20,
    fontweight="bold"
)


# ============================================================
# 1. ANNUAL REVENUE
# ============================================================

axes[0].plot(
    df["Year"],
    df["Revenue"],
    marker="o"
)

axes[0].set_title("1. Annual Revenue Trend")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Revenue ($ Billion)")
axes[0].grid(True)


# ============================================================
# 2. GROWTH RATE
# ============================================================

axes[1].plot(
    df["Year"],
    df["Growth_Rate"],
    marker="o"
)

axes[1].axhline(0, linestyle="--")

axes[1].set_title("2. Revenue Growth Rate")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Growth Rate (%)")
axes[1].grid(True)


# ============================================================
# 3. QUARTERLY REVENUE
# ============================================================

axes[2].plot(
    df["Year"],
    df["Q1"],
    marker="o",
    label="Q1"
)

axes[2].plot(
    df["Year"],
    df["Q2"],
    marker="o",
    label="Q2"
)

axes[2].plot(
    df["Year"],
    df["Q3"],
    marker="o",
    label="Q3"
)

axes[2].plot(
    df["Year"],
    df["Q4"],
    marker="o",
    label="Q4"
)

axes[2].set_title("3. Quarterly Revenue Trends")
axes[2].set_xlabel("Year")
axes[2].set_ylabel("Revenue ($ Billion)")
axes[2].legend()
axes[2].grid(True)


# ============================================================
# 4. YEAR-TO-YEAR CHANGE
# ============================================================

axes[3].bar(
    df["Year"],
    df["Revenue_Change"]
)

axes[3].axhline(0, linestyle="--")

axes[3].set_title("4. Year-to-Year Revenue Change")
axes[3].set_xlabel("Year")
axes[3].set_ylabel("Change ($ Billion)")
axes[3].grid(axis="y")


# ============================================================
# 5. ANNUAL REVENUE VS QUARTERLY SUM
# ============================================================

quarterly_data = df.dropna(
    subset=["Quarterly_Sum"]
)

axes[4].plot(
    quarterly_data["Year"],
    quarterly_data["Revenue"],
    marker="o",
    label="Annual Revenue"
)

axes[4].plot(
    quarterly_data["Year"],
    quarterly_data["Quarterly_Sum"],
    marker="s",
    label="Quarterly Sum"
)

axes[4].set_title("5. Annual Revenue vs Quarterly Sum")
axes[4].set_xlabel("Year")
axes[4].set_ylabel("Revenue ($ Billion)")
axes[4].legend()
axes[4].grid(True)


# ============================================================
# 6. DIFFERENCE
# ============================================================

quarterly_data = df.dropna(
    subset=["Quarterly_Difference"]
)

axes[5].bar(
    quarterly_data["Year"],
    quarterly_data["Quarterly_Difference"]
)

axes[5].axhline(
    0,
    linestyle="--"
)

axes[5].set_title(
    "6. Quarterly Sum − Annual Revenue"
)

axes[5].set_xlabel("Year")
axes[5].set_ylabel("Difference ($ Billion)")
axes[5].grid(axis="y")


# ============================================================
# 7. REVENUE VS GROWTH
# ============================================================

axes[6].scatter(
    df["Revenue"],
    df["Growth_Rate"]
)

axes[6].set_title("7. Revenue vs Growth Rate")
axes[6].set_xlabel("Revenue ($ Billion)")
axes[6].set_ylabel("Growth Rate (%)")
axes[6].grid(True)


# ============================================================
# 8. DISTRIBUTION
# ============================================================

axes[7].hist(
    df["Revenue"].dropna(),
    bins=8
)

axes[7].set_title("8. Distribution of Annual Revenue")
axes[7].set_xlabel("Revenue ($ Billion)")
axes[7].set_ylabel("Frequency")
axes[7].grid(axis="y")


# ============================================================
# ADJUST SPACING
# ============================================================

plt.tight_layout(rect=[0, 0, 1, 0.98], h_pad=3)


# ============================================================
# PUT MATPLOTLIB INSIDE SCROLLABLE WINDOW
# ============================================================

figure_canvas = FigureCanvasTkAgg(
    fig,
    master=scrollable_frame
)

figure_canvas.draw()

figure_canvas.get_tk_widget().pack(
    padx=20,
    pady=20
)


# ============================================================
# MOUSE WHEEL SCROLLING
# ============================================================

def mouse_wheel(event):
    canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )


canvas.bind_all(
    "<MouseWheel>",
    mouse_wheel
)


# ============================================================
# START WINDOW
# ============================================================

root.mainloop()
