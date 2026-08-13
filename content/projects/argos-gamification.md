---
title: "ARGOS : gamification"
date: 2026-08-11
description: "Évaluer puis concevoir des mécaniques de jeu dans ARGOS pour soutenir la progression des étudiants en programmation C."
summary: "Évaluer puis concevoir des mécaniques de jeu dans ARGOS pour soutenir la progression des étudiants en programmation C."
categories:
  - "P3 HES d'été"
statuts:
  - "Idea"
aliases:
  - "/projects/gamifying-c-programming-learning/"
---

Évaluer puis concevoir des mécaniques de jeu dans ARGOS, pour soutenir la progression
des étudiants sur les exercices de programmation en C.

## Contexte

ARGOS corrige automatiquement les exercices de programmation en C et affiche les
résultats dans un dashboard. Il produit donc déjà tout ce dont une couche de
gamification a besoin : un identifiant d'exercice, un chapitre, une difficulté, un
état de réussite et des diagnostics.

Reste la vraie question, qui est le cœur de ce sujet : est-ce que des badges, des
points ou un classement améliorent réellement l'apprentissage, ou est-ce qu'ils
déplacent l'attention de l'étudiant vers le score ? Le projet commence par y répondre
avant de construire.

## Références

Deux plateformes à étudier, dont la combinaison est le point de départ de l'idée :

- [Stack Overflow](https://stackoverflow.com/help/badges) — son système de **badges**,
  attribués pour des actions précises et vérifiables plutôt que pour un volume brut,
  avec trois niveaux (bronze, argent, or) et des badges à obtention unique ou répétable.
  C'est le modèle de progression le plus documenté et le plus critiqué : les deux sont
  utiles ici.
- [SPOJ](https://www.spoj.com/) — Sphere Online Judge : un **juge en ligne** qui accepte
  ou rejette une soumission de code, avec des problèmes classés par difficulté et un
  classement des participants. C'est exactement la mécanique qu'ARGOS possède déjà sans
  l'exploiter, puisqu'il sait si un exercice passe ou non.

L'idée fondatrice tient en une phrase : **croiser le système de badges de Stack Overflow
avec le juge en ligne de SPOJ**, appliqué aux exercices de C corrigés par ARGOS.

## Objectifs

### Principaux

- Faire un état de l'art de la gamification dans l'apprentissage de la programmation,
  et en tirer ce qui est pertinent — et ce qui est contre-productif — pour ARGOS.
- Prendre connaissance du dashboard ARGOS et des données qu'il expose déjà.
- Concevoir les mécaniques retenues et les justifier au regard de l'état de l'art.
- Implémenter la couche de gamification dans le dashboard.

### Secondaires

- Visualiser la progression par chapitre et par difficulté.
- Proposer un exercice suivant en fonction de la progression.
- Mettre en place un mode d'évaluation permettant de mesurer l'effet sur une volée.
- Prévoir la désactivation complète de la gamification, par étudiant ou par cours.

## À rapprocher

[C Achievements in Unity]({{< relref "/projects/c-achievements-in-unity" >}}) a exploré
la même idée sans ARGOS, sous l'angle de la visualisation de la progression ; la
plateforme réalisée dans [ARGOS V2]({{< relref "/projects/argos-v2" >}}) fournit
désormais la base technique.
