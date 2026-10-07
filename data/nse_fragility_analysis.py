import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# NSE Fragility Analysis
# Preliminary / Illustrative Model
# -------------------------------------------------

# Drift demand levels
drift = np.linspace(0.001, 0.015, 100)

# Illustrative median drift capacities
# for different NSE damage states
median_slight = 0.003
median_moderate = 0.006
median_severe = 0.010

# Dispersion parameter
beta = 0.40

# Lognormal fragility function
def fragility_probability(drift, median_capacity, beta):
    return 0.5 * (
        1 + np.erf(
            np.log(drift / median_capacity) /
            (beta * np.sqrt(2))
        )
    )


# Calculate exceedance probabilities
P_slight = fragility_probability(
    drift, median_slight, beta
)

P_moderate = fragility_probability(
    drift, median_moderate, beta
)

P_severe = fragility_probability(
    drift, median_severe, beta
)


# -------------------------------------------------
# Plot fragility curves
# -------------------------------------------------

plt.figure(figsize=(8, 6))

plt.plot(
    drift * 100,
    P_slight,
    label="Slight Damage"
)

plt.plot(
    drift * 100,
    P_moderate,
    label="Moderate Damage"
)

plt.plot(
    drift * 100,
    P_severe,
    label="Severe Damage"
)

plt.xlabel("Inter-Storey Drift Ratio (%)")
plt.ylabel("Probability of Exceedance")
plt.title("Illustrative NSE Fragility Curves")

plt.ylim(0, 1)
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    "nse_fragility_curves.png",
    dpi=300
)

plt.show()
