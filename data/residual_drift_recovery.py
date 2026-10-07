import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Residual Drift and Post-Earthquake Recovery
# Preliminary / Illustrative Model
# -------------------------------------------------

# Time after earthquake (hours)
time = np.array([
    0,
    6,
    12,
    24,
    48,
    72,
    120,
    168
])

# Illustrative residual drift (%)
residual_drift = np.array([
    0.80,
    0.72,
    0.62,
    0.50,
    0.35,
    0.22,
    0.10,
    0.04
])

# -------------------------------------------------
# Recovery Index
# -------------------------------------------------

initial_drift = residual_drift[0]

recovery_index = (
    1 - residual_drift / initial_drift
) * 100

# -------------------------------------------------
# Print results
# -------------------------------------------------

print("Post-Earthquake Residual Drift Assessment")
print("-" * 50)

for i in range(len(time)):
    print(
        f"Time = {time[i]:>3} h | "
        f"Residual Drift = {residual_drift[i]:.2f}% | "
        f"Recovery Index = {recovery_index[i]:.1f}%"
    )

# -------------------------------------------------
# Plot residual drift
# -------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    time,
    residual_drift,
    marker="o"
)

plt.xlabel("Time After Earthquake (hours)")
plt.ylabel("Residual Drift (%)")
plt.title("Post-Earthquake Residual Drift")

plt.grid(True)
plt.tight_layout()

plt.savefig(
    "residual_drift_recovery.png",
    dpi=300
)

plt.show()
