import numpy as np
import matplotlib.pyplot as plt

# Time (seconds)
time = np.linspace(0, 20, 2000)

# Illustrative ground acceleration (m/s²)
acceleration = (
    0.8 * np.sin(2 * np.pi * 1.2 * time)
    + 0.4 * np.sin(2 * np.pi * 2.1 * time)
) * np.exp(-0.08 * time)

# Plot ground motion
plt.figure(figsize=(10, 4))
plt.plot(time, acceleration)

plt.xlabel("Time (s)")
plt.ylabel("Ground Acceleration (m/s²)")
plt.title("Illustrative Earthquake Ground Motion")
plt.grid(True)
plt.tight_layout()

plt.savefig("illustrative_ground_motion.png", dpi=300)
plt.show()
