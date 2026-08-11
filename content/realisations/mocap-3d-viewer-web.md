---
title: "MoCap 3D Viewer Web"
date: 2025-12-18
description: "Le but de ce projet est de porter MotionMachine sur le web en utilisant WebGPU."
summary: "Le but de ce projet est de porter MotionMachine sur le web en utilisant WebGPU."
categories:
  - "TB"
statuts:
  - "Completed"
---

Le but de ce projet est de porter MotionMachine sur le web en utilisant WebGPU.

## Contexte

MotionMachine est un système de lecture et de génération d'animations 3D en temps-réel. Le tout est implémenté en Python, et exposé via une API web. Pour le moment, il existe des clients pour Unity, Unreal Engine 5, ainsi que pour GeeXLab (Python). Le but de ce projet est de porter MotionMachine sur le web en utilisant WebGPU.

## Objectifs

### Principaux

- Prendre connaissance de l'API web de MotionMachine.
- Implémenter un viewer 3D WebGPU (ou avec Babylon.js, Three.js, etc.) permettant de lire des animations 3D streamées par MotionMachine.
- Afficher les animations 3D dans une scène 3D.

### Secondaires

- Implémenter une GUI pour contrôler les animations 3D.
- Concevoir un système permettant d'afficher les trajectoires de points spécifiques (trails).
- Ajouter dans la GUI la possibilité de gérer les paramètres de connexion et de sessions.
- Évaluer les performances du viewer en fonction du nombre d'animations 3D streamées en direct.
