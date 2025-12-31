import pandas as pd
import matplotlib.pyplot as plt

# Simulated healthcare coding dataset
data = {
    "coder_name": ["Asha", "Ravi", "Asha", "Meena", "Ravi", "Meena", "Asha"],
    "chart_id": [101, 102, 103, 104, 105, 106, 107],
    "tat_days": [2, 5, 3, 1, 4, 2, 6],
    "status": ["Completed", "Completed", "Completed", "Completed", "Completed", "Completed", "Completed"]
}

df = pd.DataFrame(data)

# 1. Productivity by coder
productivity = df.groupby("coder_name")["chart_id"].count().sort_values(ascending=False)

ax = productivity.plot(kind="bar", title="Coder Productivity")

for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        int(bar.get_height()),
        ha="center",
        va="bottom"
    )

plt.xlabel("Coder")
plt.ylabel("Charts Completed")
plt.show()

# 2. SLA Performance using CASE-like logic
df["performance"] = df["tat_days"].apply(
    lambda x: "Excellent" if x <= 2 else "Good" if x <= 4 else "Needs Improvement"
)

print(df[["coder_name", "chart_id", "tat_days", "performance"]])

# 3. SLA Breach Analysis
sla_breach = df[df["tat_days"] > 4]

print("\nCharts breaching SLA:")
print(sla_breach[["chart_id", "coder_name", "tat_days"]])
