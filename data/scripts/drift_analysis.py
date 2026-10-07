import numpy as np
import matplotlib.pyplot as plt

# Example storey data
storeys = np.arange(1, 7)

# Placeholder displacement values (m)
displacement = np.array([
    0.008,
    0.021,
    0.038,
    0.057,
    0.074,
    0.089
])

# Storey height
h = 3.2

# Calculate approximate inter-storey drift ratio
drift = np.diff(np.insert(displacement, 0, 0)) / h

print("Inter-storey drift ratios:")
for i, value in enumerate(drift, 1):
    print(f"Storey {i}: {value:.4f}")

plt.plot(drift, storeys, marker="o")
plt.xlabel("Inter-storey Drift Ratio")
plt.ylabel("Storey")
plt.title("Inter-storey Drift Profile")
plt.grid(True)
plt.show()
