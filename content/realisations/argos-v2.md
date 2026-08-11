---
title: "ARGOS V2"
date: 2025-12-19
description: "ARGOS est un outil de correction automatique d'exercices de programmation en C, basé sur GCC, CMake et Ninja."
summary: "ARGOS est un outil de correction automatique d'exercices de programmation en C, basé sur GCC, CMake et Ninja."
categories:
  - "TB"
statuts:
  - "Completed"
---

## Contexte

ARGOS est un outil de correction automatique d'exercices de programmation en C, basé sur GCC, CMake et Ninja.

La 1ère version, déployée sur GitLab et dépendante de son infrastructure CI/CD, s'est révélée difficile à maintenir. Une refonte a permis de développer **ARGOS CLI**, capable d'exécuter localement les compilations et les tests. Ce travail de bachelor vise à développer **ARGOS V2**, une plateforme entièrement locale intégrant un **dashboard web**, tout en renforçant la structuration pédagogique et la qualité des retours fournis aux étudiants. Le projet sera **hébergé sur GitHub**, afin d'améliorer la maintenabilité et la diffusion.

## Objectifs

### Principaux

- Concevoir **ARGOS V2**, une plateforme locale de correction automatique d'exercices en C.
- Intégrer **ARGOS CLI** comme moteur d'exécution (compilation, tests, analyse).
- Développer un **dashboard web local** pour visualiser les résultats et incluant :
  - un **diagramme radar** de compétences/notions,
  - des **diagnostics automatiques** sur les exercices,
  - l'**extraction et l'affichage structurés** :
    - des **warnings** du compilateur,
    - des **erreurs de compilation**,
    - des **erreurs issues des tests unitaires**.
- Héberger et versionner le projet sur **GitHub**.

### Secondaires

- Définir et imposer un **identifiant unique d'exercice**, partagé entre énoncé, squelette et tests.
- Ajouter dans chaque squelette un **en-tête structuré minimal** (ID, chapitre/thème, lien vers l'énoncé).
- Afficher dans le dashboard **ARGOS V2** des liens directs vers les énoncés.
- Permettre des **statistiques par notion et par chapitre** dans le dashboard.
- Ajouter une visualisation de complétion des exercices, en fonction de leur difficulté.
