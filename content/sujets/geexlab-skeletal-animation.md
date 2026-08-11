---
title: "GeeXLab + Skeletal Animation : faire install, auto-update, etc."
date: 2022-10-05
description: "Industrialiser la distribution du package d'animation squelettique pour GeeXLab : CI/CD, installeurs multiplateformes et mise à jour automatique."
summary: "Industrialiser la distribution du package d'animation squelettique pour GeeXLab : CI/CD, installeurs multiplateformes et mise à jour automatique."
categories:
  - "Ra&D"
  - "TB"
  - "Python"
statuts:
  - "Next Up"
tags:
  - "Python"
  - "CI/CD"
---

Industrialiser la distribution du package d'animation squelettique pour GeeXLab :
chaîne d'intégration continue, installeurs multiplateformes et mise à jour automatique.

## Objectifs

- Mettre en place un CI/CD sur GitLab
- Créer des runners (Windows, Mac et Linux)
- Créer des installeurs (multiplateformes)
- Créer des tests automatiques pour le package d'animation
- Créer des tests automatiques pour l'affichage
- Créer des auto-updaters (Windows, Linux, Mac)

## Installation (ZIP)

- Dans GeeXLab_win64_lite décompressé il faut garder :
  - libs/common, libs/python, plugins/, scripts/, shaders/
  - conf.xml, EULA.txt
  - GeeXLab.exe, GeeXLab_cli.exe, gxc_x64.dll, gxl_x64.dll
  - icon.ico, imgui.ini, init0.xml
- Pour mettre à jour il faut remplacer :
  - libs/common, libs/python, plugins/
  - GeeXLab.exe, GeeXLab_cli.exe, gxc_x64.dll, gxl_x64.dll
- Python
  - Lien pour la version 3.8.10 : [https://www.python.org/downloads/release/python-3810/](https://www.python.org/downloads/release/python-3810/), téléchargement direct : [https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe)
  - De préférence déjà pré-installé, ou bien avec .exe d'installation mis à disposition et installé sur le moment
  - Créer un environnement virtuel dans l'installation GXL : python.exe -m venv /path/to/virtualenv → à tester !
  - Changer « python3_home » dans le fichier init0.xml de GXL pour virtualenv/Scripts/
  - Préparer un fichier de prérequis pour pip : [https://pip.pypa.io/en/stable/reference/requirements-file-format/](https://pip.pypa.io/en/stable/reference/requirements-file-format/)
  - Installer les packages nécessaires dans le virtualenv avec pip install -r requirement.txt

## Créer un installeur

- En créant un fichier .msi : [https://learn.microsoft.com/en-us/windows/msix/app-installer/how-to-create-appinstaller-file](https://learn.microsoft.com/en-us/windows/msix/app-installer/how-to-create-appinstaller-file)
- Avec un script bash à exécuter qui lancerait tout le processus via un script Python
- En créant un .exe, apparemment Windows a un outil déjà installé « IExpress », mais je ne sais pas ce que ça vaut.
