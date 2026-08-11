---
title: "BdD de Motion Capture"
date: 2025-12-18
description: "Le but de ce projet est de mettre en place une Base de Données pour gérer des fichiers de capture de mouvements."
summary: "Le but de ce projet est de mettre en place une Base de Données pour gérer des fichiers de capture de mouvements."
categories:
  - "TB"
  - "Projets P3"
statuts:
  - "Prospection"
---

Le but de ce projet est de mettre en place une Base de Données pour gérer des fichiers de capture de mouvements.

## Contexte

Le Motion-Lab de la HE-Arc est un espace technologique de pointe dédié à la capture et à l'analyse 3D du mouvement humain. Il génère et stocke une grande quantité de fichiers de mouvements 3D, sous différents formats. L'objectif de ce projet est de concevoir une base de données robuste et une intégration Python permettant d'indexer, rechercher, filtrer et exploiter ces assets de manière fiable.

## Objectifs

### Principaux

- Faire un état de l'art des bases de données existantes et de leur conception. Évaluer leur intégration dans notre propre base de données. Il faudra en particulier vérifier les droits d'utilisation.
- Concevoir et implémenter une base de données structurée pour la gestion de fichiers Motion Capture (MoCap) provenant de différentes sources (Motion-Lab @ HE-Arc, CMU MoCap, etc.).
- Définir un modèle de données cohérent couvrant sources, projets, sessions, acteurs, takes, fichiers et métadonnées associées (avec licences d'utilisation, etc.).
- Mettre en place une intégration complète en Python permettant d'effectuer toutes les opérations et requêtes sur la base de données (voir SQLAlchemy ou similaires).
- Permettre la recherche et le filtrage multi-critères des données MoCap (format, acteur, session, framerate, tags, dates, etc.) depuis Python.

### Secondaires (à définir)

- Implémenter un système d'import de fichiers de MoCap 3D. On pourra utiliser des scripts, un formulaire ou une GUI en fonction de ce qui est le plus pertinent.
- Détecter et gérer les doublons de fichiers.
- Prévoir un mécanisme d'annotations et de tags pour enrichir les données.
- Fournir des outils d'agrégation et de statistiques simples (inventaire, volumes, durées, formats).
- Mettre en place des outils de visualisation et de classification des animations 3D.
- Concevoir, implémenter et intégrer une API web pour utiliser la base de données.
