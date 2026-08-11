---
title: "Motion Machine SaaS"
date: 2025-12-18
description: "Le Motion-Lab de la HE-Arc est un espace technologique de pointe dédié à la capture et à l'analyse 3D du mouvement humain."
summary: "Le Motion-Lab de la HE-Arc est un espace technologique de pointe dédié à la capture et à l'analyse 3D du mouvement humain."
categories:
  - "TB"
statuts:
  - "Prospection"
---

Le Motion-Lab de la HE-Arc est un espace technologique de pointe dédié à la capture et à l'analyse 3D du mouvement humain.

Il repose sur l'utilisation de Motion Machine : un package Python offrant toutes les fonctionnalités relatives à l'animation de personnages 3D, de la gestion de la capture, au stockage, à la génération de mouvements et au streaming.

Il existe déjà des intégrations de Motion Machine pour Unity et Unreal Engine.

Le but de ce projet est de transformer Motion Machine en « AWS pour l'animation de personnages 3D ».

## Objectifs

### Principaux

- Concevoir une plateforme permettant d'héberger tous les services offerts par Motion Machine.
- Implémenter les APIs des services de Motion Machine avec FastAPI. Certains services comme le streaming d'animation, ou la génération de mouvements pourront servir d'exemples.
- Implémenter un système de gestion d'utilisateurs.
- Intégrer le tout comme un Dev Tool : tous les services doivent être accessibles grâce à une API en Python.

### Secondaires

- Concevoir un portail web permettant de créer des utilisateurs, de vérifier ses privilèges, etc.
- Implémenter une interface administrateur pour gérer les différents services.
- Implémenter un dashboard pour monitorer l'état des différents services.
