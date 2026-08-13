---
title: "Spatialisation temps réel sur Sonos Era 300"
date: 2026-08-06
description: "Le but de ce projet est de jouer un son en temps réel sur les quatre enceintes Sonos Era 300 du Motion-Lab, en faisant varier dynamiquement leur volume pour simuler le déplacement…"
summary: "Le but de ce projet est de jouer un son en temps réel sur les quatre enceintes Sonos Era 300 du Motion-Lab, en faisant varier dynamiquement leur volume pour simuler le déplacement…"
categories:
  - "Projets P3"
statuts:
  - "Completed"
---

Le but de ce projet est de jouer un son en temps réel sur les quatre enceintes Sonos Era 300 du Motion-Lab, en faisant varier dynamiquement leur volume pour simuler le déplacement d'une source sonore dans l'espace.

## Contexte

Le Motion-Lab dispose de quatre enceintes Sonos Era 300, capables de produire un son immersif. L'objectif de ce projet est de jouer un son en temps réel sur ces enceintes et de faire varier dynamiquement leur volume respectif pour créer l'illusion que la source sonore se déplace dans l'espace autour de l'auditeur. Ce projet mettra en œuvre à la fois le contrôle logiciel des Sonos et la gestion en temps réel de paramètres audio spatiaux.

## Pipeline

Application de contrôle (API Sonos ou protocole UPnP) → Gestion en temps réel des volumes des quatre enceintes → Synchronisation audio → Restitution spatialisée dans le Motion-Lab.

## Objectifs

### Principaux

- Établir la connexion et le contrôle des Sonos Era 300 via API ou protocole réseau compatible.
- Jouer un son en temps réel de manière parfaitement synchronisée sur les quatre enceintes.
- Implémenter une variation dynamique des volumes pour simuler le déplacement de la source sonore dans l'espace.

### Secondaires

- Créer une interface visuelle pour contrôler la position virtuelle de la source sonore.
- Expérimenter différentes trajectoires et vitesses de déplacement du son.
- Intégrer des capteurs de position (ex. OptiTrack) pour que la spatialisation s'adapte à la position de l'auditeur.

## Réalisation

Sujet proposé et livré en projet de semestre P3 durant l'année académique 2025-2026.
