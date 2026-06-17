# ============================================================
# E-Commerce Business Simulation (30 Days) using NumPy
# Author: Ayaan Pasha
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── Reproducibility ──────────────────────────────────────────
np.random.seed(42)

# ── Simulate 30 Days of Data ─────────────────────────────────
days       = np.arange(1, 31)
customers  = np.random.poisson(lam=100,  size=30)           # Daily visitors
purchase   = np.random.normal(loc=1500,  scale=300, size=30) # Avg basket (₹)
delivery   = np.random.poisson(lam=3,    size=30)            # Delivery days
waiting    = np.random.exponential(scale=2, size=30)         # Hours between orders
quality    = np.random.binomial(n=1,     p=0.9,  size=30)   # 1=Pass, 0=Fail

products   = np.random.multinomial(
    n=30, pvals=[0.3, 0.3, 0.2, 0.2]
)  # [Electronics, Clothing, Food, Books]

# ── Build DataFrame ───────────────────────────────────────────
df = pd.DataFrame({
    "Day":            days,
    "Customers":      customers,
    "Avg_Purchase":   purchase.round(2),
    "Delivery_Days":  delivery,
    "Waiting_Hours":  waiting.round(2),
    "Quality_Pass":   quality,
    "Daily_Revenue":  (customers * purchase).round(2),
})

# ── Summary Statistics ────────────────────────────────────────
print("=" * 55)
print("      E-COMMERCE 30-DAY SIMULATION REPORT")
print("=" * 55)
print(f"  Total Revenue       : ₹{df['Daily_Revenue'].sum():,.2f}")
print(f"  Avg Daily Revenue   : ₹{df['Daily_Revenue'].mean():,.2f}")
print(f"  Avg Daily Customers : {df['Customers'].mean():.1f}")
print(f"  Avg Purchase Amount : ₹{df['Avg_Purchase'].mean():.2f}")
print(f"  Avg Delivery Time   : {df['Delivery_Days'].mean():.1f} days")
print(f"  Quality Pass Rate   : {df['Quality_Pass'].mean()*100:.1f}%")
print(f"  Quality Fail Days   : {(df['Quality_Pass']==0).sum()} out of 30")
print("=" * 55)

print("\nProduct Category Distribution (out of 30 units):")
categories = ["Electronics", "Clothing", "Food", "Books"]
for cat, count in zip(categories, products):
    bar = "█" * count
    print(f"  {cat:<15}: {bar} ({count})")

print("\nFirst 5 Days Preview:")
print(df.head().to_string(index=False))

# ── Export CSV ────────────────────────────────────────────────
os.makedirs("outputs", exist_ok=True)
df.to_csv("outputs/simulation_data.csv", index=False)
print("\n✅ Data exported to outputs/simulation_data.csv")

# ── Visualizations ────────────────────────────────────────────
sns.set_theme(style="darkgrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 9))
fig.suptitle("E-Commerce 30-Day Business Simulation", fontsize=16, fontweight="bold")

# 1. Daily Revenue Trend
axes[0, 0].plot(df["Day"], df["Daily_Revenue"], color="#4C72B0", linewidth=2, marker="o", markersize=4)
axes[0, 0].fill_between(df["Day"], df["Daily_Revenue"], alpha=0.2, color="#4C72B0")
axes[0, 0].set_title("Daily Revenue (₹)")
axes[0, 0].set_xlabel("Day")
axes[0, 0].set_ylabel("Revenue (₹)")

# 2. Customer Traffic
axes[0, 1].bar(df["Day"], df["Customers"], color="#55A868", alpha=0.85)
axes[0, 1].axhline(df["Customers"].mean(), color="red", linestyle="--", linewidth=1.5, label=f'Avg: {df["Customers"].mean():.0f}')
axes[0, 1].set_title("Daily Customer Traffic")
axes[0, 1].set_xlabel("Day")
axes[0, 1].set_ylabel("Customers")
axes[0, 1].legend()

# 3. Product Category Distribution
axes[1, 0].bar(categories, products, color=["#4C72B0","#55A868","#C44E52","#8172B2"], alpha=0.9)
axes[1, 0].set_title("Product Category Demand")
axes[1, 0].set_xlabel("Category")
axes[1, 0].set_ylabel("Units Sold")

# 4. Purchase Amount Distribution
axes[1, 1].hist(df["Avg_Purchase"], bins=10, color="#C44E52", alpha=0.8, edgecolor="white")
axes[1, 1].axvline(df["Avg_Purchase"].mean(), color="black", linestyle="--", linewidth=1.5, label=f'Mean: ₹{df["Avg_Purchase"].mean():.0f}')
axes[1, 1].set_title("Purchase Amount Distribution (₹)")
axes[1, 1].set_xlabel("Amount (₹)")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].legend()

plt.tight_layout()
plt.savefig("outputs/simulation_charts.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Charts saved to outputs/simulation_charts.png")
