import numpy as np
import matplotlib.pyplot as plt

#Const
V0 = 50     # Profondeur du puits
a = 1       # Largeur du puits
E_vals = np.linspace(0.1, 100, 500)

def transmission(E):
    k = np.sqrt(2 * E)
    K = np.sqrt(2 * (E + V0))

    num = 4 * k**2 * K**2
    denom = (k**2 - K**2)**2 * np.sin(K * a)**2 + 4 * k**2 * K**2

    return num / denom

T_vals = transmission(E_vals)

plt.plot(E_vals, T_vals)
plt.xlabel("Énergie (E)")
plt.ylabel("Probabilité de transmission |T|²")
plt.title("Effet Ramsauer-Townsend : transmission / énergie")
plt.grid(True)
plt.show()
