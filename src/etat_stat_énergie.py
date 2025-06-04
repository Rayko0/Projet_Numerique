import numpy as np
import matplotlib.pyplot as plt

L = 10.0
nx = 1000
dx = L / nx
x = np.linspace(-L/2, L/2, nx)

#Potentiel : puits entre -1 et 1
V0 = -400
V = np.zeros(nx)
V[(x >= -1) & (x <= 1)] = V0

#hamiltonien
coeff = 1 / (2 * dx**2)
main_diag = np.ones(nx) * (2 * coeff) + V
off_diag = np.ones(nx - 1) * (-coeff)
H = np.diag(main_diag) + np.diag(off_diag, 1) + np.diag(off_diag, -1)

#Diagonalisation du hamiltonien
E, psi = np.linalg.eigh(H)

#Tracé des courbes
plt.figure(figsize=(8,6))
plt.plot(x, V, color='black', label='Potentiel')

n_states = 5  # Nombre d'états à afficher
colors = ['orange', 'green', 'red', 'purple', 'blue']

for n in range(n_states):
    psi_n = psi[:, n]
    psi_n /= np.sqrt(np.sum(psi_n**2) * dx)  # normalisation
    scale = 5  # pour étirer visuellement la fonction d'onde
    plt.plot(x, psi_n**2 * scale + E[n], label=f"E={E[n]:.2f}", color=colors[n])

plt.xlabel("x")
plt.ylabel("Énergie")
plt.title("Fonctions d’onde stationnaires")
plt.legend()
plt.grid(True)
plt.show()
