import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# 6-Storey RC Building - Simplified Shear Model
# -------------------------------------------------

n_storeys = 6

# Storey height
storey_height = 3.2  # m

# Mass assigned to each storey
mass = 2.5e5  # kg

# Storey stiffness
storey_stiffness = 2.0e8  # N/m

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
eigenvalues, eigenvectors = np.linalg.eig(np.linalg.inv(M) @ K)

# Sort natural frequencies
idx = np.argsort(eigenvalues)
eigenvalues = eigenvalues[idx]

natural_frequencies = np.sqrt(eigenvalues)
periods = 2 * np.pi / natural_frequencies

print("Natural periods of the 6-storey model:")
for i, T in enumerate(periods, 1):
    print(f"Mode {i}: {T:.3f} seconds")

# Plot first-mode shape
mode_shape = eigenvectors[:, idx[0]]
mode_shape = mode_shape / np.max(np.abs(mode_shape))

storeys = np.arange(1, n_storeys + 1)

plt.figure(figsize=(6, 7))
plt.plot(mode_shape, storeys, marker="o")

plt.xlabel("Normalized Lateral Displacement")
plt.ylabel("Storey")
plt.title("First Mode Shape - 6-Storey RC Building")

plt.grid(True)
plt.tight_layout()

plt.savefig("first_mode_shape.png", dpi=300)
plt.show()
