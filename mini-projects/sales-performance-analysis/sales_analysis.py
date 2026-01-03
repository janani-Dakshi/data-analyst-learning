import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
data = {
    "Region": ["North", "South", "East", "West"],
    "Amount": [12000, 18000, 10000, 15000]
}

monthly_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Amount": [8000, 12000, 15000, 20000]
}

df_region = pd.DataFrame(data)
df_month = pd.DataFrame(monthly_data)

# 1. Bar chart: Sales by Region
ax = df_region.plot(
    x="Region",
    y="Amount",
    kind="bar",
    title="Total Sales by Region",
    legend=False
)

total = df_region["Amount"].sum()

for bar in ax.patches:
    value = bar.get_height()
    percentage = (value / total) * 100
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value,
        f"₹{int(value)}\n({percentage:.1f}%)",
        ha="center",
        va="bottom"
    )

plt.xlabel("Region")
plt.ylabel("Sales Amount")
plt.tight_layout()
plt.savefig(
    "mini-projects/sales-performance-analysis/images/sales_by_region.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


# 2. Line chart: Monthly Sales Trend
df_month.plot(
    x="Month",
    y="Amount",
    kind="line",
    marker="o",
    title="Monthly Sales Trend"
)

plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.tight_layout()
plt.savefig(
    "mini-projects/sales-performance-analysis/images/monthly_sales_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


# 3. Histogram: Sales Distribution
df_region["Amount"].plot(
    kind="hist",
    bins=5,
    title="Distribution of Sales Amount"
)

plt.xlabel("Sales Amount")
plt.tight_layout()
plt.savefig(
    "mini-projects/sales-performance-analysis/images/sales_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

