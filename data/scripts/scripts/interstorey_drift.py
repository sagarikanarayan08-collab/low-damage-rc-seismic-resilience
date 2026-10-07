import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Inter-Storey Drift Analysis
# 6-Storey RC Building
# -------------------------------------------------

# Storey numbers
storeys = np.arange(1, 7)

# Storey height
storey_height = 3.2  # m

# Maximum storey displacements obtained
# from the simplified seismic response model
max_displacement = np.array([
    0.02381,
    0.04670,
    0.06750,
    0.08453,
    0.09659,
    0.10283
])

# Calculate inter-storey displacement
interstorey_displacement = np.diff(
    np.insert(max_displacement, 0, 0)
)

# Calculate inter-storey drift ratio
drift_ratio = interstorey_displacement / storey_height

# Print results
print("Inter-Storey Drift Analysis")
print("-" * 35)

for i in range(len(storeys)):
    print(
        f"Storey {storeys[i]}: "
        f"Displacement = {max_displacement[i]:.5f} m, "
        f"Drift Ratio = {drift_ratio[i]:.6f}"
    )

# Maximum drift
max_drift = np.max(drift_ratio)
max_drift_storey = np.argmax(drift_ratio) + 1

print("\nMaximum Drift Ratio:")
print(f"Storey {max_drift_storey}: {max_drift:.6f}")

# Plot drift profile
plt.figure(figsize=(6, 7))

plt.plot(
    drift_ratio,
    storeys,
    marker="o"
)

plt.xlabel("Inter-Storey Drift Ratio")
plt.ylabel("Storey")
plt.title("Inter-Storey Drift Profile")

plt.grid(True)
plt.tight_layout()

# Save figure
plt.savefig(
    "seismic_drift_profile.png",
    dpi=300
)

plt.show()
