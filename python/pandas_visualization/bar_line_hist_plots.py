import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Region": ["North", "South", "East", "West"],
    "Amount": [12000, 18000, 10000, 15000]
}

df = pd.DataFrame(data)

# Bar Chart
ax = df.plot(
    x="Region",
    y="Amount",
    kind="bar",
    title="Total Sales by Region"
)

for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{int(bar.get_height())}',
        ha='center',
        va='bottom'
    )

plt.xlabel("Region")
plt.ylabel("Amount")
plt.show()

# Histogram
df["Amount"].plot(kind="hist", bins=5, title="Sales Distribution")
plt.show()
