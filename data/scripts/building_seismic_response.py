import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# 6-Storey RC Building - Seismic Response
# Simplified linear dynamic model
# -------------------------------------------------

n_storeys = 6
dt = 0.01
duration = 20

time = np.arange(0, duration, dt)

# Illustrative earthquake ground acceleration
ground_acc = (
    0.8 * np.sin(2 * np.pi * 1.2 * time)
    + 0.4 * np.sin(2 * np.pi * 2.1 * time)
) * np.exp(-0.08 * time)

# Building properties
mass = 2.5e5
storey_stiffness = 2.0e8
damping_ratio = 0.05

# Mass matrix
M = np.eye(n_storeys) * mass

# Stiffness matrix
K = np.zeros((n_storeys, n_storeys))

for i in range(n_storeys):

    if i == 0:
        K[i, i] += storey_stiffness

    else:
        K[i, i] += storey_stiffness
        K[i-1, i-1] += storey_stiffness
        K[i, i-1] -= storey_stiffness
        K[i-1, i] -= storey_stiffness


# Eigenvalue analysis
eigenvalues, eigenvectors = np.linalg.eig(
    np.linalg.inv(M) @ K
)

idx = np.argsort(eigenvalues)

eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

omega = np.sqrt(eigenvalues)

# Fundamental circular frequency
omega_1 = omega[0]

# Approximate damping matrix
C = 2 * damping_ratio * omega_1 * M


# Initialize response
u = np.zeros((n_storeys, len(time)))
v = np.zeros((n_storeys, len(time)))
a = np.zeros((n_storeys, len(time)))

# Influence vector
r = np.ones(n_storeys)

# Time integration
for j in range(1, len(time)):

    effective_force = -M @ r * ground_acc[j]

    restoring_force = K @ u[:, j-1]
    damping_force = C @ v[:, j-1]

    a[:, j] = np.linalg.solve(
        M,
        effective_force - restoring_force - damping_force
    )

    v[:, j] = v[:, j-1] + a[:, j] * dt

    u[:, j] = u[:, j-1] + v[:, j] * dt


# Maximum displacement at each storey
max_displacement = np.max(np.abs(u), axis=1)

print("Maximum Storey Displacements:")

for i, value in enumerate(max_displacement, 1):
    print(f"Storey {i}: {value:.5f} m")


# Plot maximum displacement profile
storeys = np.arange(1, n_storeys + 1)

plt.figure(figsize=(6, 7))

plt.plot(
    max_displacement,
    storeys,
    marker="o"
)

plt.xlabel("Maximum Displacement (m)")
plt.ylabel("Storey")
plt.title("Maximum Storey Displacement Profile")

plt.grid(True)
plt.tight_layout()

plt.savefig(
    "maximum_storey_displacement.png",
    dpi=300
)

plt.show()
