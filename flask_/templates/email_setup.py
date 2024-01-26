# setup.py

import os
import sys

# Ajouter le dossier parent au chemin d'accès
dossier_parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
dossier_parent = os.path.abspath(os.path.join(dossier_parent, os.pardir))
sys.path.append(dossier_parent)
