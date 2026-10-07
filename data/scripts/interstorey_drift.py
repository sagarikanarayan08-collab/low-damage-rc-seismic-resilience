import numpy as np
import matplotlib.pyplot as plt

# Maximum displacement obtained from the 6-storey seismic model
# Values are illustrative outputs from the simplified model

storeys = np.arange(1, 7)
storey_height = 3.2

max_displacement = np.array([
    0.0000,
    0.0000,
    0.0000,
    0.0000,
    0.0000,
    0.0000
])

# Calculate inter-storey displacement
interstorey_displacement = np.diff(
    np.insert(max_displacement, 0, 0)
)

# Calculate inter-storey drift ratio
drift_ratio = interstorey_displacement / storey_height

print("Inter-Storey Drift Ratios:")

for i, drift in enumerate(drift_ratio, 1):
    print(f"Storey {i}: {drift:.6f}")

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

plt.savefig(
    "seismic_drift_profile.png",
    dpi=300
)

plt.show()
