# LinguistiX

LinguistiX est un outil simple de linguistique de corpus écrit en Python. Il
permet de lire des fichiers texte, de tokeniser leur contenu et de calculer des
fréquences de mots.

## Installation

Assurez‑vous de disposer de Python 3.8 ou plus récent. Aucune dépendance
externe n'est nécessaire pour les fonctionnalités de base.

## Utilisation en ligne de commande

```bash
python -m linguistix.cli chemin/vers/fichier.txt
```

Par défaut, les dix mots les plus fréquents sont affichés. Utilisez `-n` pour
changer ce nombre :

```bash
python -m linguistix.cli -n 20 fichier1.txt fichier2.txt
```

## Interface graphique

Une petite interface Tkinter est disponible pour analyser des fichiers sans
utiliser la ligne de commande :

```bash
python -m linguistix.gui
```

## Tests

Lancez la suite de tests unitaires avec :

```bash
PYTHONPATH=. pytest -q
```
