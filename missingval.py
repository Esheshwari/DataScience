import math

# Given data
n_women = 45
n_men = None
n_child = 20
n_total = 100

mean_women = 16
mean_men = None
mean_child = 7.5
mean_total = 15

sd_women = math.sqrt(6)
sd_men = None
sd_child = math.sqrt(3)
sd_total = math.sqrt(19.55)

# --------------------------------
# 1. Find missing n
# --------------------------------
n_men = n_total - n_women - n_child

# --------------------------------
# 2. Find missing Mean
# --------------------------------
mean_men = (
    (n_total * mean_total)
    - (n_women * mean_women)
    - (n_child * mean_child)
) / n_men

# --------------------------------
# 3. Find missing SD
# --------------------------------
# Combined variance formula:
# total variance = sum[n * (variance + (mean - combined_mean)^2)] / N

total_variance = sd_total ** 2

known_variance = (
    n_women * (sd_women ** 2 + (mean_women - mean_total) ** 2)
    + n_child * (sd_child ** 2 + (mean_child - mean_total) ** 2)
)

missing_variance = (
    (n_total * total_variance - known_variance) / n_men
    - (mean_men - mean_total) ** 2
)

sd_men = math.sqrt(missing_variance)

# --------------------------------
# Display results
# --------------------------------
print("========== MISSING VALUES ==========")

print("Men's Wear n =", n_men)
print("Men's Wear Mean =", mean_men)
print("Men's Wear SD =", sd_men)

n_women = 45
n_men = 35
n_child = 20

mean_women = 16
mean_men = 18
mean_child = 7.5

combined_mean = (
    n_women * mean_women +
    n_men * mean_men +
    n_child * mean_child
) / (n_women + n_men + n_child)

print("Combined Mean =", combined_mean)
