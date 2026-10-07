import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Non-Structural Element (NSE) Damage Assessment
# -------------------------------------------------

storeys = np.arange(1, 7)

# Inter-storey drift ratios obtained from
# the simplified building model
drift_ratio = np.array([
    0.007441,
    0.007153,
    0.006500,
    0.005322,
    0.003769,
    0.001950
])

# Illustrative drift-based damage thresholds
# for a hypothetical drift-sensitive NSE
slight_damage = 0.002
moderate_damage = 0.005
severe_damage = 0.010

# Classify damage state
damage_state = []

for drift in drift_ratio:

    if drift < slight_damage:
        damage_state.append("No / Very Low Damage")

    elif drift < moderate_damage:
        damage_state.append("Slight Damage")

    elif drift < severe_damage:
        damage_state.append("Moderate Damage")

    else:
        damage_state.append("Severe Damage")


# Print results
print("NSE Drift-Based Damage Assessment")
print("-" * 45)

for i in range(len(storeys)):

    print(
        f"Storey {storeys[i]}: "
        f"Drift = {drift_ratio[i]:.4f} "
        f"({drift_ratio[i] * 100:.3f}%), "
        f"Damage State = {damage_state[i]}"
    )


# Plot drift profile with thresholds
plt.figure(figsize=(7, 7))

plt.plot(
    drift_ratio * 100,
    storeys,
    marker="o",
    label="Storey Drift"
)

plt.axvline(
    slight_damage * 100,
    linestyle="--",
    label="Slight Damage Threshold"
)

plt.axvline(
    moderate_damage * 100,
    linestyle="--",
    label="Moderate Damage Threshold"
)

plt.axvline(
    severe_damage * 100,
    linestyle="--",
    label="Severe Damage Threshold"
)

plt.xlabel("Inter-Storey Drift Ratio (%)")
plt.ylabel("Storey")
plt.title("Drift-Based NSE Damage Assessment")

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "nse_damage_assessment.png",
    dpi=300
)

plt.show()
