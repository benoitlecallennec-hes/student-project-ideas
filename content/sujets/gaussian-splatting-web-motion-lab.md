---
title: "Gaussian Splatting Web du Motion-Lab"
date: 2026-08-06
description: "Le but de ce projet est de représenter visuellement le Motion-Lab sur le Web en utilisant la technique du 3D Gaussian Splatting."
summary: "Le but de ce projet est de représenter visuellement le Motion-Lab sur le Web en utilisant la technique du 3D Gaussian Splatting."
categories:
  - "Projets P3"
statuts:
  - "Idea"
---

Le but de ce projet est de représenter visuellement le Motion-Lab sur le Web en utilisant la technique du 3D Gaussian Splatting.

## Contexte

Le Motion-Lab est équipé pour capturer et modéliser des environnements réels avec une grande précision. L'objectif de ce projet est de représenter visuellement le Motion-Lab sur le Web en utilisant la technique du *3D Gaussian Splatting*, une méthode récente permettant de reconstruire et afficher des scènes 3D photoréalistes à partir de jeux d'images. Le rendu devra être consultable en ligne, offrant aux visiteurs la possibilité d'explorer virtuellement le Motion-Lab depuis un navigateur.

## Pipeline

Capture photo/vidéo du Motion-Lab → Reconstruction 3D via Gaussian Splatting → Export vers un format compatible Web (WebGL / Three.js) → Visualisation interactive dans un navigateur.

## Objectifs

### Principaux

- Réaliser la capture d'images du Motion-Lab selon un protocole optimisé pour le Gaussian Splatting.
- Traiter les données pour obtenir un modèle 3D photoréaliste.
- Intégrer le rendu interactif sur le Web via un moteur 3D (Three.js ou équivalent).

### Secondaires

- Ajouter des points d'intérêt cliquables pour décrire certains équipements du Motion-Lab.
- Optimiser la taille et les performances pour une navigation fluide sur navigateur.
- Proposer plusieurs points de vue prédéfinis pour guider la visite virtuelle.

## À rapprocher

Le projet [Web Viewer pour insectes]({{< relref "/sujets/web-viewer-pour-insectes" >}}) emploie la même technique de reconstruction, mais appliquée à des scans d'insectes.
