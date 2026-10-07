import numpy as np
import matplotlib.pyplot as plt

# Time parameters
dt = 0.01
time = np.arange(0, 20, dt)

# Illustrative ground acceleration (m/s²)
ground_acc = (
    0.8 * np.sin(2 * np.pi * 1.2 * time)
    + 0.4 * np.sin(2 * np.pi * 2.1 * time)
) * np.exp(-0.08 * time)

# SDOF system properties
mass = 1.0
natural_period = 1.0
damping_ratio = 0.05

# Natural frequency
omega = 2 * np.pi / natural_period

# Stiffness and damping
stiffness = mass * omega**2
damping = 2 * damping_ratio * mass * omega

# Initialize response
displacement = np.zeros(len(time))
velocity = np.zeros(len(time))
acceleration = np.zeros(len(time))

# Numerical time integration
for i in range(1, len(time)):
    restoring_force = stiffness * displacement[i-1]
    damping_force = damping * velocity[i-1]

    acceleration[i] = (
        -ground_acc[i]
        - damping_force / mass
        - restoring_force / mass
    )

    velocity[i] = velocity[i-1] + acceleration[i] * dt
    displacement[i] = displacement[i-1] + velocity[i] * dt

# Plot displacement response
plt.figure(figsize=(10, 4))

plt.plot(time, displacement)

plt.xlabel("Time (s)")
plt.ylabel("Relative Displacement (m)")
plt.title("SDOF Seismic Response")

plt.grid(True)
plt.tight_layout()

plt.savefig("sdof_response.png", dpi=300)
plt.show()
