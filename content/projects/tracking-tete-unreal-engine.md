---
title: "Tracking de tête temps réel dans Unreal Engine"
date: 2026-08-06
description: "Le but de ce projet est de tracker la position de la tête d'un utilisateur avec le système OptiTrack du Motion-Lab, et d'exploiter ces données dans Unreal Engine pour créer un…"
summary: "Le but de ce projet est de tracker la position de la tête d'un utilisateur avec le système OptiTrack du Motion-Lab, et d'exploiter ces données dans Unreal Engine pour créer un…"
categories:
  - "Projets P3"
statuts:
  - "Idea"
---

Le but de ce projet est de tracker la position de la tête d'un utilisateur avec le système OptiTrack du Motion-Lab, et d'exploiter ces données dans Unreal Engine pour créer un effet de perspective immersif.

## Contexte

Le Motion-Lab dispose d'un système de capture de mouvement OptiTrack composé de 14 caméras, capable de suivre avec précision des objets rigides en 6 degrés de liberté (position et orientation). L'objectif de ce projet est de concevoir et tracker un support léger (par exemple une paire de lunettes équipée de marqueurs) pour récupérer en temps réel la position de la tête d'un utilisateur. Ces données seront utilisées dans Unreal Engine pour contrôler la caméra et ajuster la perspective, offrant une sensation de profondeur et d'immersion 3D lorsque l'utilisateur se déplace devant l'écran.

## Pipeline

OptiTrack (Motive) → Transmission temps réel via Live Link → Unreal Engine (contrôle caméra) → Affichage immersif sur écran.

## Objectifs

### Principaux

- Concevoir et calibrer un objet rigide (lunettes ou équivalent) pour le tracking de tête dans OptiTrack.
- Transmettre les données de position/orientation en temps réel vers Unreal Engine via Live Link.
- Contrôler la caméra dans Unreal Engine pour adapter la perspective aux mouvements réels de l'utilisateur.

### Secondaires

- Implémenter un filtrage pour réduire le jitter et améliorer la stabilité du rendu.
- Créer une petite scène 3D fixe permettant de démontrer clairement l'effet d'immersion.
- Expérimenter des extensions (stéréoscopie, ajout d'objets virtuels fixes dans l'espace).
