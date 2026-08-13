---
title: "ARGOS : gamification"
date: 2026-08-11
description: "Évaluer puis concevoir des mécaniques de jeu dans ARGOS pour soutenir la progression des étudiants en programmation C."
summary: "Évaluer puis concevoir des mécaniques de jeu dans ARGOS pour soutenir la progression des étudiants en programmation C."
categories:
  - "P3 HES d'été"
statuts:
  - "Idea"
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

[CONCEPTION Gamifying C Programming Learning]({{< relref "/projects/gamifying-c-programming-learning" >}})
et [C Achievements in Unity]({{< relref "/projects/c-achievements-in-unity" >}}) ont
exploré la même idée sans ARGOS ; la plateforme réalisée dans
[ARGOS V2]({{< relref "/projects/argos-v2" >}}) fournit désormais la base
technique.
