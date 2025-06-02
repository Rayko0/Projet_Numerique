import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

start_time = time.time()

# === Initialisation des paramètres ===
dt = 1E-7
dx = 0.001
nx = int(1 / dx) * 2
nt = 90000
nd = int(nt / 1000) + 1
s = dt / (dx ** 2)

# Paramètres du paquet d'onde
xc = 0.6
sigma = 0.05
A = 1 / (math.sqrt(sigma * math.sqrt(math.pi)))

# Paramètres du potentiel
v0 = -4000
e = 5
E = e * v0
k = math.sqrt(2 * abs(E))

# Grille spatiale
o = np.linspace(0, (nx - 1) * dx, nx)
V = np.zeros(nx)
V[(o >= 0.8) & (o <= 0.9)] = v0  # puits de potentiel

# Initialisation du paquet gaussien
cpt = A * np.exp(1j * k * o - ((o - xc) ** 2) / (2 * (sigma ** 2)))
re = np.real(cpt)
im = np.imag(cpt)

# Tableaux pour la densité
densite = np.zeros((nt, nx))
densite[0, :] = np.abs(cpt) ** 2
final_densite = np.zeros((nd, nx))

# Propagation en temps avec schéma explicite
b = np.zeros(nx)
it = 0
for i in range(1, nt):
    if i % 2 != 0:
        b[1:-1] = im[1:-1]
        im[1:-1] = im[1:-1] + s * (re[2:] + re[:-2]) - 2 * re[1:-1] * (s + V[1:-1] * dt)
        densite[i, 1:-1] = re[1:-1] ** 2 + im[1:-1] * b[1:-1]
    else:
        re[1:-1] = re[1:-1] - s * (im[2:] + im[:-2]) + 2 * im[1:-1] * (s + V[1:-1] * dt)

    if (i - 1) % 1000 == 0:
        it += 1
        final_densite[it][:] = densite[i][:]

# === Animation ===
def init():
    line.set_data([], [])
    return line,

def animate(j):
    line.set_data(o, final_densite[j, :])
    return line,

# === Plot ===
plot_title = "Marche Ascendante avec E/V₀ = " + str(e)
fig = plt.figure()
line, = plt.plot([], [], lw=2)
plt.xlim(0, 2)

# Y-limits calculés automatiquement pour inclure potentiel et densité
plt.ylim(-10,13)
plt.xlim(0,2)

# Tracé du potentiel avec ses vraies valeurs
plt.plot(o, V, label="Potentiel réel", color="orange")
plt.title(plot_title)
plt.xlabel("x")
plt.ylabel("Densité de probabilité de présence")
plt.legend()

# Lancement de l'animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=nd, blit=False, interval=100, repeat=False)
plt.show()

# Affichage optionnel du temps de calcul
# end_time = time.time()
# print(f"Temps d'exécution : {end_time - start_time:.2f} s")
