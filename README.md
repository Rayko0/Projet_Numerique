# Simulation de l'effet Ramsauer–Townsend (Physique Moderne – CY Tech)

**Projet numérique – PréIng 2 MI1G – CY Tech 2024–2025**  
**Encadrant : P. Akridas**

---

## Objectif du projet

Ce projet a pour but de simuler numériquement la **diffusion quantique d’un paquet d’onde sur un puits de potentiel**, afin d’expliquer **l’effet Ramsauer–Townsend**, un phénomène où la probabilité de diffusion d’un électron par un atome de gaz noble **s’annule pour certaines énergies**.

---

## Objectifs pédagogiques

- Implémenter un **solveur numérique** de l'équation de Schrödinger dépendante du temps.
- Étudier la **transmission d’un paquet d’onde** à travers un potentiel en 1D.
- Analyser la **densité de probabilité** et la **section efficace de diffusion**.
- Comparer les **résultats numériques** aux **données expérimentales**.
- Renforcer les liens entre **physique quantique théorique** et **modélisation numérique**.

---

## Contenu du dépôt

| Fichier / Dossier                                              | Description                                                                                              |
|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| `src/propagation_paquet_onde.py`                               | Simulation principale : propagation d’un paquet d’onde dans un puits de potentiel (animation matplotlib). |
| `src/etat_stat_énergie.py`                                     | Calcul des fonctions d’onde stationnaires et de leurs énergies propres dans le puits.                     |
| `src/etat_stat_densité.py`                                     | Visualisation de la densité de probabilité associée aux états stationnaires.                              |
| `src/courbe_transmission.py`                                   | Génération de la courbe de transmission \( T(E) \) en fonction de l’énergie (Effet Ramsauer–Townsend).    |
| `outputs/data/propagation_paquet_onde.mp4`                     | Animation de la propagation du paquet d’ondes sauvegardée en vidéo (simulation dynamique).                |
| `outputs/data/densite.csv`                                     | Export CSV des valeurs de densité de probabilité calculées durant la simulation.                          |
| `Projet-Sujet_2024-2025_Physique-moderne_P2S2_PAkridas.pdf`    | Énoncé officiel du projet fourni par l’enseignant.                                                        |
| `README.md`                                                    | (ce fichier) Documentation complète du projet.                                                            |
| `requirements.txt`                                             | Dépendances nécessaires à l’exécution (numpy, matplotlib…).                                               |

---

## Dépendances

- Python ≥ 3.6  
- `numpy`
- `matplotlib`
- `pandas`

### Installation rapide et exécution

Dans \Projet_Numerique-main

`pip freeze > requirements.txt`

Dans \Projet_Numerique-main\src

`python [nom_du_fichier].py`

### Auteurs


Nino AUDREN

Timothé DESMARQUET
