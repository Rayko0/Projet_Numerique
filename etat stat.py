import numpy as np
import matplotlib.pyplot as plt

# Paramètres
hbar = 1
m = 1
L = 2.0
nx = 1000
dx = L / nx
x = np.linspace(0, L, nx)

# Potentiel en marche (exemple)
V0 = -4000
V = np.zeros(nx)
V[(x >= 0.8) & (x <= 0.9)] = V0

# Construction de la matrice Hamiltonienne
diag = np.ones(nx) * (1 / dx**2)
off_diag = np.ones(nx - 1) * (-0.5 / dx**2)

H = np.diag(0.5 * diag + V) + np.diag(off_diag, 1) + np.diag(off_diag, -1)

# Résolution du problème aux valeurs propres
E, psi = np.linalg.eigh(H)

# Normalisation
psi[:,0] = psi[:,0] / np.sqrt(np.sum(psi[:,0]**2) * dx)

# Affichage du premier état stationnaire
plt.plot(x, psi[:,0]**2, label=f"État fondamental, E ≈ {E[0]:.2f}")
plt.plot(x, V / np.abs(V0) * np.max(psi[:,0]**2), label="Potentiel (échelle)")
plt.xlabel("x")
plt.ylabel("|ψ(x)|²")
plt.legend()
plt.title("État stationnaire dans un puits de potentiel")
plt.show()
