import numpy as np
import matplotlib.pyplot as plt

#plan 
L = 2.0
nx = 1000
dx = L / nx
x = np.linspace(0, L, nx)

#Potentiel : puits entre x = 0.8 et 0.9
V0 = -400
V = np.zeros(nx)
V[(x >= 0.8) & (x <= 0.9)] = V0

#hamiltonien
coeff = 1 / (2 * dx**2)
main_diag = np.ones(nx) * (2 * coeff) + V
off_diag = np.ones(nx - 1) * (-coeff)
H = np.diag(main_diag) + np.diag(off_diag, 1) + np.diag(off_diag, -1)

#Diagonalisation du hamiltonien
E, psi = np.linalg.eigh(H)

#Etat propres
psi0 = psi[:, 0]
psi1 = psi[:, 1]
psi0 /= np.sqrt(np.sum(psi0**2) * dx)
psi1 /= np.sqrt(np.sum(psi1**2) * dx)

#Tracé des courbes
plt.plot(x, psi0**2, label=f"État fondamental, E ≈ {E[0]:.2f}", color="blue")
plt.plot(x, psi1**2, label=f"1er état excité, E ≈ {E[1]:.2f}", color="green")
plt.plot(x, V / np.abs(V0) * np.max(psi0**2), label="Potentiel (échelle)", color="orange")
plt.xlabel("x")
plt.ylabel("|ψ(x)|²")
plt.title("Deux premiers états stationnaires dans un puits de potentiel")
plt.legend()
plt.grid(True)
plt.show()
