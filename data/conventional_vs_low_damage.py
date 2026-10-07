import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Conventional vs Low-Damage RC Building
# Preliminary / Illustrative Comparison
# -------------------------------------------------

storeys = np.arange(1, 7)

# Maximum storey displacement from the
# simplified conventional RC model (m)
conventional = np.array([
    0.02381,
    0.04670,
    0.06750,
    0.08453,
    0.09659,
    0.10283
])

# Illustrative reduced displacement response
# for a low-damage structural system
low_damage = np.array([
    0.01600,
    0.03100,
    0.04500,
    0.05700,
    0.06600,
    0.07100
])

# -------------------------------------------------
# Calculate reduction
# -------------------------------------------------

reduction = (
    (conventional - low_damage)
    / conventional
) * 100

print("Conventional vs Low-Damage RC Comparison")
print("-" * 55)

for i in range(len(storeys)):
    print(
        f"Storey {storeys[i]}: "
        f"Conventional = {conventional[i]:.5f} m | "
        f"Low-Damage = {low_damage[i]:.5f} m | "
        f"Reduction = {reduction[i]:.1f}%"
    )

# -------------------------------------------------
# Plot displacement profiles
# -------------------------------------------------

plt.figure(figsize=(7, 7))

plt.plot(
    conventional,
    storeys,
    marker="o",
    label="Conventional RC"
)

plt.plot(
    low_damage,
    storeys,
    marker="s",
    label="Low-Damage RC"
)

plt.xlabel("Maximum Storey Displacement (m)")
plt.ylabel("Storey")
plt.title("Conventional vs Low-Damage RC Response")

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig(
    "conventional_vs_low_damage.png",
    dpi=300
)

plt.show()
